import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset/forestfires.csv', delimiter=',')
numbers = ['X','Y','FFMC','DMC','DC','ISI','temp','RH','wind','rain','area']
cat = ['month','day']

# print(data[cat].describe())

cat_columns = data.select_dtypes(['object']).columns
print(cat_columns.to_list())
#convert all categorical columns to numeric
t = data[cat_columns].apply ( lambda x: pd.factorize (x)[ 0 ])

#view updated DataFrame



# X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain,area
# 'X',
# 'Y',
# 'FFMC',
# 'DMC',
# 'DC',
# 'ISI',
# 'temp',
# 'RH',
# 'wind',
# 'rain',
# 'area',

# 'month',
# 'day',

# 
# X
# Y
# month
# day
# FFMC
# DMC
# DC
# ISI
# temp
# RH
# wind
# rain
# area