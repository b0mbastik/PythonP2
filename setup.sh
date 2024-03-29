#!/bin/bash


if [ -d venv ]
then
  echo Virtual Environemnt under 'venv' already exists!
else 
  echo Creating the Virtual Environemnt under 'venv'...
  python3 -m venv venv
  echo Created!
fi

source venv/bin/activate
echo Installing Dependencies...
pip install -r requirements.txt
echo Done!
