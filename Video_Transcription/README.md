<h1>Video Transcription</h1>

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
In this project, we will walk through the process of transcribing a video and generating subtitles using OpenAI's Whisper and WhisperX — powerful tools for automatic speech recognition (ASR) and speaker diarization.

### 1.2. Original Project Details

- Author: [Armaghan](https://www.kaggle.com/sacrum)
- License: [Apache 2.0 open source license](https://www.apache.org/licenses/LICENSE-2.0)
- Notebook: [Whisper AI & Pyannote - Transcribing](https://www.kaggle.com/code/sacrum/whisper-ai-pyannote-transcribing/notebook)

# 2. Prerequisites
- HF_TOKEN
- Requesting WhisperX model access through Hugging Face 
- Video file
- CPU or GPU (NVIDIA GPU with 16GB VRAM is recommended for optimal performance)

Note: This project is configured to automatically detect and utilize a GPU if available, ensuring faster processing times. If a GPU is not available, the project will gracefully fallback to using the CPU.

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

Load the notebook `Video_Transcription.ipynb` and follow the instructions contained in it.
   
# 5. Required libraries

- moviepy
- openai-whisper
- whisperx

All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.