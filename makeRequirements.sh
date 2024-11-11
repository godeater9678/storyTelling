#!/bin/bash

#rm requirements.txt
pip3 install pipreqs
pipreqs ./

pip3 install -U -r ./requirements.txt
