import os
import sys


root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
os.chdir(root)

print("Update is disabled")
from launch_update import *
