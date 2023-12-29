"""Parse and Evalate"""
import os
import json
from argparse import ArgumentParser

from utils import save_json, CAT_SHORT2LONG,evaluate, parse_multi_choice_response, parse_open_response


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--path', type=str, default="", help="The path to model output directory.")
    parser.add_argument('--subject', nargs='+',
                        help=f'The name of the sub-task. Availble: {CAT_SHORT2LONG.keys()} or ALL')

    args = parser.parse_args()
    if args.subject[0] == 'ALL':
        args.subject = CAT_SHORT2LONG.keys()
    ex_output_path = os.path.join(args.path)
    
    print('ex_output_path:', ex_output_path)

    all_results = {}
    print('args.subject:', args.subject, '\n')
    for cat_short in args.subject:
        category = CAT_SHORT2LONG[cat_short]
        print("Evaluating: {}".format(category))
        if category not in os.listdir(ex_output_path):
            print("Skipping {} for not found".format(category))
        else:
            cat_folder_path = os.path.join(ex_output_path, category)
            cat_outputs = json.load(open(os.path.join(cat_folder_path, 'output.json')))
            
            print('cat_outputs:', len(cat_outputs), '\n')
            print(cat_outputs[:1], '\n')
            cat_outputs = [{'id': 'validation_Electronics_1', 'question_type': 'multiple-choice', 'answer': 'A', 'all_choices': ['A', 'B'], 'index2ans': {'A': 'yes, saturation', 'B': 'no, not in saturation'}, 'response': 'yes, not in saturation'}] 
            #cat_outputs = [{'answer': 'A', 'question_type': 'multiple-choice', 'index2ans': {'A': 'yes, saturation', 'B': 'no, not in saturation'}, 'response': 'yes, not in saturation'}] 
            print(cat_outputs)
            
            # Evaluation
            eval_samples = []
            for cat_output in cat_outputs:
                response = cat_output['response']
                if cat_output['question_type'] == 'multiple-choice':                    
                    all_choices = cat_output['all_choices']
                    index2ans = cat_output['index2ans']
                    parsed_pred = parse_multi_choice_response(response, all_choices, index2ans)
                    print('test:', all_choices, index2ans, parsed_pred,'\n')
                    eval_samples.append(
                        {
                            'id': cat_output['id'],
                            'question_type': cat_output['question_type'],
                            'answer': cat_output['answer'], # the content in option, not answer index.
                            'response': response,
                            'parsed_pred': parsed_pred,
                            'index2ans': index2ans,
                        }
                    )
                else:  # open
                    parsed_pred = parse_open_response(response)
                    eval_samples.append(
                        {
                            'id': cat_output['id'],
                            'question_type': cat_output['question_type'],
                            'answer': cat_output['answer'],
                            'response': response,
                            'parsed_pred': parsed_pred,
                        }
                    )

            print("Num of valid samples: {}, Expected Num: {}".format(len(eval_samples), len(cat_outputs)))
            
            judge_dict, metric_dict = evaluate(eval_samples)
            metric_dict.update({"num_example": len(eval_samples)})
            for eval_sample in eval_samples:
                eval_sample.update({"judge": judge_dict[eval_sample['id']]})
            print('metric_dict:', metric_dict)
            save_json(os.path.join(cat_folder_path, 'parsed_output.json'), eval_samples)
            save_json(os.path.join(cat_folder_path, 'result.json'), metric_dict)
