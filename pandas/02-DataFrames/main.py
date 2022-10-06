# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

import pandas as pd

data = {
        "calories": [120, 450, 300],
        "duration": [20, 60, 45]
        }

df = pd.DataFrame(data)

# refer to the row index:
print(df)
print("=============================")

# Use the named index in the loc attribute to return the specified row(s).
print(df.loc[[0,1]])
