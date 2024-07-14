import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
#from shape.geometry import Point,Polygen

data=pd.read_csv('Tweets.csv')
data.head()
data.shape

data.isnull().any()
data['airline'].value_counts()



