from flask import Flask, render_template, redirect, url_for, request
from numpy import tracemalloc_domain
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
import plotly
import plotly.express as px
import plotly.graph_objs as go
import json
app = Flask(__name__)






@app.route('/', methods=['GET', 'POST'])
def home():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    if request.method == 'GET':
        return render_template('home.html',colours=colours)

@app.route('/Calculate', methods=['GET', 'POST'])
def calculate():
    if request.method =='POST':
        c1 = request.form['Crypto1']
        c2 = request.form['Crypto2']
        ticket_list= []
        ticket_list.append(c1)
        ticket_list.append(c2)
        #ticket_list =['BTC-USD','ETH-USD']
        today = date.today()
        #start_date = "2017-01-11"
        start_date = request.form['sdate']
        end_date = request.form['edate']
        #end_date =  "2019-01-11"
        files = []
        to_drop = ['Open','High','Low','Adj Close', 'Volume']
        data = pdr.get_data_yahoo(ticket_list[0], start=start_date, end=today)
        data2 = pdr.get_data_yahoo(ticket_list[1], start=start_date, end=today)
        data.drop(to_drop,inplace=True,axis=1)
        #fig = go.Figure()
        trace1 = (go.Scatter(x=data.index, y=data['Close'],
                    mode='lines',  name = c1))
        trace2 = (go.Scatter(x=data2.index, y= data2['Close'],
                    mode='lines',  name = c2))
                    #mode = lines
        #fig.update_layout(title='line charts',)
        cdata = [{'name':c1},{'name':c2}]
        ddata = [{'sdate':start_date,'edate':end_date}]
        data = [trace1,trace2]
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('Visualize.html',graphJSON=graphJSON,cdata=cdata,ddate=ddata)

    #Calculate Correlation


    #display Correlation
    


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)