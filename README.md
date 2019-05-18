## Raspberry Pi 3 G.P.I.O. Control
This is a tool for controlling Raspberry Pi 3 G.P.I.O.

It has been written in [**Python 3**] (https://www.python.org/) using [**PyQt 5.12**](https://www.riverbankcomputing.com/static/Docs/PyQt5/), the python variant for [**Qt 5 Framework**] (https://www.qt.io/)

## Requirements
1. Install **Python 3 pip**:
`sudo apt install python3-pip`

2. Update **pip3** to latest version using:
`sudo pip3 install --upgrade pip`

3. Install RPi.GPIO (it might be already installed):
    `sudo pip3 install RPi.GPIO`

4. Install PyQt5 by running this command:
`sudo apt-get install python-pyqt5`


**Optional**: Using pipenv may not work sometimes. I don't know why.
Install **pipenv**:
`sudo pip3 install pipenv`


## Install steps
1. Download or clone the repository using:
`git clone https://github.com/dd-iuonac/rpi-control-gpio`

2. Go to `rpi-control-gpio` folder:
`cd rpi-control-gpio`

## Run the program
Make sure you are in the `rpi-control-gpio` folder.

Run the software with this command:
    `python3 main.py`
