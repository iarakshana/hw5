#!/usr/bin/env python

import pandas as pd

# solution should hold the final answer
df = pd.read_csv("chicago_crime.csv", index_col = "ID")
df.dropna(inplace = True)
df.groupby('Ward')['Arrest'].sum().sort_values(ascending = False)

solution = 28 # Ward with most crime.
print(solution)
