from distutils.core import setup
import py2exe
import sip
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import pprint
import pyperclip
from gui.ping_gui_v3 import Ui_ServerPing

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "twitchservercheck.py"}],
    zipfile = None,
)
