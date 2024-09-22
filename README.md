# Crypto Time Series Analysis

## Introduction
Welcome to the Crypto Time Series Analysis repository! This project focuses on analyzing Bitcoin (BTC) closing prices to identify trends and forecast future movements. By leveraging feature engineering and various predictive models, including ARIMA and Random Forest Regressor, this analysis aims to evaluate the performance of different forecasting techniques, providing actionable insights for investors and traders.

**_Disclaimer_**: _All datasets and analyses are for educational purposes only and do not represent any financial advice._

## Data Sources
**BTC Data**: The primary dataset used for this analysis is the "BTC.csv" file, which contains historical data on Bitcoin closing prices.

## Tools
## Tools
- **Python**: Utilized for data manipulation, statistical modeling, and visualizations.
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `sklearn`, `statsmodels`

## Data Cleaning/Processing
The dataset focuses solely on the closing prices of Bitcoin. Other columns such as open, high, and low prices have been ignored for this analysis. The data was cleaned and processed to handle missing values and outliers. Key steps included:
- Sorting the data by date and ensuring it has a daily frequency.
- Forward filling missing values to maintain continuity.
- Performing differencing to achieve stationarity for time series analysis.

## Problem Statement
1. How can we effectively forecast Bitcoin closing prices using historical data?
2. What impact does feature engineering have on model performance?
3. Which forecasting model provides the best accuracy in predicting future prices?
4. How do various time series models compare in terms of their predictive capabilities?

## Exploratory Data Analysis
Exploratory Data Analysis (EDA) involved visualizing trends in the Bitcoin closing prices, identifying patterns, and understanding the relationships between engineered features and the target variable.

### Key Findings from EDA:
- **Trend Identification**: 
  - Significant price increase from early 2020 to late 2021.
  - Sharp decline observed in the first half of 2022.
  
- **Volatility Analysis**: 
  - High volatility during 2020-2021 due to global market uncertainties.
  - Fluctuations exceeded 50%, with another volatile phase in early 2022.

- **Seasonality**: 
  - Higher price movements consistently noted in Q4 (October to December) across multiple years.

- **Stationarity**: 
  - ADF test showed the time series is non-stationary. Differencing was applied to achieve stationarity for modeling.

## Skills/Concepts Demonstrated
### Python Features Utilized:
1. Data manipulation with Pandas
2. Time series analysis techniques
3. Model evaluation metrics
4. Data visualization with Matplotlib and Seaborn

### Data Analysis Tools/Techniques:
1. Feature Engineering
2. Time Series Forecasting
3. Model Comparison
4. Statistical Analysis

## Model Implementation
### ARIMA Model
- **Fitting Process**: Employed differencing to ensure stationarity and used ADF tests to validate it.
- **Parameter Selection**: Automated ARIMA order selection based on AIC criterion.
- **Multiple Model Execution**: Executed ARIMA models on differenced, standardized, and normalized data to evaluate performance across different preprocessing methods.

### Steps Taken:
1. **Differencing**: The original data was differenced to achieve stationarity.
2. **ADF Test**: The Augmented Dickey-Fuller (ADF) test confirmed that the differenced data was stationary.
3. **ACF and PACF**: The ACF and PACF plots of the original data showed high correlations, indicating the need for differencing.
4. **Model Selection**: Multiple ARIMA models were executed on differenced, standardized, and normalized data, with the best-performing model identified based on RMSE.


#### Results from ARIMA:
- Best ARIMA Order for Differenced Data: **(2, 0, 2)**
  - Root Mean Squared Error (RMSE): **18980.43**
- Best ARIMA Order for Normalized Data: **(3, 0, 4)**
  - RMSE: **20345.67**
- Best ARIMA Order for Standardized Data: **(3, 0, 4)**
  - RMSE: **5281.48**

### Random Forest Regressor
- Implemented feature engineering to create lagged features and rolling statistics.
- Defined the target variable (closing price) and the relevant features.
- Evaluated the model's performance and analyzed feature importance.

#### Results from Random Forest:
- Mean Squared Error: **773219.72**
- Root Mean Squared Error (RMSE): **879.33**
- Top Features: 
  - lag1 (50.27%)
  - MA3 (49.46%)

## Model Comparison
While the ARIMA model provided reasonable forecasts with higher RMSE values, the Random Forest model outperformed in terms of predictive accuracy, making it the recommended choice for this analysis.

The project includes various visualizations to illustrate trends and model performance:

1. **BTC Closing Price**: Shows the historical closing prices of Bitcoin.
   ![](BTCClosingPrice.png)

2. **Differenced Data**: Illustrates the transformation applied to achieve stationarity.
   ![](BTCDifferencedData.png)

3. **ACF of Original Data**: Displays the autocorrelation of the original data, indicating high correlation with past values.
   ![](ACFOriginal.png)

4. **PACF of Original Data**: Shows the partial autocorrelation, supporting the stationarity of the series.
   ![](PacfOriginal.png)

5. **ACF of Differenced Data**: Reflects reduced correlations, confirming stationarity post-differencing.
   ![](AcfDiff.png)

6. **PACF of Differenced Data**: Further supports the findings of the ACF plot for the differenced data.
   ![](PacfDiff.png)

7. **ARIMA Model Forecast**: Compares actual vs. forecasted values using the ARIMA model.
   ![](ARIMADiff.png)

8. **Normalized and Standardized ARIMA Forecasts**: Visual comparison of forecasts from different data transformations.
   ![](ARIMANormStandard.png)

9. **Feature Importance**: Highlights the significance of features used in the Random Forest model.
   ![](FeaturesPlot.png)

## Conclusion
This project successfully analyzed and forecasted Bitcoin closing prices using ARIMA and Random Forest models. The Random Forest model demonstrated superior predictive accuracy, making it the preferred choice for future forecasting tasks.

## Recommendations
1. **Utilize Feature Engineering**: Continue to explore additional features to enhance predictive models.
2. **Monitor Model Performance**: Regularly assess the performance of forecasting models and adjust parameters as needed.
3. **Consider External Factors**: Incorporate market news and events that may impact Bitcoin prices into the analysis for improved forecasting.

## Limitations
The dataset used is limited to closing prices and does not account for other market factors that could influence prices. Future analyses could incorporate additional features for improved modeling.

## References
1. Kaggle
2. Chatgpt
