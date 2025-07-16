<h1>CoreAI: Tech Projects</h1>

Examples using CoreAI (CUDA, TensorFlow, PyTorch, OpenCV) as their source container.

CoreAI: https://github.com/Infotrend-Inc/CoreAI

CoreAI is a powerful environment designed to facilitate machine learning, computer vision and NLP projects. These examples have been adapted from public sources and presented as Jupyter Notebooks to demonstrate the versatility and capabilities of CoreAI. Each project leverages different libraries and tools within the CoreAI environment to solve domain-specific problems. This collection serves as a practical resource for developers and researchers to explore various machine learning, computer vision and NLP techniques.


# Project List

| Domain | Project Name | Link to Directory |
| --- | --- | --- |
| Computer Vision | CLIP (Contrastive Language-Image Pre-training) Model Implementation | [OpenAI-CLIP](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/OpenAI-CLIP) |
| Computer Vision | Fashion MNIST Classification | [Fashion_MNIST_Classification](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Fashion_MNIST_Classification) |
| Computer Vision | Fast Neural Style Transfer | [Fast_neural-Style-Transfer](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Fast_neural-Style-Transfer) |
| Computer Vision | Image Background Removal | [Image_Background_Removal](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Image_Background_Removal) |
| Data Science | Amex Default Prediction | [amex-default-prediction](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/amex-default-prediction) |
| Data Science | Home Credit Default Risk Recognition | [Home-Credit-Default-Risk-Recognition](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Home-Credit-Default-Risk-Recognition) |
| Data Science | Hotel reservation cancellation Prediction | [Hotel_reservation_cancellation](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Hotel_reservation_cancellation) |
| Data Science | Predicting Yelp Ratings | [predicting-yelp-ratings](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/predicting-yelp-ratings) |  
| Data Science | Wind turbine failure detection | [Wind_turbine_failure_detection](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Wind_turbine_failure_detection) |
| Large Language Model | AI Agent with Web Search and LiteLLM | [Agent](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Agent) |
| Large Language Model (Computer Vision) | Flux1Schnell Image Generation | [Flux1Schnell](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Flux1Schnell) |
| Large Language Model (and Computer Vision) | Gemma3 LLM + VLM (Image Understanding) | [Gemma3](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Gemma3) |
| Large Language Model | RAG Pipeline | [RAG_Pipeline](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/RAG_Pipeline) |
| Machine Learning | Document Extraction with Docling | [DoclingExtract](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/DoclingExtract) |
| Machine Learning | Electrical Transmission lines Fault detection | [Electrical_Fault_Detection_Classification](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Electrical_Fault_Detection_Classification) |
| Machine Learning| SDXL DreamBooth LoRA Training | [SDXL_DreamBooth_LoRA_Training](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/SDXL_DreamBooth_LoRA%20_Training) |
| Machine Learning | Sleep Disorder Prediction | [Sleep_Disorder_prediction](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Sleep_Disorder_prediction) |
| Multimedia Processing | Lyrical Video Generator | [Lyrical_Video_Generator](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Lyrical_Video_Generator) |
| Multimedia Processing | Video Transcription | [Video_Transcription](https://github.com/Infotrend-Inc/CoreAI-DemoProjects/tree/main/Video_Transcription) |
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

# GPU Trader

Many thanks to [GPU Trader](https://www.gputrader.io/) for generously supporting [Infotrend Inc]( https://infotrend.com/)’s Summer 2025 intern cohort by providing access to a high-performance GPU. This vital resource enabled our interns to explore advanced AI applications and accelerate the development of their proof-of-concept projects.

GPU Trader is a platform dedicated to democratizing access to GPU power. Whether you’re a researcher, AI developer, or startup in need of scalable compute resources, GPU Trader connects you to a global network of GPU providers offering cost-effective and on-demand rentals. 

GPU Trader’s managed templates helped our team quickly spin up environments without significant setup cycles, allowing us to focus on development. Having reliable, on-demand access to powerful data center GPUs has streamlined our workflow significantly.

Thanks to this partnership, our interns successfully built and showcased several innovative projects featured in our [CoreAI-DemoProjects]( https://github.com/Infotrend-Inc/CoreAI-DemoProjects). We’re grateful for GPU Trader's commitment to supporting the next generation of AI talent and research.

## Deploying CoreAI on GPU Trader

The following two methods can be used to deploy CoreAI on GPU Trader on any instance with at least CUDA 12.6.

### Basic Authentication template

This template relies on GPU Trader's built-in authentication system and will generate a secure URL, a password and a user to access the environment.

```yaml
services:
  coreai:
    stdin_open: true
    tty: true
    volumes:
      - ./iti:/iti
    environment:
      - NVIDIA_DRIVER_CAPABILITIES=all
      - TZ="America/New_York"
    user: root
    image: infotrend/coreai:25a01-ctpo-12.6.3_2.18.1_2.6.0_4.11.0
    entrypoint: python3 /usr/local/bin/jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --IdentityProvider.token='' --NotebookApp.token='' --NotebookApp.password=''
    ports:
      - 8888:8888
    restart: unless-stopped
    labels:
      - io.gputrader.ports.name.8888=CoreAI
    shm_size: '2gb'
```


### Tailscale access template

This method allows the user to access the CoreAI environment within their Tailscale network using [auth keys](https://tailscale.com/kb/1085/auth-keys). This method does not need the `Basic Authentication` or `SSH connection` template options as the new host will appear on the end users's Tailscale `machines` list.

```yaml
services:
  coreai:
    stdin_open: true
    tty: true
    volumes:
      - ./iti:/iti
    environment:
      - NVIDIA_DRIVER_CAPABILITIES=all
      - TZ="America/New_York"
    user: root
    image: infotrend/coreai:25a01-ctpo-12.6.3_2.18.1_2.6.0_4.11.0
    entrypoint: python3 /usr/local/bin/jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --IdentityProvider.token='' --NotebookApp.token='' --NotebookApp.password=''
    depends_on:
      - tailscale-coreai
    network_mode: service:tailscale-coreai
    restart: unless-stopped
    shm_size: '2gb'
  tailscale-coreai:
    image: tailscale/tailscale:latest
    hostname: tailscale-coreai
    environment:
      - TS_AUTHKEY=tskey-client-REPLACEWITHYOURREALAUTHKEY
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_USERSPACE=false
    volumes:
      - .ts:/var/lib/tailscale
    devices:
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - net_admin
    restart: unless-stopped
```