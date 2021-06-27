from typing import Type
from pandas_datareader import data as pd
import pandas
import datetime 
import sys


# start date, ticker 
# taking start date from today to how many years ago

# reading the data from two years ago to today for a particular stock


# pickling the data frame so do not have reload every time


def main(ticker: str, start: datetime, end=datetime.datetime.now()):
    raw_data = pd.DataReader(ticker, 'yahoo', start, end)
    raw_data.to_pickle('CBA_frame.pickle')
    stock_frame = pandas.read_pickle('CBA_frame.pickle')
    print(stock_frame.head())



if __name__ == "__main__":
    try:
        startDate = input("Please enter a starting date: ")
        startDateArray = startDate.split("/")
        startDate = datetime.datetime(int(startDateArray[2]),int(startDateArray[1]),int(startDateArray[0]))
        
        ticker = input("Please enter a ticker: ")
        stockTicker = ticker.upper()
    except Exception:
        print("Please enter a valid start date and ticker")
    else:
        result = main(stockTicker, startDate)

        
        




