# MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning

This repo contains the evaluation code for the paper "[MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning](https://arxiv.org/pdf/2311.10774.pdf)"

```
@article{liu2023mmc,
  title={MMC: Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning},
  author={Liu, Fuxiao and Wang, Xiaoyang and Yao, Wenlin and Chen, Jianshu and Song, Kaiqiang and Cho, Sangwoo and Yacoob, Yaser and Yu, Dong},
  journal={arXiv preprint arXiv:2311.10774},
  year={2023}
}
```

- We introduce a large-scale MultiModal Chart Instruction (MMC-Instruction) dataset comprising 600k instances supporting diverse tasks and chart types. Leveraging this data.
- We develop Multi-Modal Chart Assistant (MMCA), an LMM that achieves state-of-the-art performance on existing chart QA benchmarks.
- We also propose a Multi-Modal Chart Benchmark (MMC-Benchmark), a comprehensive human-annotated benchmark with nine distinct tasks evaluating reasoning capabilities over charts. Extensive experiments on MMC-Benchmark reveal the limitations of existing LMMs on correctly interpreting charts, even for the most recent GPT-4V model. 

<p align="center">
    <a href="https://llava.hliu.cc/"><img src="./images/WechatIMG6440.jpg" width="100%"></a> <br>
</p>

## Updates
- [-/-]🔥 Our **MMC-Instruction** and Evaluation Code will be released soon.
- [12/20]🔥 Our **MMC-Benchmark** is available.


## Evaluation
### Images
```
gdown https://drive.google.com/file/d/19CA-AFKshOVEOabK3-pkkZfjbtaJFP7Y
```
### Questions and Answers
```
```
### Implementation

```
git clone https://github.com/FuxiaoLiu/MMC.git
cd ./Eval
python eval.py --path OUTPUT_PATH --subject ALL # all subject
```

# Contact
Fuxiao Liu [fl3es@umd.edu](fl3es@umd.edu). 
