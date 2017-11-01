#!/usr/bin/env python

# You can simply write your final solution as a comment.

import pandas as pd

# Solution should hold a tuple containing the median value
# of college ready (%) for public and charters:

#For Charter Schools
df = pd.read_csv("chicago_schools.csv", index_col = "Zip")

df = df[["ISBE_ID","College Ready (%)", "PARCC Proficiency (%)", "Low Income (%)" ]]
charter = df[df["ISBE_ID"].str.contains("C")]
charter.dropna(inplace = True)
charter_CR = charter["College Ready (%)"].median()
#for answers in the SOLUTIONS page
charter_P = charter["PARCC Proficiency (%)"].median()
charter_LI = charter["Low Income (%)"].median()
#For Public Schools

public = df[~df["ISBE_ID"].str.contains("C")] # the tilde reverses the condition so showing
#all without a C in the ISBE_ID
public_CR = public["College Ready (%)"].median()
public_CR

public_CR, charter_CR = 5.2, 13.3
solution = (public_CR, charter_CR)
print(solution)
