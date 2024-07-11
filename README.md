# [MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning](https://arxiv.org/abs/2311.10774)

<div align="center">
  <a href="https://arxiv.org/abs/2311.10774"><img src="https://img.shields.io/badge/Paper-arXiv-red" alt="arXiv"></a>
  <a href="https://huggingface.co/datasets/xywang1/MMC"><img src="https://img.shields.io/badge/Dataset-%F0%9F%A4%97%20Hugging_Face-yellow" alt="Hugging Face"></a>
  <a href="https://aclanthology.org/2024.naacl-long.70"><img src="https://img.shields.io/badge/NAACL-2024-blue" alt="NAACL 2024"></a>
</div>

This is the official GitHub repo of the paper [MMC: Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning](https://arxiv.org/abs/2311.10774).

## News

- [Jul. 9, 2024] 🔥🔥🔥 Our dataset is now released through [Hugging Face Datasets](https://huggingface.co/datasets/xywang1/MMC).
- [Mar. 13, 2024] Our paper is accepted to [NAACL 2024](https://aclanthology.org/2024.naacl-long.70).
- [Nov. 15, 2023] Our paper is available on [arXiv](https://arxiv.org/abs/2311.10774).

## Highlights

- We introduce a large-scale MultiModal Chart Instruction (**MMC-Instruction**) dataset supporting diverse tasks and chart types. Leveraging this data.
- We also propose a Multi-Modal Chart Benchmark (**MMC-Benchmark**), a comprehensive human-annotated benchmark with nine distinct tasks evaluating reasoning capabilities over charts. Extensive experiments on MMC-Benchmark reveal the limitations of existing LMMs on correctly interpreting charts, even for the most recent GPT-4V model.
- We develop Multi-Modal Chart Assistant (MMCA), an LMM that achieves state-of-the-art performance on existing chart QA benchmarks.

<div align="center">
<img src="./images/overview.png" width="90%">
</div>

## Data Release

The chart-text alignment data (MMC-Alignment), chart instruction-tuning data (MMC-Instruction), and benchmark data (MMC-Benchmark) introduced in our [paper](https://arxiv.org/abs/2311.10774) can be downloaded from [Hugging Face Datasets](https://huggingface.co/datasets/xywang1/MMC) using git clone:
```
git lfs install
git clone https://huggingface.co/datasets/xywang1/MMC
```

It contains three sub-directories MMC-Alignment, MMC-Benchmark, and MMC-Instruction:

### MMC-Alignment

- mmc_chart_text_alignment_arxiv_text.jsonl: 250,000 samples for chart-text alignment training.
- mmc_chart_text_alignment_arxiv_images.tar.gz: images for mmc_chart_text_alignment_arxiv_text.jsonl.

### MMC-Benchmark

- mmc_benchmark_text.jsonl: 2,126 instances for testing and benchmarking.
- mmc_benchmark_images.tar.gz: images for mmc_benchmark_text.jsonl.

### MMC-Instruction

- mmc_instruction_arxiv_text.jsonl: 300,000 question-answer pairs synthesized with arXiv data for instruction tuning.
- mmc_instruction_arxiv_images.tar.gz: images for mmc_instruction_arxiv_text.jsonl.
- mmc_instruction_non-arxiv_text.jsonl: 110,020 extra question-answer pairs for instruction tuning.
- mmc_instruction_non-arxiv_images.tar.gz: images for mmc_instruction_non-arxiv_text.jsonl.

## Existing Datasets

As mentioned in the [paper](https://arxiv.org/abs/2311.10774), chart summarization datasets from Statist, PlotQA, [VisText](https://github.com/mitvis/vistext), ChartInfo, and Unichart are used in our experiments for chart-text alignment training. Please refer to the following script for details:
```
# Existing chart-text alignment images
gdown https://drive.google.com/uc?id=1e1mx_nb5PWjPkuIsJkY8B4xSET9DOWTa
# Existing chart-text alignment text
gdown https://drive.google.com/uc?id=18SJ13V4qEt1ixOQPbRmEnZKQrjS5v14T
```

For existing Chart QA training data, please refer to the following script:
```
# Existing chart qa images
gdown https://drive.google.com/uc?id=1Y17wNYdBlPxhB5KKiux2BD8C2FlA5MC9
# Existing chart qa text
gdown https://drive.google.com/uc?id=1tUtntLRgsBJ9v5NcdTMvVI32ruLHAyFe
```

## MMCA Gradio demo

**1. Install the environment according to [mplug-owl](https://github.com/X-PLUG/mPLUG-Owl#Usage).**

We finetuned mplug-owl on 8 V100. If you meet any questions when implement on V100, feel free to let me know!

**2. Download the Checkpoint**

```
gdown https://drive.google.com/uc?id=11KJA8bSNi1yxgcijsG3xfBHvWe8C748F
```

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

## Contact

If you have any questions about this work, please email Fuxiao Liu [fl3es@umd.edu](fl3es@umd.edu).

## Citation

```
@article{liu2023mmc,
  title={MMC: Advancing Multimodal Chart Understanding with Large-scale Instruction Tuning},
  author={Liu, Fuxiao and Wang, Xiaoyang and Yao, Wenlin and Chen, Jianshu and Song, Kaiqiang and Cho, Sangwoo and Yacoob, Yaser and Yu, Dong},
  journal={arXiv preprint arXiv:2311.10774},
  year={2023}
}
```

## Disclaimer

We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes.
