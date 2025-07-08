<h1>Project: Document Extraction with Docling</h1>

- [1. Project Description](#1-project-description)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)


# 1. Project Description

This notebook demonstrates an end-to-end pipeline for extracting structured information from PDF and image documents using the **Docling** framework. It automatically detects and extracts:

- Tables (as structured CSV files)
- Figures (as cropped PNGs)
- Document text (as clean Markdown)

# 2. Prerequisites

- CPU (It is recommended to use a GPU for significantly faster processing.)
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

- docling[vlm]
- pdf2image
- PyMuPDF


All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.
