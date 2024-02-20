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
- Download the content dataset: [Celeba-HQ](https://paperswithcode.com/dataset/celeba-hq).
- Download the style dataset: [WikiArt](https://www.kaggle.com/c/painter-by-numbers).



5. (Optional) Some experimental results app:
   
![qualitative](https://github.com/haizhu12/ConsfomerST/assets/93024130/c8cf0fcf-65ee-4cc7-a086-83ab6d776410)



**You can also specify the path to the checkpoint**

[checkpoints](https://pan.baidu.com/s/13-l1Jcz340MjT3RBAS_9sA?pwd=81y1)

**The default checkpoint is style_vgg.pth**

Google Drive: Check [here](https://drive.google.com/file/d/12JKlL6QsVWkz6Dag54K59PAZigFBS6PQ/view?usp=sharing)

**VGG Module：vgg_normalised.pth**

Google Drive: Check [here](https://drive.google.com/file/d/1DKYRWJUKbmrvEba56tuihy1N6VrNZFwl/view?usp=sharing)

6.Main implementation framework
![main](https://github.com/haizhu12/ConsfomerST/assets/93024130/98a54aa5-08a6-4de8-a2bc-084083c35246)




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

   1.conda create -n consformerST
   
   2.conda activate consformerST
   
   3.pip install -r requirements.txt
   
   4.pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html


  pytorch [pytorch](https://pytorch.org/get-started/previous-versions/)

**Execute a command**

### train
   ```sh
   python train.py --dataroot ./datasets/{dataset_name} --name {model_name}
   ```

### test

   Test the CAST or UCAST model:
   
   ```sh
   python test.py --dataroot ./datasets/{dataset_name} --name {model_name}
   ```
   
## Runtime Controls:

**Content-style trade-off:**

  `python test.py --content inputs/content/1.jpg --style inputs/style/1.jpg --phi 0.5`
  
![stylecontrol](https://github.com/haizhu12/ConsfomerST/assets/93024130/d9fad21b-0fd1-4322-9006-c76422e2c93c)






## Acknowledge

Thanks to 
- [QuantArt](https://github.com/siyuhuang/QuantArt)
- [Instruct-pix2pix](https://github.com/timothybrooks/instruct-pix2pix)
- [STYTR2](https://github.com/diyiiyiii/StyTR-2)

## Citation

```
noon
```

