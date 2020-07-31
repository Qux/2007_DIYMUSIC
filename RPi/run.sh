#!/bin/bash

# move to this directory
cd `dirname $0`

# load venv and run python
source .venv/bin/activate
python main.py
