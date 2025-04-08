<h1>SkimLit: Skimming Literature with NLP</h1>

In `.WiP`: issue with XLA

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
    - [1.5.1. How to Download Dataset](#151-how-to-download-dataset)
    - [1.5.2. File Descriptions](#152-file-descriptions)
    - [1.5.3. Setup for Dataset Use](#153-setup-for-dataset-use)
  - [1.6. Contents of the Notebook](#16-contents-of-the-notebook)
  - [1.7. Expected Packages and Resource Requirements](#17-expected-packages-and-resource-requirements)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. How To Use](#31-how-to-use)
    - [3.1.1. Important Note](#311-important-note)
  - [3.2. Troubleshooting Tips](#32-troubleshooting-tips)


# 1. Project Details

## 1.1. Original Author

**GitHub Profile**: [Itsskofficial](https://github.com/itsskofficial)

## 1.2. Original License

MIT License  
This project is licensed under the MIT License - see the LICENSE file for details in the original repository.

## 1.3. Original GitHub Link

[SkimLit: Skimming Literature with NLP](https://github.com/itsskofficial/Natural-Language-Processing/tree/master/Projects/SkimLit)

## 1.4. Description of Project

This project uses natural language processing techniques to analyze and classify sentences from scientific abstracts. The goal is to automate the extraction of important information from scientific papers, which is crucial for researchers and professionals who need to quickly review and understand the literature.

## 1.5. Required Datasets

**PubMed 20k RCT Dataset**:

This project utilizes text files from the `PubMed_20k_RCT_numbers_replaced_with_at_sign` folder, which should be downloaded and stored in a `data` directory accessible by the notebook.

### 1.5.1. How to Download Dataset

To access and set up the datasets, please follow these steps:

1. Create a `data` folder in your project directory if it doesn't already exist.
2. Download the text files from the following Kaggle dataset link:
   - [PubMed 20k RCT Dataset](https://www.kaggle.com/datasets/matthewjansen/pubmed-200k-rtc?select=PubMed_200k_RCT_numbers_replaced_with_at_sign) (ensure you comply with the dataset's usage rules).
3. Place the downloaded text files into the `data` folder. This step ensures that all data files are ready to be accessed by the notebook.

### 1.5.2. File Descriptions

- **train.txt**: Contains the training data with sentences from scientific abstracts and their corresponding labels.
- **dev.txt**: Contains the validation data used for tuning the model.
- **test.txt**: Contains the test data used for evaluating the model's performance.

### 1.5.3. Setup for Dataset Use

After placing the files in the `data` directory, ensure your Jupyter notebook is configured to read from this directory. This might involve setting the correct path to the `data` folder in your data loading script or notebook cells.

## 1.6. Contents of the Notebook

- **Introduction**: Overview of the project's aim and importance.
- **Basic Exploratory Data Analysis**: Initial analysis of the data to understand the distribution and nature of the dataset.
- **Text Normalization**: Processing steps to clean and normalize the text data.
- **Model Building**: Implementation of various models to classify sentences in scientific abstracts.
- **Model Evaluation**: Evaluation of the models' performance using appropriate metrics.
- **Acknowledgements**: Credits to data providers and contributors.
- **References**: Sources and inspirations for the project methodology.

## 1.7. Expected Packages and Resource Requirements

**Python Packages**:
- numpy
- pandas
- scikit-learn
- tensorflow
- tensorflow_hub
- tensorflow_text
- seaborn
- matplotlib

**Resource Requirements**:
- CPU or GPU (GPU recommended for faster processing)

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `SkimLit.ipynb`.

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
 Open the skim_lit.ipynb notebook in a Jupyter environment.
 Execute the notebook cells sequentially to perform data loading, preprocessing, model training, and evaluation.

5. **Model Usage**:
- **Predictive Capability**: The trained model can accurately classify sentences in scientific abstracts, facilitating rapid literature review and information extraction for researchers.

## 3.2. Troubleshooting Tips

1. **Environment Issues**:
- Ensure that the correct virtual environment is activated before running the notebook.
- Verify that all required packages are installed. If not, re-run the installation command: `pip install -r requirements.txt`.

2. **Data Loading Problems**:
- Ensure that the `data` directory contains the required dataset files (`train.txt`, `dev.txt`, and `test.txt`).
- Check the file paths in the notebook to ensure they correctly point to the `data` directory.

3. **Kernel Errors**:
- If the notebook is not recognizing the correct kernel, restart the Jupyter server and select the appropriate kernel (`Python (myvenv)`).

4. **Performance Issues**:
- If the model training is slow, consider using a machine with a GPU. Configure TensorFlow to use the GPU if available.

5. **Model Training Errors**:
- Ensure the dataset is correctly preprocessed and formatted before feeding it into the model.
- Check for any NaN or infinite values in the dataset that might cause training to fail.