#!/usr/bin/env python

import pandas as pd
df = pd.read_csv("chicago_crime.csv", index_col = "ID")
df_q0 = df[["Primary Type", "Arrest"]]
df_q0.head(5)

df.groupby('Primary Type')['Arrest'].count().sort_values(ascending = False)
# solution should hold the final answer

solution = "THEFT"
print(solution)
