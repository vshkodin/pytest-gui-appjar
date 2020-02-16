from lib.tools.GUI import run_GUI
from config import GUI
import os

if GUI: run_GUI() # run GUI
else: os.system('pytest ') # run all without GUI