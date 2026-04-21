from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def train_model(df):
    X = df[['Average Speed', 'Congestion Level']]
    y = df['Traffic Volume']

    df['Congestion Level'] = df['Congestion Level'].map({
    'Low': 1,
    'Medium': 2,
    'High': 3
})

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeRegressor(max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    score = r2_score(y_test, y_pred)

    print("Model Accuracy (R2 Score):", score)

    return model
  