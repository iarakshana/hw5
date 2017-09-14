#!/usr/bin/env python 

import pandas as pd
import requests

# The possible variables come from here:
# https://api.census.gov/data/2015/acs5/profile/variables.html
def get_chicago_census_data(variable):
  
  # Illinois is 17 and Cook County is 17.
  api_base = "https://api.census.gov/data/2015/acs5/profile?for=tract:*&in=state:17+county:31&get=NAME,"
  return requests.get(api_base + variable).json()

## You could change the variables here...
census_resp = get_chicago_census_data("DP03_0119PE")

# Merge the Cesnsus and school datasets.
# Plot their scatterplot and save q7.pdf.

