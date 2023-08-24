# MMC: Evaluating Large Multimodal Models for Chart Understanding

![image](./dataset1.jpg)

Multimodal Large Language Model (MLLM) relies on the powerful LLM to perform multimodal tasks, showing amazing emergent abilities in recent studies, such as writing poems based on an image. However, it's still lacking a comprehensive evaluation for chart understanding. In this paper, we fill in this blank, presenting the **MMC**, a first **human-annotated** benchmark, consisting of 2k instructions, 9 tasks, various topics and unbound chart types for chart understanding. The 9 tasks are :

**Chart Information Extraction, Chart Reasoning, Contextual Chart Understanding, Multiple Chart Understanding, Chart Type Classification, Chart Topic Classification, Stock Chart Analysis, Chart2datatable,Chart2json**

## Data
### Dataset Statistic

| Benchmark | Customized Question | #Answer Annotation |Image Type |# of Tasks for Chart Understanding | # Human Check|
| --- | --- | --- | --- |--- |---: |
| MME | yes | 2194 | General |N/A | yes |
| LAMM | no | - | Point Cloud |N/A | no |
| PlotQA | no | - | Chart |1 | no |
| **MMC** | yes | 2130 | Chart |9 | yes |


### Access the data
* You can download the data from [here](). Stay Tunned! You can also email fl3es@umd.edu.

## Evaluation
Since the output of the model is limited to two types (“yes” or “no”), it is convenient to measure the metrics of accuracy and accuracy+. The former is calculated based on each question, while the latter is based on each image where both of the two questions need to be answered correctly. The random accuracies of the two metrics are equal to 50% and 25%, respectively. 


## Evaluation Results

| Model |Chart Information Extraction | Chart Reasoning | Contextual Chart Understanding |Multiple Chart Understanding | Chart Type Classification|Chart Topic Classification|Stock Chart Analysis|Chart2datatable|Chart2json|Average|
| --- | --- |--- |--- |--- |--- | --- | --- |--- |--- |---: |
| MiniGPT4 | 0.51 | 0.45 | 0.43 |0.44| 0.54 |0.54 |0.56 |0.50 |0.50 |0.49 |
| Mplug-Owl | 0.55 | 0.54 | 0.53 |0.60| 0.53 |0.50 |0.55 |0.55 |0.54 |0.54 |





## Citation
If you find this useful in your research, please consider citing it:
