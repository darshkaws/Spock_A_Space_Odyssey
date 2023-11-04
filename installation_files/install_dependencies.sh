#!/bin/bash

# Install Python dependencies
pip install pyfiglet
pip install termcolor
pip install pygame

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
else
    echo "Failed to install dependencies."
fi
