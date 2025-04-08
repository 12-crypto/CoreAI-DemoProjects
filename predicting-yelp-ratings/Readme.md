<h1>Yelp Ratings Predictor</h1>

- [1. Project Details](#1-project-details)
    - [1.0.1. Original Author](#101-original-author)
    - [1.0.2. Original License](#102-original-license)
    - [1.0.3. Original GitHub Link](#103-original-github-link)
    - [1.0.4. Code Adaptation](#104-code-adaptation)
    - [1.0.5. Description of Project](#105-description-of-project)
    - [1.0.6. Required Datasets](#106-required-datasets)
    - [1.0.7. How to Download Dataset](#107-how-to-download-dataset)
    - [1.0.8. Expected Packages and Resource Requirements](#108-expected-packages-and-resource-requirements)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
    - [3.0.1. How To Use](#301-how-to-use)
    - [3.0.2. Additional Library Installation](#302-additional-library-installation)
    - [3.0.3. Run the Notebook:](#303-run-the-notebook)
    - [3.0.4. Model Training and Evaluation:](#304-model-training-and-evaluation)
    - [3.0.5. Model Usage:](#305-model-usage)
    - [3.0.6. Troubleshooting](#306-troubleshooting)


# 1. Project Details

### 1.0.1. Original Author
**GitHub Profile**: [Aymen](https://github.com/aymen)

### 1.0.2. Original License
**MIT License**  
This project is licensed under the MIT License - see the LICENSE.md file for details.

### 1.0.3. Original GitHub Link
[Yelp Ratings Predictor Notebook](https://github.com/aymen/yelp-ratings-predictor)

### 1.0.4. Code Adaptation
This project's code was adapted from [Predicting Yelp Ratings](https://github.com/concision/predicting-yelp-ratings), originally developed by concision.

### 1.0.5. Description of Project
This project employs natural language processing (NLP) and machine learning in TensorFlow to predict Yelp business ratings from the content of user reviews. By analyzing text data, the model aims to uncover correlations between review sentiments and star ratings, aiding in more accurate business evaluations.

### 1.0.6. Required Datasets
**Yelp Open Dataset** - Available on Yelp's dataset page

### 1.0.7. How to Download Dataset
To access and download the dataset, please follow these steps:
1. Visit the [Yelp Dataset](https://www.yelp.com/dataset) page.
2. Click on the "Download" button to download the JSON files.
3. Unzip the files into the `data` folder within the project directory, ensuring they are ready for use in the Jupyter notebook.

### 1.0.8. Expected Packages and Resource Requirements
**Python Packages**:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- TensorFlow

**Resource Requirements**:
- CPU/GPU

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `Yelp-ratings-predictor.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

### 3.0.1. How To Use
**Setup Environment**:
- Clone the repository or download the specific project files.

**Install Required Packages**:
1. Create and Activate the Virtual Environment:
   - Open your terminal or command prompt within the Jupyter notebook.
   - Navigate to the project directory.
   - Execute commands to create and activate the virtual environment, install ipykernel, and link it to the Jupyter notebook.

2. Install Required Libraries:
   - Activate the virtual environment and install the necessary libraries from the requirements.txt file.

### 3.0.2. Additional Library Installation
To enhance the functionality of the CoreAI environment, some additional libraries not pre-installed may be required. Follow these steps to install the necessary libraries from the `requirements.txt` file:
1. Open your terminal or command prompt within the Jupyter notebook: `File -> New -> Terminal`.
2. Navigate to the project directory:
   ```bash
   cd /path/to/your/project/directory
   pwd
3. Execute the following commands to create and activate the virtual environment:
   ```bash
   python3 -m venv --system-site-packages myvenv
   source myvenv/bin/activate
   pip3 install ipykernel
   python -m ipykernel install --user --name=myvenv --display-name="Python (myvenv)"
   pip install -r requirements.txt

- After installing libraries from the `requirements.txt` file, ensure you select the correct Python kernel (`Python (myvenv)`) in your Jupyter notebook.

### 3.0.3. Run the Notebook:
1. Open the `Yelp_Ratings_Predictor.ipynb` notebook in a Jupyter environment.
2. Execute the notebook cells sequentially to perform data analysis and model training.

### 3.0.4. Model Training and Evaluation:
1. Follow the steps within the notebook to train the model using the provided dataset.
2. Evaluate the model's performance and adjust parameters as needed.

### 3.0.5. Model Usage:
- Use the trained model to predict Yelp ratings based on new review data, facilitating better business insights and decision-making.

### 3.0.6. Troubleshooting
If you encounter issues:
- **Environment Setup**: Ensure that the virtual environment is correctly set up and that all libraries are installed as per the instructions.
- **Dataset Loading**: Verify that the dataset files are correctly placed in the `data` folder and that file paths in the notebook match.

This revised README should now comprehensively cover the setup, usage, and troubleshooting steps for your project. If any more adjustments are needed, please let me know!

