# Stock Market Analysis Dashboard
## Indian Stock Market (NSE) - Python & Streamlit

A comprehensive stock market analysis dashboard for the Indian stock market (NSE) built with Python, Streamlit, and machine learning.

---

## Features

### Data Acquisition & Pipeline
- Real-time and historical stock data fetching using yfinance
- Robust data cleaning pipeline (handling missing values, outliers)
- Support for 20+ major Indian NSE stocks
- Custom ticker support

### Financial Analytics Engine
- **Technical Indicators**: SMA, EMA, RSI, MACD, Stochastic
- **Volatility Analysis**: Bollinger Bands, Historical Volatility, ATR, Keltner Channels
- **Portfolio Metrics**: Daily Returns, Cumulative Returns, Sharpe Ratio, Sortino Ratio, VaR

### Trend Detection & Prediction
- Linear Regression model for price forecasting
- Random Forest and Gradient Boosting models
- Feature importance analysis
- 5-day price predictions

### Visualization (Streamlit)
- Interactive candlestick charts
- Technical indicator charts
- Risk metrics visualization
- Fundamental analysis panel

---

## Project Structure

```
Stock Market Analysis Dashboard/
├── requirements.txt          # Python dependencies
├── main.py                   # Application entry point
├── README.md                 # This file
├── src/
│   ├── __init__.py
│   ├── data_acquisition.py   # Data fetching module
│   ├── data_cleaning.py      # Data cleaning pipeline
│   ├── technical_indicators.py  # Technical analysis
│   ├── volatility_analysis.py   # Volatility metrics
│   ├── portfolio_metrics.py     # Portfolio calculations
│   └── prediction_model.py      # ML predictions
├── app/
│   ├── __init__.py
│   └── dashboard.py          # Streamlit dashboard
└── docs/
    └── POWERBI_INTEGRATION_GUIDE.md  # PowerBI guide
```

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd "Stock Market Analysis Dashboard"
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Note**: For pandas-ta (optional), you may need to install TA-Lib separately:
```bash
# Download TA-Lib from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
# Then install the .whl file
pip install TA-lib-0.4.28-cp311-cp311-win_amd64.whl
```

Alternatively, use pandas-ta which is pure Python:
```bash
pip install pandas-ta
```

---

## Usage

### Running the Dashboard

**Option 1: Using main.py**
```bash
python main.py
```

**Option 2: Using Streamlit**
```bash
streamlit run app/dashboard.py
```

**Option 3: Using Streamlit with custom port**
```bash
streamlit run app/dashboard.py --server.port 8501
```

### Dashboard Controls

1. **Sidebar Options**:
   - Select from 20+ Indian stocks (RELIANCE, TCS, INFY, etc.)
   - Choose custom ticker (e.g., "RELIANCE.NS")
   - Select time period (1mo, 3mo, 6mo, 1y, 2y, 5y, 10y)
   - Toggle technical indicators, volatility, predictions, fundamentals

2. **Main Dashboard**:
   - Market Overview with KPIs
   - Interactive price charts with overlays
   - Technical indicator panels (RSI, MACD, Stochastic)
   - Volatility analysis (Bollinger Bands, Historical Volatility)
   - Price predictions with ML models
   - Fundamental analysis
   - Data export (CSV/Parquet)

---

## PowerBI Integration

### Step 1: Export Data
1. In the dashboard, select your stock
2. Click "Download as CSV" or "Download as Parquet"
3. Save to your preferred location

### Step 2: Import to PowerBI
1. Open PowerBI Desktop
2. Get Data > File > Parquet/CSV
3. Navigate to the exported file
4. Click Load

### Step 3: Create DAX Measures
See [`docs/POWERBI_INTEGRATION_GUIDE.md`](docs/POWERBI_INTEGRATION_GUIDE.md) for:
- Complete DAX measures list
- Dashboard layout design
- Three main views (Market Overview, Ticker Deep-Dive, Risk Assessment)

---

## Supported Stocks

### NSE Stocks (Pre-configured)
- RELIANCE, TCS, INFY, HDFCBANK, ICICIBANK
- SBIN, BAJFINANCE, ADANIPORTS, ASIANPAINT, AXISBANK
- HINDUNILVR, LT, MARUTI, SUNPHARMA, TITAN
- WIPRO, NESTLEIND, POWERGRID, NTPC, ONGC

### Custom Tickers
You can also enter any valid NSE ticker (e.g., "CIPLA.NS", "BHARTIARTL.NS")

---

## API Reference

### Data Acquisition
```python
from src.data_acquisition import StockDataFetcher

fetcher = StockDataFetcher()
data = fetcher.fetch_historical_data('RELIANCE', period='1y')
quote = fetcher.fetch_realtime_quote('RELIANCE')
info = fetcher.get_stock_info('RELIANCE')
```

### Data Cleaning
```python
from src.data_cleaning import DataCleaner

cleaner = DataCleaner()
cleaned_data = cleaner.full_cleaning_pipeline(data)
```

### Technical Indicators
```python
from src.technical_indicators import TechnicalIndicators

ti = TechnicalIndicators()
data_with_indicators = ti.calculate_all_indicators(df)
```

### Volatility Analysis
```python
from src.volatility_analysis import VolatilityAnalyzer

va = VolatilityAnalyzer()
data_with_volatility = va.calculate_all_volatility_metrics(df)
```

### Portfolio Metrics
```python
from src.portfolio_metrics import PortfolioMetrics

pm = PortfolioMetrics(risk_free_rate=0.07)
data_with_metrics = pm.calculate_all_metrics(df)
stats = pm.calculate_portfolio_statistics(df)
```

### Predictions
```python
from src.prediction_model import StockPricePredictor

predictor = StockPricePredictor()
result = predictor.train_and_evaluate(df, model_type='linear_regression')
```

---

## Configuration

### Risk-Free Rate
Default: 7% (Indian 10-year Government Bond Yield)
Modify in [`src/portfolio_metrics.py`](src/portfolio_metrics.py):
```python
pm = PortfolioMetrics(risk_free_rate=0.07)  # Change as needed
```

### Technical Indicator Parameters
Modify in [`src/technical_indicators.py`](src/technical_indicators.py):
- RSI Period: 14 (default)
- MACD: 12, 26, 9
- Bollinger Bands: 20 periods, 2 std dev

---

## Troubleshooting

### Common Issues

1. **No Data Available**
   - Check internet connection
   - Verify ticker symbol is correct
   - Try different date range

2. **Import Errors**
   - Ensure all dependencies are installed
   - Check Python version (3.8+ recommended)

3. **Streamlit Errors**
   - Clear cache: `streamlit cache clear`
   - Restart the application

### Getting Help
- Check the documentation in [`docs/POWERBI_INTEGRATION_GUIDE.md`](docs/POWERBI_INTEGRATION_GUIDE.md)
- Review source code comments

---

## License

This project is for educational purposes. Stock data is provided by Yahoo Finance and should not be used for actual trading decisions.

---

## Author

Quantitative Developer

---

## Version

1.0.0
