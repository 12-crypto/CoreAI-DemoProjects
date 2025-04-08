<h1>Home Credit Default Risk Recognition</h1>

In `.WiP` folder: `featuretools` is not maintained.

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original GitHub Link](#12-original-github-link)
  - [1.3. Description of Project](#13-description-of-project)
  - [1.4. Required Datasets](#14-required-datasets)
    - [1.4.1. How to Set Up the Dataset](#141-how-to-set-up-the-dataset)
  - [1.5. Expected Packages and Resource Requirements](#15-expected-packages-and-resource-requirements)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. How To Use](#31-how-to-use)
    - [3.1.1. Important Note](#311-important-note)
  - [3.2. Troubleshooting](#32-troubleshooting)


# 1. Project Details

## 1.1. Original Author

**GitHub Profile**: [Abhishek Bihani](https://github.com/abhishekdbihani)

## 1.2. Original GitHub Link

[Home Credit Default Risk Recognition Repository](https://github.com/abhishekdbihani/Home-Credit-Default-Risk-Recognition/tree/master)

## 1.3. Description of Project

This project aims to predict the ability of applicants to repay a loan based on historical financial data. Utilizing machine learning techniques, the model assesses the creditworthiness of potential borrowers, enhancing the decision-making process for granting loans. This solution is particularly beneficial in providing an opportunity for people who struggle to get loans due to insufficient credit history.

## 1.4. Required Datasets

The datasets used in this project are detailed financial records provided by Home Credit, each describing a different aspect of the applicant's financial history:

- **application_{train|test}.csv**: Main tables for training and testing. Includes static data for all applications, with one row per loan.
- **bureau.csv**: Information about client's previous credits from other financial institutions.
- **bureau_balance.csv**: Monthly balances of previous credits in the Credit Bureau.
- **POS_CASH_balance.csv**: Monthly balance snapshots of previous POS and cash loans with Home Credit.
- **credit_card_balance.csv**: Monthly balance snapshots of previous credit cards with Home Credit.
- **previous_application.csv**: All previous applications for Home Credit loans for clients who have loans in our sample.
- **installments_payments.csv**: Repayment history for previously disbursed credits in Home Credit.
- **HomeCredit_columns_description.csv**: Descriptions for the columns in the various data files.

### 1.4.1. How to Set Up the Dataset
1. Create a `data` folder in your project directory.
2. Download the datasets from [Home Credit Dataset](https://www.kaggle.com/c/home-credit-default-risk/data) on Kaggle.
   - Note: You will need to log in to Kaggle to access and download these files due to the special rules set by the competition.
3. Place the downloaded files into the `data` folder.


## 1.5. Expected Packages and Resource Requirements

**Python Packages**:
- pydash
- featuretools
- lightgbm
- hyperopt
- featuretools==0.16

**Resource Requirements**:
- CPU

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `Home-Credit-Default-Risk-Recognition.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. How To Use

1. **Setup Environment**:
   - Clone the repository or download the specific project files.
   - Ensure Python 3.x is installed.

2. **Install Required Packages**:

   - To enhance the functionality of the CoreAI environment, you may need to install some libraries not pre-installed but required for this notebook. Follow these steps to install the necessary libraries from the `requirements.txt` file:

   **2.1 Create and Activate the Virtual Environment:**
   
   Open your terminal or command prompt within the jupyter notebook. `File -> New -> Terminal`
   
   Navigate to the project directory where you want to set up the environment.
   
   Execute the following commands to create and activate the virtual environment:
   
   ```
   python3 -m venv --system-site-packages myvenv #myvenv is name of virtual environment you can change it
   source myvenv/bin/activate
   pip3 install ipykernel
   python -m ipykernel install --user --name=myvenv --display-name="Python (myvenv)"
   ```
   **2.2 Install Required Libraries**
   
   Before running the following command in jupyter notebook, make sure you are in the directory where the Jupyter Notebook and virtual environment is located. This ensures the ./ path is always current. You can use the cd command to change to your project directory and pwd to verify your current directory.
   
   ```
   !. ./myvenv/bin/activate; pip install -r requirements.txt
   ```
### 3.1.1. Important Note

It is crucial to load the new "myvenv" kernel for the notebook to work correctly. If the new "myvenv" kernel is not loaded, the required libraries and environment settings will not be applied, and the notebook will not function as expected.

3. **Run the Notebook**:
   - Open the `Home Credit Risk Notebook.ipynb` in a Jupyter environment.
   - Execute the notebook cells sequentially to perform data loading, preprocessing, feature engineering, model training, and evaluation.

4. **Model Usage**:
   - **Predictive Capability**: The trained models can be used to predict default risk on new customer data, thereby helping financial institutions make informed loan approval decisions.

## 3.2. Troubleshooting
- Ensure all required packages from `requirements.txt` are properly installed.
- Verify that dataset paths in the notebook match the location of the downloaded files.
- Check Python version compatibility with the packages used.
- If the notebook crashes or fails to execute, check for sufficient memory availability as the datasets and models may require significant resources.
- Ensure the kernel used matches the virtual environment where dependencies are installed. If not, switch to the correct kernel using the Jupyter interface.
