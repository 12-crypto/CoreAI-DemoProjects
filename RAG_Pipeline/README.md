<h1>Project: RAG Pipeline</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)


# 1. Project Description

In this project we are building a Retrieval-Augmented Generation (RAG) Pipeline using Ragbits, Docling, Chromadb and Litellm.

You can know more about each tools in the links below:

Ragbits: https://ragbits.deepsense.ai/
Docling: https://docling-project.github.io/docling/
Chromadb: https://www.trychroma.com/
Litellm: https://www.litellm.ai/

# 2. Prerequisites

- CPU (It is recommended to use a GPU for significantly faster processing and reduced wait times.)
- Docker or Podman
- An API Provider with the url to access the API and the API key

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

Load the notebook `RAG_Pipeline.ipynb` and follow the instructions contained in it.

# 5. Required libraries

- ragbits
- chromadb

All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.

