import pandas as pd

def create_features(df):
    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract features
    df['day'] = df['Date'].dt.day_name()
    df['month'] = df['Date'].dt.month

    return df