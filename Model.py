import numpy
import pandas
import random
import shutil
import os

import tensorflow
from tensorflow import keras
from keras import layers

for (_, _, image) in os.walk("LabelledPokemon", topdown=True):
   print(image)
