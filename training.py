"""
ML training demonstration
"""
import pandas as pd
import numpy as np
from sklearn import linear_model

## Import CSV
path = "data/kc_house_data.csv"
df = pd.read_csv(path, parse_dates=True, infer_datetime_format=True)

## Preprocessing
print(df.columns) # Print columns for clarity

y = df["price"] # Assign target to y; price
print(f"Shape of y: {str(y.shape)}")

X = df.drop(labels=["price"], axis=1) # Assign features to X
print(f"Shape of X: {str(X.shape)}")

## Remove non-numerical features; in future they might be used
cols_to_remove = []

for col in X.columns:
    try:
        _ = X[col].astype(float)
    except ValueError:
        print('Couldn\'t covert %s to float' % X)
        cols_to_remove.append(col)
        pass

X = X[[col for col in X.columns if col not in cols_to_remove]]

print(X.columns) # Double check outcome 

## ML 
reg = linear_model.LinearRegression() # Instantiate an sklearn multivariate linear regression model
reg.fit(X, y) # Fit on data
print(reg.coef_) # Print coefficients

predict_data = np.array([[0, 2, 1, 667, 0, 1, 0, 0, 5, 5, 0, 0, 1970, 2006, 0, 0, 0, 0, 0]]) # Give bullshit data

print(reg.predict(predict_data)) # Check bullshit answer