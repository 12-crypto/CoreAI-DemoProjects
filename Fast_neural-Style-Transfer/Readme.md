<h1>Style Transform Project</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
    - [1.5.1. How to Download Models](#151-how-to-download-models)
  - [1.6. Supported Media Formats](#16-supported-media-formats)
  - [1.7. Expected Packages and Resource Requirements](#17-expected-packages-and-resource-requirements)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. How To Use](#31-how-to-use)
  - [3.2. Troubleshooting](#32-troubleshooting)
  - [3.3. Changes Made to the Original Notebook](#33-changes-made-to-the-original-notebook)


# 1. Project Details

## 1.1. Original Author

**GitHub Profile**: [Erik Linder-Norén](https://github.com/eriklindernoren)

## 1.2. Original License

MIT License  
This project is licensed under the MIT License - see the original repo for details.

## 1.3. Original GitHub Link

[Fast Neural Style Transfer](https://github.com/eriklindernoren/Fast-Neural-Style-Transfer)

## 1.4. Description of Project

This project is designed to perform style transfer on images and videos, applying artistic styles to media via convolutional neural networks. It leverages models trained on various artistic images to transform the aesthetic of input images and videos, allowing users to create stylized media in real-time.

## 1.5. Required Datasets

**Pre-trained Style Transfer Models**:

The pre-trained models can be downloaded from the following Google Drive folder. Please download all the files at once to ensure you have the complete set of necessary models for this project.

### 1.5.1. How to Download Models
To access and download all the models in one go, please follow these simplified steps:

1. Visit the [Google Drive folder with pre-trained models](https://drive.google.com/drive/folders/1aRD6zakhcDImN2Y54qAT6f4801iLcCLB?usp=sharing).
2. Click on the "Download all" button to download the models as a single compressed (zip) file.
3. Unzip the downloaded file into the `models` directory within your project folder.


## 1.6. Supported Media Formats

**Images Supported**:
- JPEG (.jpg, .jpeg)

**Videos Supported**:
- AVI (.avi)
- GIF (.gif)

## 1.7. Expected Packages and Resource Requirements

**Python Packages**:
- torch
- torchvision
- numpy
- PIL
- tqdm
- ipywidgets
- skvideo

**Resource Requirements**:
- CPU or GPU (GPU recommended for faster processing)

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `fast-neural-style-transfer.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. How To Use

1. **Setup Environment**:
   - Clone the repository or download the specific project files.
   - Ensure Python 3.x is installed.

2. **Install Required Packages**:

   - To enhance the functionality of the CoreAI environment, you may need to install some libraries not pre-installed but required for this notebook. Follow these steps to install the necessary libraries from the `requirements.txt` file:

   **2.1 Create and Activate the Virtual Environment:**
   
   Open your terminal or command prompt within the jupyter notebook. `File -> New -> Terminal`
   
   Navigate to the project directory where you want to set up the environment.
   
   Execute the following commands to create and activate the virtual environment:
   
   ```
   python3 -m venv --system-site-packages myvenv #myvenv is name of virtual environment you can change it
   bash
   source myvenv/bin/activate
   pip3 install ipykernel
   python -m ipykernel install --user --name=myvenv --display-name="Python (myvenv)"
   ```
   **2.2 Install Required Libraries:**

- Before running the following commands, load the "Python (myvenv)" kernel to limit the chances of altering the underlying container. Ensure you are in the directory where the Jupyter Notebook and the `myvenv` directory are located. Use `cd` to change to your project directory and `pwd` to verify your current directory.
   
   ```
   !. ./myvenv/bin/activate; pip install -r requirements.txt
   ```

3. **Run the Notebook**:
- Open the `fast-neural-style-transfer.ipynb` notebook in a Jupyter environment.
- Execute the notebook cells sequentially to upload media, perform style transfer, and view the results.

4. **Media Processing**:
- Upload images or videos through the interactive widgets.
- Select the desired pre-trained style transfer model.
- Execute style transfer and view the stylized outputs directly in the notebook.

## 3.2. Troubleshooting

- Ensure that the model and media files are placed in the correct directories (`models` and `input/images` or `input/videos` respectively).
- Check that all dependencies are installed correctly within the virtual environment.
- Make sure CUDA is available for GPU usage if a GPU is being utilized for processing.

## 3.3. Changes Made to the Original Notebook

- Integrated image and video style transfer capabilities into a single Jupyter notebook.
- Enhanced user interaction through the use of IPython widgets for file upload and model selection.
- Optimized image processing workflows to support real-time media transformation.

