<h1>Project: Realistic Face Generator</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)


# 1. Project Description

In this project, we develop a Realistic Face Generator using a Generative Adversarial Network (GAN) trained on the CelebA dataset. The model learns to generate a realistic human faces by capturing complex patterns and features from the dataset through adversarial training.

For more details on Celeba dataset visit: https://www.kaggle.com/datasets/jessicali9530/celeba-dataset/data

# 2. Prerequisites

- GPU 
- Docker or Podman

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

Load the notebook `Realistic_Face_Generator.ipynb` and follow the instructions contained in it.

# 5. Required libraries

This notebook does not require any additional libraries to run. The libraries available in the container are sufficient to execute it.

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.

