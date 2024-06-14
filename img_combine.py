import cv2
import numpy as np
import os
from pathlib import Path

real_path = Path(
    "/home/cwt1/scratch/BasicLFSR/RR-HLFSR_NTIRE2023_LFSR/log/SR_5x5_4x/ALL"
)
# models_name = ['DistgSSR_official', 'EPIT_official', 'LFT_official']
models_name = ["DistgEPIT_d_w", "EPIT_d_w", "RR_HLFSR"]
filename_path = '/home/cwt1/scratch/BasicLFSR/RR-HLFSR_NTIRE2023_LFSR/log/SR_5x5_4x/ALL/DistgEPIT_d_w/results/TEST/NTIRE_Test_Synth'
filenames = os.listdir(filename_path)

for filename in filenames:
    print(filename)
    img_filenames_path = os.path.join(filename_path, filename)
    img_filenames = os.listdir(img_filenames_path)
    if not os.path.isdir(os.path.join(real_path, "combined_Test_Synth")):
        os.mkdir(os.path.join(real_path, "combined_Test_Synth"))
    combined_path = os.path.join(real_path, "combined_Test_Synth", filename)
    if not os.path.isdir(combined_path):
        os.mkdir(combined_path)
    for img_filename in img_filenames:
        img_list = []
        for model_name in models_name:
            img_path = os.path.join(
                real_path,
                model_name,
                "results/TEST/NTIRE_Test_Synth",
                filename,
                img_filename,
            )
            img = cv2.imread(img_path)
            img_list.append(img)
            # print(img_path)
        img_sum = np.zeros_like(img, dtype=float)
        for img in img_list:
            img_sum += img
        img_avg = img_sum / len(img_list)
        combined_img_path = os.path.join(combined_path, img_filename)
        cv2.imwrite(combined_img_path, img_avg   )
    # exit(0)
