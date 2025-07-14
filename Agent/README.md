<h1>Project: AI Agent with Web Search and LiteLLM</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)


# 1. Project Description

This notebook demonstrates a comprehensive AI agent that provides users with complete control over model selection and processing approaches. The agent integrates multiple AI models including Perplexity's Sonar models for web-enhanced responses and various large language models (LLMs) for general processing tasks. The system offers four distinct processing modes: Sonar-only for web research, LLM-only for traditional processing, hybrid combining both approaches, and auto-selection based on query characteristics.

- Multi-Model Support: Seamless access to both Sonar (web-enabled) and regular LLM models through a unified interface

- Interactive Command System: Intuitive command-based interface for easy model switching and preference management

- Flexible Processing Approaches: Four distinct modes to match different query types and user requirements

# 2. Prerequisites

- CPU 
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

The Jupyter Lab password is `iti`.

Load the notebook `ExtractionDocling.ipynb` and follow the instructions contained in it.

# 5. Required Libraries

- litellm
- requests
- python-dotenv


All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.
