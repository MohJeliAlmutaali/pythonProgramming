# load data of csv

import pandas as pd


# use max_row method to determine the maximum row
pd.options.display.max_rows = 30

df = pd.read_csv('data.csv')


# method is named to_string for display all data.
# if you don't use that method, only the the first and last 5 lines

print(df)