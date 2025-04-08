<h1>Project: Flux 1 Schnell</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Stop CoreAI](#5-stop-coreai)
- [6. Cleanup](#6-cleanup)


# 1. Project Description

> FLUX.1 [schnell] is a 12 billion parameter rectified flow transformer capable of generating images from text descriptions.

https://huggingface.co/black-forest-labs/FLUX.1-schnell

# 2. Prerequisites

- A GPU with at least 24GB of VRAM
- Docker or Podman
- A Hugging Face token to download the required weights at runtime

# 3. Start CoreAI

From the folder where this `README.md` is, run:

```bash
# set your HF token
export HF_TOKEN=enter_your_HF_TOKEN_here

# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

# 4. Access CoreAI

After the container is started, you can access CoreAI at `http://localhost:8888`.

The Jupyer Lab password is `iti`.

Load the notebook `Flux1Schnell.ipynb` and follow the instructions contained in it.

# 5. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 6. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.

