import os
from six.moves import urllib
import tempfile

import numpy as np
import pandas as pd
import tensorflow as tf

### For downloading data  ###

# Storage directory
DATA_DIR = os.path.join(tempfile.gettempdir(), 'TBP_data')

DATA_URL = 'https://github.com/gen740/Jyouho-alpha/tree/master/TBP_sim/build/data_for_learning'
TRAINING_FILE = 'initial_value.csv'
EVAL_FILE = 'forward_step_data.csv'
TRAINING_URL = '%s/%s' % (DATA_URL, TRAINING_FILE)
EVAL_URL = '%s/%s' % (DATA_URL, EVAL_FILE)

### For interpreting data ###

# Data imformation

### Hyperparameter for training ###

BATCH_SIZE = 128
NUM_EPOCHS = 20
LEARNING_RATE = 0.001

def _download_and_clean_file(filename, url):
  """Downloads data from url, and makes changes to match the CSV format.

  The CSVs may use spaces after the comma delimters (non-standard) or include
  rows which do not represent well-formed examples. This function strips out
  some of these problems.

  Args:
    filename: filename to save url to
    url: URL of resource to download
  """
  temp_file, _ = urllib.request.urlretrieve(url)
  with tf.io.gfile.open(temp_file, 'r') as temp_file_object:
    with tf.io.gfile.open(filename, 'w') as file_object:
      for line in temp_file_object:
        line = line.strip()
        line = line.replace(', ', ',')
        line = line.replace(' ', ',')
        if not line or ',' not in line:
          continue
        if line[-1] == '.':
          line = line[:-1]
        line += '\n'
        file_object.write(line)
  tf.io.gfile.remove(temp_file)

def download(data_dir):
  """Downloads census data if it is not already present.

  Args:
    data_dir: directory where we will access/save the census data
  """
  tf.io.gfile.makedirs(data_dir)

  training_file_path = os.path.join(data_dir, TRAINING_FILE)
  if not tf.io.gfile.exists(training_file_path):
    _download_and_clean_file(training_file_path, TRAINING_URL)

  eval_file_path = os.path.join(data_dir, EVAL_FILE)
  if not tf.io.gfile.exists(eval_file_path):
    _download_and_clean_file(eval_file_path, EVAL_URL)

  return training_file_path, eval_file_path
