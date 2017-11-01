#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
bls = pd.read_csv("bls_unemployment.csv", index_col = "Date", parse_dates = ['Date'])


ax = bls["New York"].plot()
ax = bls["Philadelphia"].plot()
ax = bls["Houston"].plot()
ax = bls["Chicago"].plot()
ax = bls["Los Angeles"].plot()

ax.set_xlabel("Years")
ax.set_ylabel("Unemployment Rate")
ax.legend(labels = ["New York", "Philadelphia", "Houston", "Chicago", "Los Angeles"])
ax.figure.savefig("q6.pdf")

# Load bls_unemployment and plot it
# Save the time series as q6.pdf
