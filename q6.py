#!/usr/bin/env python 

import pandas as pd


################
################
## THIS IS ALL COPIED FROM CLASS.

import requests

def get_census_data(variables = [], state = "", county = "*"):

  census_url = "http://api.census.gov/data/2014/acs5?for=tract:*&in=state:{}+county:{}&get=NAME,{}"
  addr = census_url.format(state, county, ",".join(variables))

  return requests.get(addr).json()

## You could change the variables here...
variables = ["B16010_041E", "B16010_001E", "B06012_002E", "B06012_001E"]
census_resp = get_census_data(state = 17, county = 31, variables = variables)

census_df = pd.DataFrame(data = census_resp[1:], columns = census_resp[0])

census_df["Census Tract"] = census_df["tract"].astype(int)/100.
census_df.set_index("Census Tract", inplace = True)

for v in variables: census_df[v] = census_df[v].astype(int)
census_df["Percent Bachelor's"] = census_df["B16010_041E"] / census_df["B16010_001E"]
census_df["Percent Poverty"]    = census_df["B06012_002E"] / census_df["B06012_001E"]
census_df = census_df[["Percent Bachelor's", "Percent Poverty"]]


# This also...

df_sch_import = pd.read_csv("chicago_schools.csv", index_col = "ISBE_ID")
df_sch_import = df_sch_import[["Name", "PARCC Proficiency (%)", "Grades"]]

df_sch_geocode = pd.read_csv("school_address_geocoded.csv", index_col = "ISBE_ID", usecols = ["ISBE_ID", "CensusTract"])
df_sch_geocode = df_sch_geocode[["CensusTract"]]
df_sch_geocode.rename(columns = {"CensusTract" : "Census Tract"}, inplace = True)

df_sch_geocode

df_sch_merged = df_sch_import.join(df_sch_geocode)
df_sch_merged.dropna(inplace = True)
df_sch_merged.set_index("Census Tract", inplace = True)


############
############
### NOW USE THOSE DATASETS TO MAKE A SCATTER PLOT

census_schools = df_sch_merged.join(census_df)

ax = census_schools.plot(kind = "scatter", x = "PARCC Proficiency (%)", y = "Percent Poverty")
ax.get_figure().savefig('q6.pdf', bbox_inches='tight')

