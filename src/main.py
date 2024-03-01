import pandas as pd
from data_methods import Data

filepath = Data.make_filepath("us")
us_data = Data.read(filepath)

# cleaning the data
us_columns_to_drop = ["Country Name", "Country Code", "Indicator Code"]
us_data = Data.clean_data(us_data, us_columns_to_drop)

# selecting and modifying the data
us_data["Year"] = us_data["Year"].astype(int)
us_data = us_data.tail(30)

# checking the number of null values in each column
us_data.isna().sum()

# sorting the data according to no of null values in every column, in ascending order
sorted_cols = us_data.isna().sum().to_dict()
sorted(sorted_cols.items(), key=lambda x: x[1])

# selecting the columns we want to analyse
selected_us_data = us_data[
    [
        "Year",
        "GDP growth (annual %)",
        "GDP per capita (current US$)",
        "Foreign direct investment, net outflows (BoP, current US$)",
        "Inflation, consumer prices (annual %)",
        "Unemployment, total (% of total labor force) (national estimate)",
        "Population growth (annual %)",
        "Taxes on income, profits and capital gains (current LCU)",
    ]
]
print(selected_us_data)
