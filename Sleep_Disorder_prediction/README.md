<h1>Sleep Disorder Prediction</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original Notebook](#13-original-notebook)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
    - [1.5.1. How to Download Dataset](#151-how-to-download-dataset)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. Expected Packages and Resource Requirements](#31-expected-packages-and-resource-requirements)
  - [3.2. How To Use](#32-how-to-use)
  - [3.3. Ensure Proper Folder Structure](#33-ensure-proper-folder-structure)


# 1. Project Details

## 1.1. Original Author

**GitHub Profile**: [Sukhman Singh](https://github.com/SUKHMAN-SINGH-1612)

## 1.2. Original License

MIT License  
This project is licensed under the MIT License - see the [LICENSE](https://github.com/SUKHMAN-SINGH-1612/Data-Science-Projects/blob/main/LICENSE) file for details.

## 1.3. Original Notebook

[Sleep Disorder Prediction Notebook](https://github.com/SUKHMAN-SINGH-1612/Data-Science-Projects/blob/main/Sleep%20Disorder%20Prediction/Sleep%20Disorder%20Prediction.ipynb)

## 1.4. Description of Project

This project focuses on predicting sleep disorders by analyzing various lifestyle and medical variables such as age, BMI, physical activity, sleep duration, blood pressure, and more. By utilizing machine learning techniques, the model aims to identify patterns and factors contributing to sleep disorders, enabling early intervention and improved healthcare outcomes.

## 1.5. Required Datasets

**Sleep Health and Lifestyle Dataset** - [Kaggle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)

### 1.5.1. How to Download Dataset

To access and download the dataset, please follow these steps:

1. Visit the Kaggle dataset page through the link provided above.
2. Click on the "Download" button on the dataset page to download the dataset zip file.
3. Unzip the downloaded file into the folder where you will run the Jupyter notebook. This step ensures that all data files are ready to be accessed by the notebook.

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `Sleep_Disorder_Prediction.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. Expected Packages and Resource Requirements

**Python Packages**:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

**Resource Requirements**:
- CPU

## 3.2. How To Use

1. **Setup Environment**:
   - Clone the repository or download the specific project files.
   - Ensure Python 3.x is installed.

2. **Install Required Packages**:

   To enhance the functionality of the CoreAI environment, you may need to install some libraries not pre-installed but required for this notebook. Follow these steps to install the necessary libraries from the `requirements.txt` file:

   **2.1 Create and Activate the Virtual Environment:**
   
   Open your terminal or command prompt within the Jupyter notebook. `File -> New -> Terminal`

   Navigate to the project directory where you want to set up the environment.

   Execute the following commands to create and activate the virtual environment:

   ```sh
   bash
   python3 -m venv --system-site-packages myvenv #myvenv is name of virtual environment you can change it
   source myvenv/bin/activate
   pip3 install ipykernel
   python -m ipykernel install --user --name=myvenv --display-name="Python (myvenv)"
   ```

   **2.2 Install Required Libraries**

   Before running the following command in the Jupyter notebook, make sure you are in the directory where the Jupyter Notebook and virtual environment is located. This ensures the `./` path is always current. You can use the `cd` command to change to your project directory and `pwd` to verify your current directory.

   ```sh
   !. ./myvenv/bin/activate; pip install -r requirements.txt
   ```

3. **Run the Notebook**:
   - Open the `Sleep_Disorder_Prediction.ipynb` notebook in a Jupyter environment.
   - Load the "Python (myvenv)" kernel.
   - Execute the notebook cells sequentially to perform data analysis, model training, and evaluation.

4. **Model Training and Evaluation**:
   - Follow the steps within the notebook to train the model using the provided dataset.
   - Evaluate the model's performance and tweak parameters as necessary to improve accuracy.

5. **Model Usage**:
   - The trained model can be used to predict sleep disorders for new data, helping healthcare professionals to identify at-risk individuals and provide early interventions.

## 3.3. Ensure Proper Folder Structure

Make sure that the folders in your directory are structured as follows to ensure the notebook runs correctly:
- The dataset file `Sleep_health_and_lifestyle_dataset.csv` should be in the same directory as the notebook.
- Ensure any output directories specified in the notebook exist or adjust the paths accordingly.
