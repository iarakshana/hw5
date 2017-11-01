#!/usr/bin/env python
import pandas as pd
%matplotlib inline
df = pd.read_csv("chicago_crime.csv",
                 index_col = 'Date', parse_dates = ['Date'])
df['Date'] = pd.to_datetime(df['Date'])

df.index = df['date']

#couldn't really do this q - was not sure how to create the 168 bins by the groupby function and then creat the histogram from plot
# Print out q3.pdf
