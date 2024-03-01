import pandas as pd

class Data:

    def __init__(self, country: str , skiprows: int = 3) -> None:
        self.skiprows = skiprows
        self.country = country
    
    def make_filepath(country: str) -> str:
        filepath = "../data/"+ country + "_data.csv"
        return filepath

    def read(filepath: str, skiprows: int=3) -> pd.core.frame.DataFrame:
        data = pd.read_csv(filepath,skiprows=skiprows)
        return data
    
    def clean_data(df: pd.core.frame.DataFrame, columns_to_drop: list) -> pd.core.frame.DataFrame:
        df = df.drop(columns_to_drop, axis = 1)
        df = df.T.reset_index()
        df.columns = df.iloc[0]
        df = df[1:]
        df = df.rename(columns={"Indicator Name":"Year"})
        df = df[:-1].convert_dtypes()
        return df