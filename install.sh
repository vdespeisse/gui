#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
venv/bin/python api.py
