import pandas as pd

# This is to ensure that the csc file is clean
lines = []
with open(r"../data/us_data.csv", 'r') as fp:
    lines = fp.readlines()

if lines[0][1:15]!='"Country Name"':
    with open(r"../data/us_data.csv", 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [0, 7]:
                fp.write(line)

#read data
us_data = pd.read_csv('../data/us_data.csv')
us_data=us_data.loc[:,'Indicator Name':'2022'].drop('Indicator Code',axis=1)
us_data=us_data.rename(columns={"Indicator Name":"Year"}).T

# Transforming the header
new_header = us_data.iloc[0] #grab the first row for the header
us_data = us_data[1:] #take the data less the header row
us_data.columns = new_header #set the header row as the df header

# Reset indices
us_data.reset_index(inplace=True)

# Workaround for naming columns and indices right
us_data.rename(columns={'index':'Year'},inplace=True)
us_data = us_data.rename_axis(None, axis=1)
us_data