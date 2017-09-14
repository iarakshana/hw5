# Homework 5: Pandas and Primes

The homework focusses on Pandas, but maintains some level of 'basic python' work.

You may accept the assignment [here](https://classroom.github.com/assignment-invitations/829adc8487082580d8510e309105e51b).

It is due Wednesday November 1 at 1:30am.

## Pandas

### Downloading some data.

Download some data about crime in Chicago.

* Go to the data portal for the [City of Chicago](https://data.cityofchicago.org/), and navigate to "Crimes - 2001 to present"
  * You can find it here: https://data.cityofchicago.org/view/5cd6-ry5g
* We'll look at the last four full years of data, 2013-2016.  Highlight it as shown in the picture below.
* Now click on "Export." Then under "Rows as CSV," select "Current Filter (1,112,989 rows)".  (Don't worry if it goes up by a few, before the assignment is over: incidents occasionally get added.)  Then "Download" (see second picture).  It's about 250 MB, so ... wait!
* If this whole data grab is not working, just click this [link](https://data.cityofchicago.org/api/views/6zsd-86xi/rows.csv?accessType=DOWNLOAD&bom=true&query=select+*+where+%60date%60+%3E%3D+%272013-01-01T00%3A00%3A00%27+AND+%60date%60+%3C+%272017-01-01T00%3A00%3A00%27).
* Move this file to your homework directory, naming it as you like (I call mine `chicago_crime.csv`).
* DO NOT, along the way, open this file in Microsoft Excel and save it.  It will change how the lines are ended (return/enter) in the file, and make it stop working for you.  Do NOT, later on, commit this file to your GitHub repo -- it's way too big, and we don't need it.

Next week, we'll start playing with accessing these resources programmatically.

<details><summary>Pictures for Chicago Data Export</summary>
<img src="img/select-2013-2016.png" width=725px> <img src="img/export-filtered.png" width=725px>
</details>

### Exercises

As usual, there are "skeletons" in place for you.  Please fill these in.

0. Which primary type of crime resulted in the most arrests?  Use `df.groupby(..).count(..)`.
1. Which primary type most reliably (fractionally) resulted in an arrest? Use `df.groupby(..).mean()`.
2. Which ward saw the most crime of any type?
3. Plot (histogram) the hourly crime rate for the full city, as a function of day in a week.  Your plot should have one bin for every hour in a week, from midnight Monday morning, till Sunday night.  Save it as `q3.pdf`
   * Because there are over a million date strings to interpret, this will be somewhat slow to load.
   * You will want to check out [pandas.Series.dt.dayofweek](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.dayofweek.html) and  [pandas.Series.dt.hour](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.hour.html).
   * Remember that you must use reasonable labels for your x and x axes.  Since there is a single field plotted, you don't need a legend.  Check out the [matplotlib axes API](https://matplotlib.org/api/axes_api.html#axis-labels-title-and-legend) if you're stuck.
   * The magic incantation for saving is `ax.get_figure().savefig('q3.pdf')`.
4. Perform a regression with y = homicides per ward and x = weapons violations per ward.  What is the slope?  What is its error?  Use [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html).
   * N.B., you may find that not all wards have crimes or homicides, when you count by ward.  If so, you may need to use `fillna(0, inplace = True)` to specify that there weren't any.  Make sure you have 50 wards!
5. Do the same thing using `statsmodels.api.ols`.  They had better agree!
6. Use the school data from class (in this directory), compare public schools with charters (they have a "C" in their ID).
   Drop the schools that are missing data at the end (do `df.dropna(inplace = True)` on the whole frame).
   How do the charters do?  Compare the median college ready (%).
   (Is this an apples to apples comparison -- do public and charters serve comparable fractions of low income students?
    That is not part of the solution, but you should check!)
7. Visit the list of [variables](https://api.census.gov/data/2015/acs5/profile/variables.html) from the 2015 American Community Survey 5-year estimates.
   Use the function below (in your skeleton) to retrieve a json response for a single variable of your choice.  Be careful not to hammer the API (you could get locked out, though not permanently).
   It's good practice to cache the result in a csv or something, and only update it when you change something.
   Merge that data with the school estimates, using the Census Tract as a key.
   
   Make a scatter plot with one point for each school, showing the school's PPARC Proficiency against the variable that you have chosen, at the tract level.  You can use either matplotlib or seaborn.  Save it as `q7.pdf`.  (Label your axes!)
   ```python
   import requests
   def get_chicago_census_data(variable):

       api_base = "https://api.census.gov/data/2015/acs5/profile?for=tract:*&in=state:17+county:31&get=NAME,"
       return requests.get(api_base + variable).json()
   ```
8. Plot and save (`q8.pdf`) the unemployment rates for the five largest cities in the US, from the BLS file provided.

Please fill in solutions as you go.  Each question should go in one of the provided files.
I would suggest doing your exploration in jupyter, first, and then copying the small code over.

## Python

Also complete the python problem below.  It will count for 30% of the assignment.

Circular primes have the property that all rotations of their digits are also prime numbers.  For instance, 19937, 37199, 71993, 93719, 99371, are all circular primes.  Below 100, there are thirteen such primes: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.  How many circular primes are there below one million?

You should start by figuring out 'the' efficient algorithm for calculating a list of primes.
(Hint from lectures: [Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).)

There are then two methods: you can either move digits around by place value, with mods and integer division by 10,
  or you can treat your primes as strings move parts around by slicing.

This should be _very_ fast.  (Second hint: when making your list of candidate circular primes, with the sieve, what property of circular primes can you exploit to dramatically reduce the size of that list.)

The assignment is due October 26 at 1:30am.

