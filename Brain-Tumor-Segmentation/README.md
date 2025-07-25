<h1>Explainable AI</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Description of Project](#11-description-of-project)
  - [1.2. Original Project Details](#12-original-project-details)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)
  
# 1. Project Details

### 1.1. Description of Project
This project demonstrates deep learning-based brain tumor segmentation using MRI images from the LGG MRI Segmentation dataset. Using a U-Net architecture with EfficientNet-B7 encoder, we perform automated detection and segmentation of brain tumors to assist in medical diagnosis.

### 1.2. Original Project Details

- Author: [Abdallah Wagih Ibrahim](https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation)
- License: [Apache 2.0 open source license](https://www.apache.org/licenses/LICENSE-2.0)
- Notebook: [Brain Tumor Segmentation UNet + EfficientNetB7](https://www.kaggle.com/code/abdallahwagih/brain-tumor-segmentation-unet-efficientnetb7/notebook)

# 2. Prerequisites 
- [LGG Segmentation Dataset](https://www.kaggle.com/datasets/mateuszbuda/lgg-mri-segmentation)
- GPU (NVIDIA GPU with 16GB VRAM is recommended for optimal performance)


# 3. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

# 4. Access CoreAI

After the container is started, you can access CoreAI at `http://localhost:8888`.

The Jupyer Lab password is `iti`.

Load the notebook `Explainable-AI.ipynb` and follow the instructions contained in it.
   
# 5. Required libraries

- kagglehub
- seaborn

All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.