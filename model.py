import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_sales(data):
    df = pd.DataFrame(data, columns=["id", "product", "quantity", "price", "date"])
    
    if len(df) < 2:
        return "Not enough data"
    
    df["day"] = range(1, len(df)+1)
    
    X = df[["day"]]
    y = df["quantity"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    next_day = [[len(df) + 1]]
    prediction = model.predict(next_day)
    
    return round(prediction[0], 2)