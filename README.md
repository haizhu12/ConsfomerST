# Joint Transformer and Contrast Learning for Subject-driven Image Style Transfer

<p align="center">
  <a href="https://github.com/haizhu12/HumSTN">Project Page</a> |
  <a href="#QuickStart">QuickStart</a> |
  <a href="#Training">Training</a> |
  <a href="#Acknowledge">Acknowledge</a> |
</p>

<div align="center">
  <img src="figure/teaser.png" width="1000"/>
</div>

This is a pytorch implementation of consformerST, a unified general-purpose framework for coordinating computer vision tasks with human instructions.[STYTR2](https://github.com/diyiiyiii/StyTR-2),[QuantArt](https://github.com/siyuhuang/QuantArt) and [IEContraAST](https://github.com/HalbertCH/IEContraAST).<br>
### Introduction
![Image_start](https://github.com/haizhu12/ConsfomerST/assets/93024130/06562502-376f-409a-88ae-a56e41b624b3)

## QuickStart
Follow the steps below to quickly edit your own images. The inference code in our repository requires **one GPU with > 24GB memory** to test images with a resolution of **256**.

1. Clone this repo.
2. Setup conda environment:
   ```
   conda create -n consformerST python=3.8
   conda activate consformerST
   ```
3. We provide a well-trained [checkpoints](https://pan.baidu.com/s/13-l1Jcz340MjT3RBAS_9sA?pwd=81y1)
 
 提取码：**81y1**
Download checkpoints, put it into chickpoints.
 [models](https://pan.baidu.com/s/14in-oWN3UeAXkb5p6Fe66g?pwd=2ij2)
提取码：**2ij2** .
Download checkpoints, put it into models.

## Model Training  
- Download the content dataset: [MS-COCO](https://cocodataset.org/#download).
- Download the style dataset: [WikiArt](https://www.kaggle.com/c/painter-by-numbers).
```bash

5. (Optional) You can launch your own interactive editing Gradio app:
```bash
python edit_app.py 

# You can also specify the path to the checkpoint
# The default checkpoint is checkpoints/v1-5-pruned-emaonly-adaption-task-humanalign.ckpt
python edit_app.py --ckpt checkpoints/v1-5-pruned-emaonly-adaption-task-humanalign.ckpt
```

## Training
The code is developed using python 3.8 on Ubuntu 20.04. The code is developed and tested using RTX3090 GPU cards, each with 24GB of memory. Other platforms are not fully tested.
### Datasets

   Then put your content images in ./datasets/{datasets_name}/testA, and style images in ./datasets/{datasets_name}/testB.
   
   Example directory hierarchy:
   ```sh
      consformerST
      |--- datasets
             |--- {datasets_name}
                   |--- trainA
                   |--- trainB
                   |--- testA
                   |--- testB
                   
      Then, call --dataroot ./datasets/{datasets_name}
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation
   Clone the repo
   ```sh
   git clone https://github.com/haizhu12/HumSTN
   ```

<p align="right">(<a href="#top">back to top</a>)</p>
3. Setup conda environment:
   ```
   conda create -n consformerST
   conda activate consformerST
   ```

### Pre-trained Model Preparation
You can use the following command to download the official pre-trained stable diffusion model, or you can download the model trained by our pretraining adaptation process from [OneDrive](https://mailustceducn-my.sharepoint.com/:u:/g/personal/aa397601_mail_ustc_edu_cn/EXJSMIpFev5Nj0kuKI88U1IBZDSjegp3G8ukku0OxRRjFQ?e=QhnnB4) and put it into the following folder: stable_diffusion/models/ldm/stable-diffusion-v1/.
   ```
   bash scripts/download_pretrained_sd.sh
   ```

### Data Preparation
You can refer to the [dataset](https://github.com/cientgu/InstructDiffusion/tree/main/dataset) to prepare your data.

### Training Command
For multi-GPU training on a single machine, you can use the following command:
   ```
   python -m torch.distributed.launch --nproc_per_node=8 main.py --name v0 --base configs/instruct_diffusion.yaml --train --logdir logs/instruct_diffusion
   ```

For multi-GPU training on multiple machines, you can use the following command (assuming 6 machines as an example):
   ```
   bash run_multinode.sh instruct_diffusion v0 6
   ```

## Acknowledge

Thanks to 
- [QuantArt](https://github.com/siyuhuang/QuantArt)
- [Instruct-pix2pix](https://github.com/timothybrooks/instruct-pix2pix)
- [STYTR2](https://github.com/diyiiyiii/StyTR-2)

## Citation

```
noon
```

