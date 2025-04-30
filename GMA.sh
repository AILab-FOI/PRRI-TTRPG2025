#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing..."

    if [ -x "$(command -v apt)" ]; then
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif [ -x "$(command -v yum)" ]; then
        sudo yum install -y python3 python3-pip
    else
        echo "Unsupported package manager. Please install Python manually."
        exit 1
    fi
fi

# Install Python packages
python3 -m pip install --upgrade pip
python3 -m pip install Pillow openai pygame

# Run the application
nohup python3 app.py > /dev/null 2>&1 &

# Exit script (auto-close terminal)
exit 0
