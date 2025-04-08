<h1>CoreAI: Tech Projects</h1>

Examples using CoreAI (CUDA, TensorFlow, PyTorch, OpenCV) as their source container.

CoreAI: https://github.com/Infotrend-Inc/CoreAI

CoreAI is a powerful environment designed to facilitate machine learning, computer vision and NLP projects. These examples have been adapted from public sources and presented as Jupyter Notebooks to demonstrate the versatility and capabilities of CoreAI. Each project leverages different libraries and tools within the CoreAI environment to solve domain-specific problems. This collection serves as a practical resource for developers and researchers to explore various machine learning, computer vision and NLP techniques.


# Project List

| Domain | Project Name | Link to Directory |
| --- | --- | --- |
| Computer Vision | Fashion MNIST Classification | [Fashion_MNIST_Classification](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Fashion_MNIST_Classification) |
| Computer Vision | Fast Neural Style Transfer | [Fast_neural-Style-Transfer](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Fast_neural-Style-Transfer) |
| Computer Vision | Image Background Removal | [Image_Background_Removal](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Image_Background_Removal) |
| Data Science | Amex Default Prediction | [amex-default-prediction](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/amex-default-prediction) |
| Data Science | Home Credit Default Risk Recognition | [Home-Credit-Default-Risk-Recognition](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Home-Credit-Default-Risk-Recognition) |
| Data Science | Hotel reservation cancellation Prediction | [Hotel_reservation_cancellation](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Hotel_reservation_cancellation) |
| Data Science | Predicting Yelp Ratings | [predicting-yelp-ratings](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/predicting-yelp-ratings) |  
| Data Science | Wind turbine failure detection | [Wind_turbine_failure_detection](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Wind_turbine_failure_detection) |
| Large Language Model (Computer Vision) | Flux1Schnell Image Generation | [Flux1Schnell](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Flux1Schnell) |
| Large Language Model (and Computer Vision) | Gemma3 LLM + VLM (Image Understanding) | [Gemma3](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Gemma3) |
| Machine Learning | Electrical Transmission lines Fault detection | [Electrical_Fault_Detection_Classification](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Electrical_Fault_Detection_Classification) |
| Machine Learning| SDXL DreamBooth LoRA Training | [SDXL_DreamBooth_LoRA_Training](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/SDXL_DreamBooth_LoRA%20_Training) |
| Machine Learning | Sleep Disorder Prediction | [Sleep_Disorder_prediction](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Sleep_Disorder_prediction) |
| Natural Language Processing | Next Word Prediction | [Next_word_prediction](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Next_word_prediction) |
| Natural Language Processing | NLP with Disaster Tweets | [NLP_with_DisasterTweets](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/NLP_with_DisasterTweets) |
| Natural Language Processing | Sentiment Analysis | [Sentiment_Analysis](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Sentiment_Analysis) |

## Testing a Notebook

On a system with an NVIDIA GPU and docker configured to use it, clone the repo, go into a directory with the notebook you want to try and get a ready-to-use Jupyter Notebook with CUDA, TensorFlow, PyToch and OpenCV available by following the instructions in each individual README.md file present in the subfolders, before going to http://127.0.0.1:8888/ and login using the default "iti" password.

In general, the tool can be started by running:


```bash
# Run one of the following commands:

# podman command
podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh

# docker command
docker run --rm -it --runtime=nvidia --gpus all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest  /run_jupyter.sh
```

## A note on tags

Published tags should match the tags in the [CoreAI](https://github.com/Infotrend-Inc/CoreAI) repository.
