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
The primary goal of this Project is to develop a machine learning model capable of recommending the top three most suitable fertilizers based on a given set of environmental conditions and soil characteristics. By leveraging data-driven insights, this system aims to support precision agriculture, helping farmers make informed decisions that enhance crop productivity while promoting sustainable farming practices.

### 1.2. Original Project Details

- Author: [Sulani Ishara](https://www.kaggle.com/sulaniishara)
- License: [Apache 2.0 open source license](https://www.apache.org/licenses/LICENSE-2.0)
- Notebook: [🌾 Smart Fertilizer Ranker 🔢 MAP@3 | XGBoost 📊](https://www.kaggle.com/code/sulaniishara/smart-fertilizer-ranker-map-3-xgboost)

# 2. Prerequisites
- CPU

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

Load the notebook `Fertilizer_Ranker.ipynb` and follow the instructions contained in it.
   
# 5. Required libraries

- seaborn
- xgboost

All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.