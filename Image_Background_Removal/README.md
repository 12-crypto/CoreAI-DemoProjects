<h1>Image Background Removal</h1>

- [1. Project Details](#1-project-details)
  - [1.1. Original Author](#11-original-author)
  - [1.2. Original License](#12-original-license)
  - [1.3. Original GitHub Link](#13-original-github-link)
  - [1.4. Description of Project](#14-description-of-project)
  - [1.5. Changes Made to the Original Notebook](#15-changes-made-to-the-original-notebook)
  - [1.6. Required Datasets](#16-required-datasets)
  - [1.7. Expected Packages and Resource Requirements](#17-expected-packages-and-resource-requirements)
- [2. CoreAI Setup](#2-coreai-setup)
  - [2.1. Stop CoreAI](#21-stop-coreai)
- [3. Detailed Setup](#3-detailed-setup)
  - [3.1. Run the Notebook:](#31-run-the-notebook)
  - [3.2. Model Usage:](#32-model-usage)
  - [3.3. Ensure Proper Folder Structure](#33-ensure-proper-folder-structure)


# 1. Project Details

## 1.1. Original Author

**GitHub Profile**: [Shreyas BK](https://github.com/shreyas-bk)

## 1.2. Original License

MIT License  
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/shreyas-bk/u2netdemo/blob/master/LICENSE) file for details.

## 1.3. Original GitHub Link

[Image Background Removal Notebook](https://github.com/shreyas-bk/u2netdemo/blob/master/DEMOS/U_2_Netp_Demonstration_Colab.ipynb)

## 1.4. Description of Project

This project demonstrates the use of U-2-NETp for various image processing tasks, including background removal, bounding box creation, and salient feature highlighting. U-2-NETp is a lightweight model designed for salient object detection.

## 1.5. Changes Made to the Original Notebook

- Removed the need to clone other repositories by adjusting the paths within both the notebook and the `u2net_test.py` script.

- Created a function in the notebook that allows users to upload images, which are then stored in the images folder.

- Adjusted the `u2net_test.py` script to process the uploaded images and store the results in the results folder.

- The notebook uses the results from the `u2net_test.py` script to remove backgrounds, create bounding boxes, and highlight salient features in the images.

## 1.6. Required Datasets

No external datasets are required for this demonstration as it utilizes user-uploaded images.

## 1.7. Expected Packages and Resource Requirements

**Python Packages**:
- numpy
- tensorflow
- pillow
- opencv-python
- os
- pytorch
- glob

**Resource Requirements**:
- CPU or GPU (optional for faster processing)

# 2. CoreAI Setup

From the folder where this `README.md` is, run:

```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 --name CoreAI-ImageBackgroundRemoval docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 --name CoreAI-ImageBackgroundRemoval infotrend/coreai:latest  /run_jupyter.sh
```

Follow the instructions in the notebook `Image_Removal.ipynb`.

## 2.1. Stop CoreAI

You can stop the Notebook by using the `File -> Shutdown` option.

Alternatively, you can stop the container by pressing `Ctrl + C` in the terminal where the container is running.

# 3. Detailed Setup

## 3.1. Run the Notebook:

1. Open the `Image_Removal.ipynb` notebook in a Jupyter environment.
2. Execute the notebook cells sequentially to see desire results.


## 3.2. Model Usage:

The trained model can be used to:
- Remove backgrounds from images.
- Create bounding boxes around objects.
- Highlight salient features in images.

## 3.3. Ensure Proper Folder Structure

Make sure you have the folders set up the same way as in the repository to ensure the notebook runs correctly. Specifically, ensure that the `images` and `results` directories are created in the project root directory as shown in the setup steps.
