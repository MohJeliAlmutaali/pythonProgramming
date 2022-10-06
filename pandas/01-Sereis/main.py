# A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type

# seri pandas seperti kolom didalam table
# Seri adalah array satu dimensi

import pandas as pd

# list form
a = [1,9,4]

myvar = pd.Series(a, index = ["x", "y", "x"])
print("List form")
print(myvar)

# Dictionary from
calories = {"day1": 250, "day2": 200, "day3": 300}
myvar = pd.Series(calories)
print("Dictionary form")
print(myvar)
