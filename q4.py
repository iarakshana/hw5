#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import linregress
df = pd.read_csv("chicago_crime.csv", index_col = "ID")
df
is_wv = df['Primary Type'] == 'WEAPONS VIOLATION'
wv = df[is_wv]
wv_x = wv.groupby("Ward")["Primary Type"].count()

is_homi = df['Primary Type'] == 'HOMICIDE'
homi = df[is_homi]
homi_y = homi.groupby("Ward")["Primary Type"].count()

df1 = pd.DataFrame(data=wv_x, columns=['Primary Type'])
df2 = pd.DataFrame(data=homi_y, columns=['Primary Type'])

dff = pd.merge(df1, df2, left_index=True, right_index=True, how = "outer")
dff.fillna(0, inplace = True)
scipy.stats.linregress(dff["Primary Type_x"], dff["Primary Type_y"])

slope, error = 0.15414607481107656, 0.005762170019072632
solution = (slope, error)
print(solution)
