#!/bin/bash

if [ -z "$HF_TOKEN" ]; then
    echo "Error: HF_TOKEN environment variable is not set."
    exit 1
fi

podman run --rm -it --userns=keep-id --device nvidia.com/gpu=all -e WANTED_UID=`id -u` -e WANTED_GID=`id -g` -e CoreAI_VERBOSE="yes" -e HF_TOKEN=${HF_TOKEN} -v /dev/video0:/dev/video0  -v `pwd`:/iti -p 8888:8888 docker.io/infotrend/coreai:latest
