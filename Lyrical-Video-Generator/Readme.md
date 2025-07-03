# Lyrical Video Generator

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
  - [1.6. Resource Requirements](#16-resource-requirements)
  - [1.7. Capabilities to Run on CPU and/or GPU](#17-capabilities-to-run-on-cpu-andor-gpu)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. How To Use](#31-how-to-use)
  - [3.2. Troubleshooting Guides](#32-troubleshooting-guides)
    - [3.2.1. Issue 1: Environment Setup Failures](#321-issue-1-environment-setup-failures)
    - [3.2.2. Issue 2: Transcription Errors](#322-issue-2-transcription-errors)
    - [3.2.3. Issue 3: GPU Utilization Not Detected](#323-issue-3-gpu-utilization-not-detected)
    - [3.2.4. Algorithm Insights](#324-algorithm-insights)

# 1. Project Details

## 1.1. Original Author
- Piyush Sharma
- [Kaggle Profile](https://www.kaggle.com/piyushsharma5654)
  
## 1.2. Original License
- [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)

## 1.3. Original Link
- [Lyrical Video Generation](https://www.kaggle.com/code/piyushsharma5654/lyrical-video-generation)

## 1.4. Description of Project
This project automates the creation of continuous lyric videos from audio files using advanced AI models and multimedia processing tools. The Jupyter Notebook `lyrical-video-generation.ipynb` provides an interactive environment where users can input audio files, process them through transcription and image generation, and produce a fully synchronized lyric video with guaranteed audio-visual coverage. Key features include audio transcription, dynamic visual segmentation, AI-generated visuals, and continuous video assembly.

## 1.5. Required Datasets
- No specific datasets are required beyond the input audio files provided by the user.
- Pre-trained models used include the Whisper model for transcription and Stable Diffusion (runwayml/stable-diffusion-v1-5) for image generation.

## 1.6. Resource Requirements
- CPU or GPU (NVIDIA GPU recommended for optimal performance)
- Recommended GPU: NVIDIA GPU with sufficient memory to handle AI model processing (e.g., Stable Diffusion)
- Approximate processing time varies based on audio length and system capabilities; expect longer times for image generation and video rendering on CPU.

## 1.7. Capabilities to Run on CPU and/or GPU
This project is configured to automatically detect and utilize a GPU if available, ensuring faster processing for transcription and image generation tasks. If a GPU is not available, the project will fall back to using the CPU, though processing times may be significantly longer.

# 2. CoreAI Setup

From the folder where this `README.md` is, run one of the following commands:

```bash
## podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=id -u -e WANTED_GID=id -g -e CoreAI_VERBOSE="yes" -v pwd:/iti -p 8888:8888 docker.io/infotrend/coreai:latest /run_jupyter.sh

## docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=id -u -e WANTED_GID=id -g -e CoreAI_VERBOSE="yes" -v pwd:/iti -p 8888:8888 infotrend/coreai:latest /run_jupyter.sh
```

Follow the instructions in the notebook `lyrical-video-generation.ipynb`.

## 2.1. Stop CoreAI
You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. How To Use
To get started with this project, follow these steps:

1. **Setup Environment:**
   - Clone or download the project files, including the `lyrical-video-generation.ipynb` notebook.
   - Install the required dependencies by following the setup instructions in the notebook, which include creating a virtual environment and installing packages such as Whisper and Stable Diffusion.


2. **Run the Notebook:**
   - Open the `lyrical-video-generation.ipynb` notebook using Jupyter Notebook or JupyterLab.
   - Execute the notebook cells sequentially. The environment will automatically detect and utilize a GPU if available; otherwise, it will use the CPU.

3. **Audio Processing and Video Generation:**
   - Specify or upload an audio file for processing. The notebook will transcribe the audio, generate dynamic visuals for each segment, and assemble a continuous lyric video.
   - The final video will be saved to a designated output directory as specified in the notebook.

4. **Review Output:**
   - View the generated lyric video within the notebook or access it from the output directory for sharing or further editing.

## 3.2. Troubleshooting Guides
This section addresses common issues you might encounter when running the `lyrical-video-generation.ipynb` notebook:

### 3.2.1. Issue 1: Environment Setup Failures
**Symptom:** Failure to launch the Jupyter Notebook or install required packages in the environment.

**Solution:** Ensure the virtual environment is set up correctly according to the notebook instructions. Verify that all commands for creating and activating the environment are executed properly. If using the Infotrend container, ensure it is running and properly configured. Restart the container or environment setup if necessary.

### 3.2.2. Issue 2: Transcription Errors
**Symptom:** Audio transcription fails or produces inaccurate results.

**Solution:** Check that the Whisper model is correctly installed and loaded. Ensure the audio file is of good quality and in a supported format. Review the transcription settings in the notebook to confirm that forced English language detection and other parameters are set appropriately. If errors persist, consider adjusting the segment length for processing.

### 3.2.3. Issue 3: GPU Utilization Not Detected
**Symptom:** The system falls back to CPU even though a GPU is available.

**Solution:** Verify the GPU installation and ensure the latest driver updates are installed. Ensure PyTorch is configured to recognize the GPU. Use the command `torch.cuda.is_available()` to check GPU availability from within the notebook. If issues persist, check for conflicts in the environment setup or container configuration.

### 3.2.4. Algorithm Insights
The Lyrical Video Generator leverages AI models like Whisper for audio transcription and Stable Diffusion for generating dynamic visuals. The transcription process ensures full audio coverage by processing in fixed-duration chunks, while visual segmentation guarantees continuous playback without gaps. Image generation uses varied prompts and styles to maintain visual diversity, enhancing the appeal of the final video. For advanced customization, users can modify prompts, styles, or segment durations within the notebook to suit specific needs.

[Back to Top](#lyrical-video-generator)

