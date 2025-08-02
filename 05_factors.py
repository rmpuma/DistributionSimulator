import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import importlib

# import our own files and reload
import capm
importlib.reload(capm)

# inputs
security = 'MRK'
factors = ['^SPX','IVW','IVE','QUAL','MTUM','SIZE','USMV',\
           'XLK','XLF','XLV','XLP','XLY','XLI','XLC','XLU']

# compute factors

df = capm.dataframe_factors(security, factors)
