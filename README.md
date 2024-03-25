
# MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning [[NAACL 2024]](https://2024.naacl.org)

This is the PyTorch implementation of the paper ***MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning***, the paper is available at https://arxiv.org/abs/2311.10774.

# Contact

If you have any questions about this work, please email Fuxiao Liu [fl3es@umd.edu](fl3es@umd.edu). 

# Note

- We introduce a large-scale MultiModal Chart Instruction (**MMC-Instruction**) dataset supporting diverse tasks and chart types. Leveraging this data.
- We develop Multi-Modal Chart Assistant (MMCA), an LMM that achieves state-of-the-art performance on existing chart QA benchmarks.
- We also propose a Multi-Modal Chart Benchmark (**MMC-Benchmark**), a comprehensive human-annotated benchmark with nine distinct tasks evaluating reasoning capabilities over charts. Extensive experiments on MMC-Benchmark reveal the limitations of existing LMMs on correctly interpreting charts, even for the most recent GPT-4V model. 

<p align="center">
    <a href="https://llava.hliu.cc/"><img src="./images/WechatIMG6440.jpg" width="100%"></a> <br>
</p>

# News

- [03/13]🔥 Our paper ["MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning"](https://arxiv.org/pdf/2311.10774.pdf) is accepted to **[NAACL 2024](https://2024.naacl.org)**.
- [02/26]🔥 Our paper ["HallusionBench: You See What You Think? Or You Think What You See? An Image-Context Reasoning Benchmark Challenging for GPT-4V(ision), LLaVA-1.5, and Other Multi-modality Models"](https://arxiv.org/abs/2310.14566) is accpeted to **[CVPR 2024](https://cvpr.thecvf.com)**.
- [01/15]🔥 Our paper [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](http://arxiv.org/abs/2306.14565) is accepted by **[ICLR 2024](https://iclr.cc)**

## MMC-Instruction Dataset
### Non-arxiv
```
#Part 1
#Images
gdown https://drive.google.com/file/d/1Y17wNYdBlPxhB5KKiux2BD8C2FlA5MC9
#Text
gdown https://drive.google.com/file/d/1tUtntLRgsBJ9v5NcdTMvVI32ruLHAyFe
#Part2
#Images
gdown https://drive.google.com/uc?id=1Dey-undzW2Nl21CYLFSkP_Y4RrfRJkYd
#Text
gdown https://drive.google.com/uc?id=13j2U-ectsYGR92r6J5hPdhT8T5ezItHF
#Part3
#Images
gdown https://drive.google.com/file/d/1W8sQ6fLkOm8bZo_SrRIiIGELS90aNKq7
#Text
gdown https://drive.google.com/file/d/1o3Edkf6bdyZloe_FSth8wtNmkFf_Bda_
```
### arxiv
```
#Images
gdown https://drive.google.com/file/d/1QKQOMIH9Wd3EQEYr3IV2u9qQXmSZy49G
#Text
gdown https://drive.google.com/file/d/1PI1EdgPk-gBi29adk25cjGtwskyBjcN9
```


## MMC-Benchmark
### Images
```
gdown https://drive.google.com/file/d/19CA-AFKshOVEOabK3-pkkZfjbtaJFP7Y
```
### Questions and Answers
```
gdown https://drive.google.com/file/d/1HOVhPuFJ0roaHt-6AFyYX2E5MxKjoFug
```

## MMCA Gradio demo

**1. Install the environment according to [mplug-owl](https://github.com/X-PLUG/mPLUG-Owl#Usage).**

We finetuned mplug-owl on 8 V100. If you meet any questions when implement on V100, feel free to let me know!

**2. Download the Checkpoint**

**3. Edit the Code**

As for the `mplug-owl/serve/model_worker.py`, edit the following code and enter the path of the lora model weight in lora_path.
```
self.image_processor = MplugOwlImageProcessor.from_pretrained(base_model)
self.tokenizer = AutoTokenizer.from_pretrained(base_model)
self.processor = MplugOwlProcessor(self.image_processor, self.tokenizer)
self.model = MplugOwlForConditionalGeneration.from_pretrained(
     base_model,
     load_in_8bit=load_in_8bit,
     torch_dtype=torch.bfloat16 if bf16 else torch.half,
     device_map="auto"
 )
self.tokenizer = self.processor.tokenizer

        
peft_config = LoraConfig(target_modules=r'.*language_model.*\.(q_proj|v_proj)', inference_mode=False, r=8,lora_alpha=32, lora_dropout=0.05)
self.model = get_peft_model(self.model, peft_config)
lora_path = 'Your lora model path'
prefix_state_dict = torch.load(lora_path, map_location='cpu')
self.model.load_state_dict(prefix_state_dict)
```

**4. Local Demo**

When you launch the demo in local machine, you might find there is no space for the text input. This is because of the version conflict between python and gradio. The simplest solution is to do `conda activate LRV`

```
python -m serve.web_server --base-model 'the mplug-owl checkpoint directory' --bf16
```

## Citation

```
@article{liu2023mmc,
  title={MMC: Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning},
  author={Liu, Fuxiao and Wang, Xiaoyang and Yao, Wenlin and Chen, Jianshu and Song, Kaiqiang and Cho, Sangwoo and Yacoob, Yaser and Yu, Dong},
  journal={arXiv preprint arXiv:2311.10774},
  year={2023}
}
```

# Disclaimer

We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes.

