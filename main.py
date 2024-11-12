from datetime import datetime

# Function to get and validate the stock symbol
def get_symbol():
    symbol = input("Enter stock symbol (1-7 letters, pleas make sure it is in all capsd): ")
    if not symbol.isalpha() or len(symbol) < 1 or len(symbol) > 7 or not symbol.isupper():
        raise ValueError("Symbol must be 1-7 alphabetic characters, pleas make sure it is in all caps")
    return symbol

# Function to get and validate the chart type (either 1 or 2)
def get_chart_type():
    chart_type = input("Enter chart type (1 or 2): ")
    if chart_type not in ['1', '2']:
        raise ValueError("Chart type must be '1' or '2'.")
    return chart_type

# Function to get and validate the time series (between 1 and 4)
def get_time_series():
    time_series = input("Enter time series (1-4): ")
    if time_series not in ['1', '2', '3', '4']:
        raise ValueError("Time series must be 1-4.")
    return time_series


def get_start_date():
    start_date = input("Enter start date (MM-DD-YYYY): ")
    try:
        datetime.strptime(start_date, "%m-%d-%Y")
    except ValueError:
        raise ValueError("Start date must be in the format DD-MM-YYYY.")
    return start_date

# Function to get and validate the end date (format YYYY-MM-DD)
def get_end_date():
    end_date = input("Enter end date (DD-MM-YYYY): ")
    try:
        datetime.strptime(end_date, "%m-%d-%Y")
    except ValueError:
        raise ValueError("End date must be in the format YYYY-MM-DD.")
    return end_date

