import pandas as pd

file = "Users.xlsx"

# Read the file
df = pd.read_excel(file)

# Get the column names
cols = df.columns

for row in df.itertuples():
    # Get the values
    values = row[1:]
    # Create the dictionary
    d = dict(zip(cols, values))



