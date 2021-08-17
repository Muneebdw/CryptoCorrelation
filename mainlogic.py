from numpy import tracemalloc_domain
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
import plotly.express as px
import plotly.graph_objs as go

yf.pdr_override()
import pandas as pd

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticket_list =['BTC-USD','ETH-USD']
today = date.today()
start_date = "2017-01-11"
end_date =  "2019-01-11"
files = []
to_drop = ['Open','High','Low','Adj Close', 'Volume']
data = pdr.get_data_yahoo(ticket_list[0], start=start_date, end=today)
data2 = pdr.get_data_yahoo(ticket_list[1], start=start_date, end=today)

data.drop(to_drop,inplace=True,axis=1)
#data2.drop(to_drop,inplace=True,axis=1)
#data['date']=data.Date
#data = pd.pivot_table(data,values='Close',index='Date')
#print(data.columns)

#data.to_csv('test.csv')
#data2.to_csv('test2.csv')

'''fig = px.line(data, title='Correlation')
fig.add_scatter(x=data2.index, y=data2['Close'], mode='lines')

fig.show()
'''

fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'],
               mode='markers',  name = 'Crypto 1'))
fig.add_trace(go.Scatter(x=data2.index, y= data2['Close'],
               mode='markers',  name = 'Crypto 2'))
               #mode = lines
fig.update_layout(title='line charts',)
fig.show()
print(data)
