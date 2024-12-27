# BigEPIT_NTIRE2024_LFSR


<!-- ## Results
We share the pre-trained models and the SR LF images generated by our RR-HLFSR model for 4x LF spatial SR, which are avaliable at https://drive.google.com/drive/u/2/folders/160KS4l5jWEehJ0KtgOg0T6pdlhgTyWbg -->

<!-- ## Code


### Dependencies
* Python 3.8
* Pyorch 1.13.1 + torchvision 0.14.1


This code is built up on the [Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR). Please go to orginal code for more guideline information. 

### Dataset
We use the processed data [Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR), including EPFL, HCInew, HCIold, INRIA and STFgantry datasets for training and testing. Please download the dataset in the official repository of [Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR).

### Prepare Training and Test Data
* To generate the training data, please first download the five datasets and run:
  ```python
  Generate_Data_for_Training_aug.py
* To generate the test data, run:
  ```python
  Generate_Data_for_inference.py
### Train
* Run:
  ```python
  python train.py  --model_name EPIT_d_w --angRes 5 --scale_factor 4 --lr 2e-4 --epoch 31  --crop_test_method 2  
### Test
* Run:
  ```python
  # BigEPIT_NTIRE2024_LFSR -->


## Code


### Dependencies
* Python 3.8
* Pyorch 1.13.1 + torchvision 0.14.1


This code is built up on the [Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR). Please go to orginal code for more guideline information. 

### Dataset
We use the processed data [Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR), including EPFL, HCInew, HCIold, INRIA and STFgantry datasets for training and testing. Please download the dataset in the official repository of [Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR).

### Prepare Training and Test Data
* To generate the training data, please first download the five datasets and run:
  ```python
  Generate_Data_for_Training_aug.py
* To generate the test data, run:
  ```python
  Generate_Data_for_inference.py
### Train
* Run:
  ```python
  python train.py  --model_name EPIT_d_w --angRes 5 --scale_factor 4 --lr 2e-4 --epoch 101  --crop_test_method 2  
### Test
* Run:
  ```python
  python test.py --model_name EPIT_d_w --angRes 5 --upscale_factor 4  --crop_test_method 1 --self_ensemble  --use_pre_ckpt True --path_pre_pth [pre-trained dir]

<!-- [Important note]: 

1) We use the geometric self-ensemble method to improve the performance in NTIRE2024 LFSR challenges further

2) We may need to turn off the calculated PSNR/SSIM by setting "--test_NTIRE2023_LFSR 1" since there is no ground true HR images during the testing phase.
  

## Acknowledgement
Our work and implementations are inspired and based on the following projects: <br> 
[Basic-LFSR](https://github.com/ZhengyuLiang24/BasicLFSR)<br> 
[EPIT](https://github.com/ZhengyuLiang24/EPIT)<br> 
[DistgEPIT](https://github.com/OpenMeow/NTIRE23_LFSR_DistgEPIT)<br> 
[RR-HLFSR](https://github.com/duongvinh/RR-HLFSR_NTIRE2023_LFSR/)<br>
We sincerely thank the authors for sharing their code and amazing research work!

## Contact
if you have any questions, please contact me through email at chaowentao@mail.bnu.edu.cn -->

# Citation
```
@inproceedings{chao2024bigepit,
  title={BigEPIT: Scaling EPIT for Light Field Image Super-Resolution},
  author={Chao, Wentao and Kan, Yiming and Wang, Xuechun and Duan, Fuqing and Wang, Guanghui},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshop},
  pages={6187--6197},
  year={2024}
}
``` 


