#!/usr/bin/env bash
# installs fabric to machine

pip3 uninstall -y Fabric
apt-get -y install libffi-dev
apt-get -y install libssl-dev
apt-get -y install build-essential
apt-get -y install python3.4-dev
apt-get -y install libpython3-dev
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1
