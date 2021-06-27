from typing import Type
from pandas_datareader import data as pd
import pandas
import datetime 

# taking start and end dates from today to two years ago
start = datetime.datetime.now() - datetime.timedelta(days=2*365)
end = datetime.datetime.now()
# reading the data from two years ago to today for a particular stock
raw_data = pd.DataReader('CBA', 'yahoo', start, end)

# pickling the data frame so do not have reload every time
raw_data.to_pickle('CBA_frame.pickle')
stock_frame = pandas.read_pickle('CBA_frame.pickle')
print(stock_frame.head())







