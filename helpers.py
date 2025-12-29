import os
import pandas as pd
import yfinance as yf

def get_stock_data(data_name : str ="AAPL", local_path : str ="./data/AAPL.csv") -> pd.DataFrame:
    if not os.path.exists(local_path):
        print("Downloading Data")
        stock_data = yf.download(data_name, start="2024-01-01")
        stock_data.to_csv(local_path)
    else:
        print("Loading Data From Local")
        stock_data = pd.read_csv(
            local_path,
            header=[0, 1],
            index_col = 0,
            parse_dates = True
        )
    
    return stock_data

if __name__ == "__main__":
    stock_data = get_stock_data()
    stock_data.info()