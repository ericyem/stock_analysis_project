from typing import Type
from pandas_datareader import data as pd
import pandas
import datetime 
import sys


# start date, ticker 
# taking start date from today to how many years ago
def required_date(datetime: start, datetime: end):
    
start = datetime.datetime.now() - datetime.timedelta(days=2*365)
end = datetime.datetime.now()
# reading the data from two years ago to today for a particular stock
raw_data = pd.DataReader('CBA', 'yahoo', start, end)

# pickling the data frame so do not have reload every time
raw_data.to_pickle('CBA_frame.pickle')
stock_frame = pandas.read_pickle('CBA_frame.pickle')
print(stock_frame.head())


if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        
        




