## Raspberry Pi 3 G.P.I.O. Control
This is a tool for controlling Raspberry Pi 3 G.P.I.O.

It has been written in [Python 3] (https://www.python.org/) using [PyQt 5.12](https://www.riverbankcomputing.com/static/Docs/PyQt5/), the python variant for [Qt 5 Framework] (https://www.qt.io/)

## Requirements
Install and Update the pip3 to latest version using:
`sudo apt install python3-pip`
`sudo pip3 install --upgrade pip`

Install pipenv:
`sudo pip3 install pipenv`


## Install steps
1. Download or clone the repository using:
`git clone https://github.com/dd-iuonac/rpi-control-gpio`

2. Go to `rpi-control-gpio` folder:
`cd rpi-control-gpio`

3. Install dependencies using pipenv:
`pipenv install`

## Run the program
Make sure you are in the `rpi-control-gpio` folder.
Activate the virtual environment by running this command in terminal:
`pipenv shell`

Now run the script: `python main.py`