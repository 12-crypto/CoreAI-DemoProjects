<h1>Crime Trends</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Description of Project](#11-description-of-project)
- [2. Prerequisites](#2-prerequisites)
- [3. Start CoreAI](#3-start-coreai)
- [4. Access CoreAI](#4-access-coreai)
- [5. Required Libraries](#5-required-libraries)
- [6. Stop CoreAI](#6-stop-coreai)
- [7. Cleanup](#7-cleanup)
  
# 1. Project Details

### 1.1. Description of Project
This project demonstrates comprehensive crime pattern analysis and predictive modeling using machine learning techniques applied to Los Angeles Police Department crime data from 2020 to present. Leveraging over one million crime incidents, the analysis performs automated crime type classification and geographic trend analysis to support law enforcement decision-making and public safety initiatives.

- Multi-algorithm classification with Decision Trees, Random Forest, and Logistic Regression
- Advanced data preprocessing with label encoding and feature engineering
- Interactive geographic visualization using Folium heat maps
- Comprehensive exploratory data analysis with temporal and demographic insights
- Real-time crime type prediction based on incident characteristics and location data


# 2. Prerequisites 
- [Crime Trends Dataset](https://www.kaggle.com/datasets/sonawanelalitsunil/crime-trends-2020present/data)
- CPU or GPU

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

Load the notebook `Crime-Trends.ipynb` and follow the instructions contained in it.
   
# 5. Required libraries

- kagglehub
- seaborn
- folium

All the required libraries are present in the `requirements.txt`

# 6. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 7. Cleanup

Because we used the `--rm` flag, the container will be automatically removed when you stop it.