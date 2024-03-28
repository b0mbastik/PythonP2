#!/bin/bash

echo Creating the venv...
python3 -m venv venv
echo Created!
source venv/bin/activate
echo Installing Dependencies
pip install -r requirements.txt
echo Done!
