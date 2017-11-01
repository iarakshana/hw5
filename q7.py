import pandas as pd
import requests
import json
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
# The possible variables come from here:
# https://api.census.gov/data/2015/acs5/profile/variables.html
def get_chicago_census_data(variable):

  # Illinois is 17 and Cook County is 17.
  api_base = "https://api.census.gov/data/2015/acs5/profile?for=tract:*&in=state:17+county:31&get=NAME,"
  return requests.get(api_base + variable).json()

## You could change the variables here...
census_hs = get_chicago_census_data("DP02_0056E") #DP02_0056E is
#"SCHOOL ENROLLMENT!!Population 3 years and over enrolled in school!!High school (grades 9-12)"
census_hs = pd.DataFrame(data = census_hs[1:], columns = census_hs[0])
census_hs
census_hs["tract"] = census_hs.tract.astype(int)/100
census_hs.rename(columns = {"tract" : "Census Tract"}, inplace = True)
census_hs.set_index("Census Tract", inplace = True)
census_hs["DP02_0056E"] = census_hs["DP02_0056E"].astype(int)

sdf = pd.read_csv("chicago_schools.csv", index_col = "Census Tract")


sdf =  sdf[["PARCC Proficiency (%)", "ISBE_ID"]]

sdf




df1 = pd.DataFrame(data=census_hs, columns=['DP02_0056E'])
#df1
df2 = pd.DataFrame(data=sdf, columns=['PARCC Proficiency (%)'])
df2

q7 = df1.join(df2)

q7.plot(kind = "scatter", x = "DP02_0056E", y = "PARCC Proficiency (%)", alpha = 0.20, s = 10, color = "darkred")
q7.scatter.savefig("q7.pdf")
