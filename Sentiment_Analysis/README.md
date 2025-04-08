<h1>Fine-tuning TinyBERT for Sentiment Analysis</h1>

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

**GitHub Profile**: [David Chavez](https://github.com/dnachavez)

## 1.2. Original License

MIT License  
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/dnachavez/fine-tuning-tinybert-for-sentiment-analysis/blob/main/LICENSE) file for details.

## 1.3. Original GitHub Link

[Fine-tuning TinyBERT for Sentiment Analysis Notebook](https://github.com/dnachavez/fine-tuning-tinybert-for-sentiment-analysis/blob/main/Fine-tuning%20TinyBERT%20for%20Sentiment%20Analysis.ipynb)

## 1.4. Description of Project

This project focuses on fine-tuning the TinyBERT model for sentiment analysis. The goal is to leverage the lightweight TinyBERT model to achieve efficient and accurate sentiment classification on a dataset containing text from tweets. By analyzing the sentiment of these tweets, the model can provide valuable insights into public opinion and sentiment trends.

## 1.5. Required Datasets

Sentiment Analysis Data - [Kaggle Dataset](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset?select=test.csv)

### 1.5.1. How to Download Dataset
To access and download the dataset, please follow these steps:

1. Visit the Kaggle dataset page through the link provided above.
2. Click on the "Download" button on the dataset page to download the dataset zip file.
3. Create a `data` folder in the directory with the Jupyter notebook and unzip the downloaded file into that folder. This step ensures that all data files are ready to be accessed by the notebook.

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `Fine_tuning_TinyBERT_for_Sentiment_Analysis.ipynb`.

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
- transformers
- torch
- nltk

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
   bash
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

3. **Run the Notebook**:
   - Open the `Fine_tuning_TinyBERT_for_Sentiment_Analysis.ipynb` notebook in a Jupyter environment.
   - Execute the notebook cells sequentially to perform data analysis, model training, and evaluation.

4. **Model Training and Evaluation**:
   - Follow the steps within the notebook to train the model using the provided dataset.
   - Evaluate the model's performance and tweak parameters as necessary to improve accuracy.

5. **Model Usage**:
   - The trained model can be used to predict the sentiment of new text data, providing insights into public opinion and sentiment trends.

## 3.3. Troubleshooting

- Ensure that the name of the dataset file is the same as referenced in the notebook.
- Make sure the Jupyter notebook and the dataset are in the same folder to avoid file path issues.
- Change the model saving path based on your directory structure to ensure the model is saved correctly.

## 3.4. Changes Made to the Original Notebook

- Performed Exploratory Data Analysis (EDA) to understand the dataset.
- Changed the dataset path from the original notebook, which used a drive, to a local dataset.
- Updated the `load_dataset` function to ensure it runs properly with the new dataset.

