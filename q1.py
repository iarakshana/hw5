#!/usr/bin/env python

import pandas as pd
df = pd.read_csv("chicago_crime.csv", index_col = "ID")
df.dropna(inplace = True)

df.groupby('Primary Type')['Arrest'].mean().sort_values(ascending = False)
# solution should hold the final answer

solution = "PUBLIC INDECENCY"
print(solution)
