import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Remove missing values
    df = df.dropna()

    # Standardize column names (remove spaces)
    df.columns = df.columns.str.strip()

    return df