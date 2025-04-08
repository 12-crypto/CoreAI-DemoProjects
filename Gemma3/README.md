<h1>Project: Gemma3</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Stop CoreAI](#5-stop-coreai)
- [6. Cleanup](#6-cleanup)


# 1. Project Description

> Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarization, and reasoning. Their relatively small size makes it possible to deploy them in environments with limited resources such as laptops, desktops or your own cloud infrastructure, democratizing access to state of the art AI models and helping foster innovation for everyone.

https://huggingface.co/google/gemma-3-4b-it

# 2. Prerequisites

- A GPU with at least 16GB of VRAM
- Docker or Podman
- A Hugging Face token to download the required weights at runtime

# 3. Start CoreAI

This notebook will allow you to capture images from your webcam and generate responses from the Gemma3 model, as such the `-v /dev/video0:/dev/video0` flag is used. Remove it if you do not have a webcam or if you do not want to use it.

From the folder where this `README.md` is, run:

```bash
# set your HF token
export HF_TOKEN=enter_your_HF_TOKEN_here

# Run one of the following commands:

## podman command
# with webcam
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v /dev/video0:/dev/video0 -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# without webcam
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh


## docker command
# with webcam
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v /dev/video0:/dev/video0 -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh

# without webcam
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

A `start_CoreAI.sh` script is also provided for convenience that will start the container using `podman`.

# 4. Access CoreAI

After the container is started, you can access CoreAI at `http://localhost:8888`.

The Jupyer Lab password is `iti`.

Load the notebook `Gemma3.ipynb` and follow the instructions contained in it.

# 5. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 6. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.
