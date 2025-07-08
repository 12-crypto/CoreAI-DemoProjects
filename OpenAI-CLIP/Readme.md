# CLIP (Contrastive Language-Image Pre-training) Model Implementation


- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
  - [1.6. Resource Requirements](#16-resource-requirements)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. Expected Packages and Requirements](#31-expected-packages-and-requirements)
  - [3.2. How to Use](#32-how-to-use)
    - [3.2.1. Create and Activate the Virtual Environment](#321-issue-1-environment-setup-failures)
    - [3.2.2. Install Required Libraries](#322-install-required-libraries)
    - [3.2.3. Important Note](#323-important-note)
 

# 1. Project Details

## 1.1. Original Author
- Moein Shariatnia
- [Github Profile](https://github.com/moein-shariatnia)
  
## 1.2. Original License
- [MIT License](https://choosealicense.com/licenses/mit/)
- This project is licensed under the MIT License - see the LICENSE.md file for details.

## 1.3. Original Github Link
- [OpenAI CLIP Implementation](https://github.com/moein-shariatnia/OpenAI-CLIP/blob/master/OpenAI%20CLIP%20Simple%20Implementation.ipynb)

## 1.4. Description of Project
This project implements **CLIP**, a model designed to understand the relationship between images and their corresponding textual descriptions by training on full sentences rather than single class labels. CLIP enables the retrieval of relevant images based on textual queries and performs classification tasks with high accuracy, often outperforming state-of-the-art models trained specifically for classification on datasets like ImageNet.

## 1.5. Required Datasets
- [Flickr 8K](https://www.kaggle.com/datasets/adityajn105/flickr8k)
- You can download the dataset by following the website guidelines.
  
### How to Download Dataset
To access and set up the dataset, follow these steps:
- Create a `data` folder in your project directory if it doesn't already exist.
- Place the image files in a subdirectory named `Images` within the `data` folder.
- Ensure to convert `captions.txt` to `captions.csv` file, which maps image filenames to their corresponding captions, is placed in the `data` folder.
- Run `data.py` inside `data` folder to ensure each caption has a unique ID.

## 1.6. Resource Requirements
- GPU (NVIDIA GPU recommended for optimal performance)

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

Run one of the following commands:

```bash
## podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=id -u -e WANTED_GID=id -g -e CoreAI_VERBOSE="yes" -v pwd:/iti -p 8888:8888 docker.io/infotrend/coreai:latest /run_jupyter.sh

## docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=id -u -e WANTED_GID=id -g -e CoreAI_VERBOSE="yes" -v pwd:/iti -p 8888:8888 infotrend/coreai:latest /run_jupyter.sh
```

Follow the instructions in the notebook `OpenAI-CLIP.ipynb`.

## 2.1. Stop CoreAI
You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. Expected Packages and Requirements

**Python Packages**:
- transformers
- albumentations
- timm


## 3.2. How To Use

1. **Setup Environment**:
   - Clone the repository or download the specific project files.
   - Ensure Python 3.x is installed.

2. **Install Required Packages**:

   - To enhance the functionality of the CoreAI environment, you may need to install some libraries not pre-installed but required for this notebook. Follow these steps to install the necessary libraries from the `requirements.txt` file:

## 3.2.1. Create and Activate the Virtual Environment:**
   
   Open your terminal or command prompt within the jupyter notebook. `File -> New -> Terminal`
   
   Navigate to the project directory where you want to set up the environment.
   
   Execute the following commands to create and activate the virtual environment:
   
   ```
   export PROJECT_NAME="OpenAI-CLIP"
   export PIP_CACHE_DIR=`pwd`/.cache/pip
   mkdir -p $PIP_CACHE_DIR
   python -m venv --system-site-packages myvenv
   source myvenv/bin/activate
   pip install ipykernel
   python -m ipykernel install --user --name=${PROJECT_NAME}-myvenv --display-name="Python (${PROJECT_NAME}-myvenv)"
   echo ""; echo "Before continuing load the created Python kernel: Python (${PROJECT_NAME}-myvenv)"
   ```
## 3.2.2. Install Required Libraries
   
   Before running the following command in jupyter notebook, make sure you are in the directory where the Jupyter Notebook and virtual environment is located. This ensures the ./ path is always current. You can use the cd command to change to your project directory and pwd to verify your current directory.

    
   ```
   import os
   os.environ["ANONYMIZED_TELEMETRY"] = 'False'

   def set_env_with_cache_dir(env_var_name: str, subdir: str):
       base_cache = os.path.join(os.getcwd(), ".cache")
       full_path = os.path.join(base_cache, subdir)
       os.environ[env_var_name] = full_path
       os.makedirs(full_path, exist_ok=True)

   set_env_with_cache_dir("PIP_CACHE_DIR", "pip")
   set_env_with_cache_dir("HF_HOME", "huggingface")
   ```

   
   ```
   !. ./myvenv/bin/activate; pip install -r requirements.txt
   ```
### 3.2.3. Important Note

It is crucial to load the new "OpenAI-CLIP-myvenv" kernel for the notebook to work correctly. If the new ```OpenAI-CLIP-myvenv``` kernel is not loaded, the required libraries and environment settings will not be applied, and the notebook will not function as expected.

3. **Run the Notebook**:
    Open the ```OpenAI-CLIP.ipynb``` notebook in a Jupyter environment.
    Execute the notebook cells sequentially to perform data loading, preprocessing, model training, and evaluation.

4. **Predictive Capability**: The trained CLIP model can retrieve relevant images based on textual queries (e.g., "a boy jumping with skateboard") and perform classification tasks by learning joint representations of images and text. This dual capability is valuable for applications in image search and automated content tagging.
[Back to Top](#OpenAI-CLIP)

