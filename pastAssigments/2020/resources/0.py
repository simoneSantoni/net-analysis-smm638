# %% libraries
import os
import glob
import json
import pandas as pd
from pandas import json_normalize

# %% working directory
wd = os.chdir('/tmp')

# %% read data
in_files = glob.glob(os.path.join('.', '*.json'))

data = json.load(open(in_files[0]))

data = [json.loads(line) for line in open('rb_hp_chart.json')]



# %%