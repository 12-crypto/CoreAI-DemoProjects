<h1>Fashion MNIST Classification using Neural Networks</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Required Datasets](#15-required-datasets)
  - [1.6. Resource Requirements](#16-resource-requirements)
  - [1.7. Capabilities to Run on CPU and/or GPU](#17-capabilities-to-run-on-cpu-andor-gpu)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. How To Use](#31-how-to-use)
  - [3.2. Troubleshooting Guides](#32-troubleshooting-guides)
    - [3.2.1. Issue 1: Environment Setup Failures](#321-issue-1-environment-setup-failures)
    - [3.2.2. Issue 2: Model Not Training](#322-issue-2-model-not-training)
    - [3.2.3. Issue 3: GPU Utilization Not Detected](#323-issue-3-gpu-utilization-not-detected)
    - [3.2.4. Algorithm Insights](#324-algorithm-insights)


# 1. Project Details

## 1.1. Original Author
- Sunil Singh
- [GitHub Profile](https://github.com/sssingh)

## 1.2. Original License
- [MIT License](https://choosealicense.com/licenses/mit/)
- This project is licensed under the MIT License - see the LICENSE.md file for details.

## 1.3. Original GitHub Link
- [Fashion MNIST Classification Repository](https://github.com/sssingh/fashion-mnist-classification)

## 1.4. Description of Project
This project utilizes a custom-built, fully-connected neural network to classify apparel images from the Fashion-MNIST dataset. Developed as a more complex alternative to the standard MNIST digit classification, this project serves as a benchmark for neural network capabilities in multi-label image classification.

## 1.5. Required Datasets
- Fashion MNIST dataset (included in PyTorch's torchvision package)
- [Direct dataset links](https://www.tensorflow.org/tutorials/keras/classification)

## 1.6. Resource Requirements
- CPU or GPU (NVIDIA GPU recommended for optimal performance)
- Recommended GPU: NVIDIA Quadro P5000 with 16GB memory
- Approximate training and validation time for 35 epochs: 15 minutes on recommended GPU setup.

## 1.7. Capabilities to Run on CPU and/or GPU
This project is configured to automatically detect and utilize a GPU if available, ensuring faster processing and training times. If a GPU is not available, the project will gracefully fallback to using the CPU.

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 --name CoreAI-FashionMNISTClassification docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 --name CoreAI-FashionMNISTClassification infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `Fashion_MNIST_Classification.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. How To Use
To get started with this project, follow these steps:

1. **Setup Environment:**
   - Clone the repository or download all project files, including the `Fashion_MNIST_Classification.ipynb` notebook.
   - No installation of packages is required as the project runs within the Infotrend pre-built container which includes all necessary dependencies.

2. **Run the Notebook:**
   - Open the `Fashion_MNIST_Classification.ipynb` notebook using Jupyter Notebook or JupyterLab.
   - Execute the notebook cells sequentially from start to finish. The environment will automatically detect and utilize a GPU if available; otherwise, it will use the CPU.

3. **Model Training and Evaluation:**
   - Follow the steps in the notebook to train and evaluate the neural network model on the Fashion MNIST dataset.
   - The notebook provides detailed instructions and visualizations of the training process and model performance.

4. **Model Usage:**
   - Once trained, the model can classify new images of apparel from the Fashion MNIST dataset. Instructions for using the model for prediction are provided within the notebook.

## 3.2. Troubleshooting Guides
This section addresses common issues you might encounter when running the `Fashion_MNIST_Classification.ipynb` notebook:

### 3.2.1. Issue 1: Environment Setup Failures
**Symptom:** Failure to launch the Jupyter Notebook in the Infotrend container.
**Solution:** Ensure the Infotrend container is running and properly set up. Verify network settings and container configurations. Restart the container if necessary.

### 3.2.2. Issue 2: Model Not Training
**Symptom:** The model does not show improvement over epochs.
**Solution:** Check the learning rate and optimizer settings. Ensure that the dataset is correctly loaded and preprocessed. Consider modifying hyperparameters or increasing the dataset size for training.

### 3.2.3. Issue 3: GPU Utilization Not Detected
**Symptom:** The system falls back to CPU even though a GPU is available.
**Solution:** Verify the GPU installation and driver updates. Ensure PyTorch is configured to recognize the GPU. Use the command `torch.cuda.is_available()` to check GPU availability from within the notebook.

### 3.2.4. Algorithm Insights
The fully-connected neural network used in this project is designed for simplicity to demonstrate basic image classification techniques. While it lacks the spatial hierarchy of convolutional networks, it serves as a practical starting point for understanding neural network operations. For more complex image recognition tasks, consider exploring architectures involving convolutional layers that preserve spatial relationships within images.

[Back to Top](#project-fashion-mnist-classification-using-neural-networks)
