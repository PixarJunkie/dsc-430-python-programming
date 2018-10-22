import pandas as pd 
import numpy as np

def mean_column(): 
    df = pd.read_csv('avocado.csv')
    tot_volume = df[['Total Volume']]
    return np.mean(tot_volume)

def 
