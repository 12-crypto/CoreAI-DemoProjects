<h1>Project: Fine Tuning LLama using QLoRA</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)


# 1. Project Description

In this notebook, we fine-tune the **LLaMA 3.1 8B Instruct** model using **QLoRA** (Quantized Low-Rank Adaptation) on the **CaseHOLD** dataset from the `lex_glue` benchmark.

### Task Overview

**CaseHOLD** is a legal reasoning task that requires the model to complete a legal case context by selecting the correct legal holding from a set of five multiple-choice options.

For more details on **CaseHOLD** visit: https://github.com/coastalcph/lex-glue

### What This Notebook Demonstrates

- **Efficient fine-tuning** using **4-bit NF4 quantization**
- **Parameter-efficient adaptation** with **LoRA**
- **Full training and evaluation pipeline**
- **Performance analysis and error breakdown**
- **Inference on the test set** with answer extraction and accuracy metrics

# 2. Prerequisites

- GPU (NVIDIA GPU with 20GB VRAM is recommended for optimal performance)
- Docker or Podman
- HF_TOKEN
- CaseHOLD Dataset from [LexGLUE](https://github.com/coastalcph/lex-glue)

# 3. Start CoreAI

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh
```

# 4. Access CoreAI

After the container is started, you can access CoreAI at `http://localhost:8888`.

The Jupyer Lab password is `iti`.

Load the notebook `Fine_Tuning_LLama_QLoRA.ipynb` and follow the instructions contained in it.

# 5. Required libraries

- transformers
- datasets
- accelerate
- peft
- bitsandbytes
- scipy

All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.

