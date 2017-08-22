#!/bin/bash

apt install python-pip
pip install -U pip

pip install -r requirements.txt

sudo apt remove python-scapy
sudo pip uninstall scapy
sudo apt-get install python-scapy

sudo apt-get install libpcap-dev
sudo apt remove python-pcapy
sudo pip uninstall pcapy
sudo apt-get install python-pcapy
