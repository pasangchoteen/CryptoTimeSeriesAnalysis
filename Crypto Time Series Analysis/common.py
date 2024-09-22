# common.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

def load_data(file_path):
    """Load cryptocurrency data from a CSV file."""
    date_format = '%m/%d/%y'  # Date format for parsing
    data = pd.read_csv(file_path, index_col=[1], parse_dates=[1],
                       date_parser=lambda x: pd.to_datetime(x, format=date_format))
    return data

def plot_data(data, title='Data Plot'):
    """Plot the given time series data."""
    plt.figure(figsize=(12, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

def calculate_error(actual, predicted):
    """Calculate RMSE between actual and predicted values."""
    return np.sqrt(mean_squared_error(actual, predicted))

def differenced_data(data):
    """Perform differencing on the data to make it stationary."""
    return data.diff().dropna()

def train_test_split(data, train_ratio=0.8):
    """Split the data into training and testing sets."""
    train_size = int(len(data) * train_ratio)
    return data[:train_size], data[train_size:]

def fit_arima_model(train_data, order):
    """Fit ARIMA model on training data and return the fitted model."""
    model = ARIMA(train_data, order=order)
    model_fit = model.fit()
    return model_fit

def forecast_values(model_fit, steps):
    """Forecast future values using the fitted ARIMA model."""
    return model_fit.forecast(steps=steps)

def inverse_differencing(last_actual_value, diff_forecast):
    """Inverse the differencing to obtain actual forecasted values."""
    return last_actual_value + diff_forecast.cumsum()

def automate_arima(data, p_values, d_values, q_values):
    """Automate the ARIMA order selection process using AIC as the criterion."""
    best_aic = np.inf
    best_order = None
    best_model = None
    
    for p in p_values:
        for d in d_values:
            for q in q_values:
                try:
                    order = (p, d, q)
                    diff_data = differenced_data(data)
                    diff_train, _ = train_test_split(diff_data)
                    
                    model_fit = fit_arima_model(diff_train, order)
                    aic = model_fit.aic
                    
                    if aic < best_aic:
                        best_aic = aic
                        best_order = order
                        best_model = model_fit
                        
                except Exception as e:
                    continue
                    
    return best_order, best_model

def inverse_transformation(scaler, data):
    """Inverse the transformation to get actual values."""
    return scaler.inverse_transform(data.reshape(-1, 1))

def perform_adf_test(data):
    """Perform Augmented Dickey-Fuller test for stationarity."""
    result = adfuller(data)
    return result[0], result[1]  # Return ADF statistic and p-value

# Function for feature engineering
def feature_engineering(data):
    """Create lag features and rolling statistics."""
    data['lag1'] = data['Close'].shift(1)
    data['lag2'] = data['Close'].shift(2)
    data['lag3'] = data['Close'].shift(3)
    data['MA3'] = data['Close'].rolling(window=3).mean()
    data['MA4'] = data['Close'].rolling(window=4).mean()
    data['MA5'] = data['Close'].rolling(window=5).mean()
    data['max_3'] = data['Close'].rolling(window=3).max()
    data['day'] = data.index.day
    data['month'] = data.index.month
    data['year'] = data.index.year
    data['day_of_week'] = data.index.dayofweek
    data['quarter'] = data.index.quarter
    return data.dropna()

def preprocess_data(data, scaler):
    """Normalize or standardize the data and return it with the same index."""
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1)).flatten()
    return pd.DataFrame(scaled_data, index=data.index, columns=[scaler.__class__.__name__ + ' Close'])