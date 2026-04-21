from config import DATA_PATH, CLEAN_DATA_PATH

from src.data_cleaning import load_data, clean_data
from src.feature_engineering import create_features
from src.analysis import traffic_by_day, traffic_vs_weather, congestion_analysis
from src.model import train_model

def main():
    print("Loading data...")
    df = load_data(DATA_PATH)

    print("Cleaning data...")
    df = clean_data(df)

    print("Creating features...")
    df = create_features(df)

    print("Saving cleaned data...")
    df.to_csv(CLEAN_DATA_PATH, index=False)

    print("Running analysis...")
    traffic_by_day(df)
    traffic_vs_weather(df)
    congestion_analysis(df)

    print("Training model...")
    model = train_model(df)

    print("✅ Project completed successfully!")

if __name__ == "__main__":
    main()