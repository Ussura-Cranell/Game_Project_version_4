import os
script_path = os.path.realpath(__file__)
script_directory = os.path.dirname(script_path)
os.chdir(script_directory)

from src.Game import Starting
input('Start game...')