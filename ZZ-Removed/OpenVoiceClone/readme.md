# 1. OpenVoice: Advanced Voice Cloning and Synthesis

In `ZZ-Removed` due missing library. Will investigate further.

- [1. OpenVoice: Advanced Voice Cloning and Synthesis](#1-openvoice-advanced-voice-cloning-and-synthesis)
- [2. Project Overview](#2-project-overview)
  - [2.1. Original GitHub Link](#21-original-github-link)
  - [2.2. Voice Translation Widgets](#22-voice-translation-widgets)
    - [2.2.1. Features](#221-features)
    - [2.2.2. Usage](#222-usage)
- [3. CoreAI Setup](#3-coreai-setup)
  - [3.1. Stop CoreAI](#31-stop-coreai)
- [4. Detailed Setup](#4-detailed-setup)
  - [4.1. System Requirements](#41-system-requirements)
  - [4.2. Setup and Installation](#42-setup-and-installation)
  - [4.3. How To Use](#43-how-to-use)
  - [4.4. Model Preparation](#44-model-preparation)
  - [4.5. Run the Notebook:](#45-run-the-notebook)
  - [4.6. Troubleshooting](#46-troubleshooting)
    - [4.6.1. Common Issues and Fixes](#461-common-issues-and-fixes)


# 2. Project Overview

OpenVoice is a cutting-edge project dedicated to the development of voice cloning and speech synthesis technologies. This repository hosts the tools and models necessary for implementing state-of-the-art voice cloning capabilities, enabling users to create lifelike synthetic voices from audio samples.

## 2.1. Original GitHub Link

[OpenVoice Project Repository](https://github.com/myshell-ai/OpenVoice)


## 2.2. Voice Translation Widgets

This application provides a user-friendly interface for voice translation. Below are the features available:

### 2.2.1. Features

1. **Voice Upload**: Users can upload their voice recordings in MP3 format.
   
2. **Language Selection**: A dropdown menu allows users to select the language of the text to which the uploaded voice will be translated.
   
3. **Text Input Box**: Users can input or edit the text that will be translated into the selected language using the uploaded voice.

### 2.2.2. Usage

- **Uploading Voice**: Click on the 'Upload' button and select an MP3 file from your device.
- **Selecting Language**: Use the dropdown to choose the target language for translation.
- **Entering Text**: Type into the text box the text you want to use for translation.

This application is designed to be intuitive and easy to use, ensuring that users can quickly translate voices with minimal effort.

# 3. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `OpenVoiceClone.ipynb`.

## 3.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 4. Detailed Setup

## 4.1. System Requirements

- **Python 3.x**: Ensure Python 3.x is installed.
- **Operating System**: Linux or macOS (for complete compatibility with all tools and scripts).

## 4.2. Setup and Installation

## 4.3. How To Use

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
   bash
   python3 -m venv --system-site-packages myvenv #myvenv is name of virtual environment you can change it
   source myvenv/bin/activate
   pip3 install ipykernel
   python -m ipykernel install --user --name=myvenv --display-name="Python (myvenv)"
   ```

 **2.2 Install Required Libraries**
   
 Before running the following command in the Jupyter notebook, make sure you are in the directory where the Jupyter Notebook and virtual environment is located. Load the newly created "Python (myvenv)" kernel. This ensures the `./` path is always current. You can use the `cd` command to change to your project directory and `pwd` to verify your current directory.

   ```sh
   !. ./myvenv/bin/activate; pip install -r requirements.txt
   ```

## 4.4. Model Preparation
Download and prepare the model data:

1. Create a directory for model checkpoints:
   ```
   mkdir checkpoints_v2
    ```
2. Download the model checkpoint data:
   ```
   wget https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip
    unzip checkpoints_v2_0417.zip -d checkpoints_v2
    ```
   
## 4.5. Run the Notebook:
- Open the `demo.ipynb` notebook in a Jupyter environment.
-  Follow the instructions within the notebook, executing the code cells in sequence. Each cell includes comments explaining the purpose of the code, which will guide you through the demo process.
- Make sure to read any embedded instructions or comments carefully to maximize your understanding and troubleshooting any issues that may arise.

## 4.6. Troubleshooting
### 4.6.1. Common Issues and Fixes
CUDA Library Error: If you encounter an error related to libcublas.so.11, create a symbolic link to the newer version:
    ```
    ln -s /usr/local/cuda/lib64/libcublas.so.12 /usr/local/cuda/lib64/libcublas.so.11
    ```
Install portaudio: Portaudio is required for handling audio input and output in many applications. If you experience issues related to audio operations, ensure that `portaudio19-dev` is installed:
    ```
    ! apt install -y portaudio19-dev
    ```
This ensures that all dependencies for audio processing are properly configured.