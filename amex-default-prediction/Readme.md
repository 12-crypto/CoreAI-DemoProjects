<h1>Amex Default Prediction</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
    - [1.5.1. How to Download Dataset](#151-how-to-download-dataset)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. Expected Packages and Resource Requirements](#31-expected-packages-and-resource-requirements)
  - [3.2. How To Use](#32-how-to-use)
  - [3.3. Troubleshooting](#33-troubleshooting)
  - [3.4. Changes Made to the Original Notebook](#34-changes-made-to-the-original-notebook)

# 1. Project Details

## 1.1. Original Author

**GitHub Profile**: [Marcos Ots](https://github.com/N0t10n)

## 1.2. Original License

MIT License  
This project is licensed under the MIT License - see original repo for details.

## 1.3. Original GitHub Link

[Amex Default Prediction Notebook](https://github.com/N0t10n/Amex_default_prediction/blob/main/model.ipynb)

## 1.4. Description of Project

This project aims to predict default risk using the American Express Default Prediction dataset. Utilizing advanced machine learning techniques, the project analyzes and predicts customer default likelihood, thereby enhancing financial decision-making processes.

## 1.5. Required Datasets

**American Express Default Prediction Dataset**:

Download the following datasets and place them in a `data` directory accessible by the notebook.

- Obtain the [Amex Kaggle Dataset Main Page](https://www.kaggle.com/competitions/amex-default-prediction/data) (those datasets have special rules as can be seen at [https://www.kaggle.com/competitions/amex-default-prediction/rules](https://www.kaggle.com/competitions/amex-default-prediction/rules))

- Obtain the Kaggle Feather Files from [Kaggle Feather Dataset](https://www.kaggle.com/datasets/ruchi798/parquet-files-amexdefault-prediction), download the `.ftr` (Feather format) files for efficient data handling

### 1.5.1. How to Download Dataset
To access and download the datasets, please follow these steps:

1. Visit the Kaggle dataset pages through the links provided above.
2. Click on the "Download" button on the dataset page to download the dataset zip files.
3. Create a `data` folder in the directory with the Jupyter notebook and unzip the downloaded files into that folder. This step ensures that all data files are ready to be accessed by the notebook.
4. Create a `models` folder in the same directory. This folder will be used to store and fetch the machine learning models you train.

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 --name CoreAI-AmexDefaultPrediction docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 --name CoreAI-AmexDefaultPrediction infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `amex-default-prediction.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. Expected Packages and Resource Requirements

**Python Packages**:
- pandas
- numpy
- matplotlib
- scikit-learn
- xgboost
- TensorFlow
- keras

**Resource Requirements**:
- CPU or GPU (optional for faster training)

## 3.2. How To Use

1. **Setup Environment**:
   - Clone the repository or download the specific project files.
   - Ensure Python 3.x is installed.

2. **Install Required Packages**:

   - To enhance the functionality of the CTPO environment, you may need to install some libraries not pre-installed but required for this notebook. Follow these steps to install the necessary libraries from the `requirements.txt` file:

   **2.1 Create and Activate the Virtual Environment:**
   
   Open your terminal or command prompt within the jupyter notebook. `File -> New -> Terminal`
   
   Navigate to the project directory where you want to set up the environment.
   
   Execute the following commands to create and activate the virtual environment:
   
   ```
   python3 -m venv --system-site-packages myvenv #myvenv is name of virtual environment you can change it
   bash
   source myvenv/bin/activate
   pip3 install ipykernel
   python -m ipykernel install --user --name=myvenv --display-name="Python (myvenv)"
   ```
   **2.2 Install Required Libraries**
   
   Before running the following command in jupyter notebook, make sure you are in the directory where the Jupyter Notebook and virtual environment is located. This ensures the ./ path is always current. You can use the cd command to change to your project directory and pwd to verify your current directory.
   
   ```
   !. ./myvenv/bin/activate; pip install -r requirements.txt
   ```

3. **Run the Notebook**:
- Open the `amex-default-prediction.ipynb` notebook in a Jupyter environment.
- Execute the notebook cells sequentially to perform data processing, model training, and evaluation.

4. **Model Training and Evaluation**:
- Follow the steps within the notebook to train the model using the provided dataset.
- Evaluate the model's performance and tweak parameters as necessary to improve accuracy.

5. **Model Usage**:
- The trained model can be used to predict the likelihood of customer defaults, providing valuable insights for financial decision-making.

## 3.3. Troubleshooting

- Ensure that the name of the dataset file is the same as referenced in the notebook.
- Make sure the Jupyter notebook and the dataset are in the same folder to avoid file path issues.
- Change the model saving path based on your directory structure to ensure the model is saved correctly.

## 3.4. Changes Made to the Original Notebook

- Integrated Exploratory Data Analysis (EDA) and modeling into a single Jupyter notebook.
- Combined the training dataset with target labels, which was not present in the original implementation.
- Addressed issues related to non-numeric data by employing appropriate preprocessing methods, including label encoding and imputation strategies.

