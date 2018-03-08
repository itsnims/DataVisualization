#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:29:28 2017

@author: Nimra
"""
import dash
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
from Barchartapp import BarChart, DonutChart, LineChart

DatasetBar= BarChart()
trace1= go.Bar(x=DatasetBar["Zone"], y=DatasetBar["GeburtenM"], name = "Mänlich")
trace2= go.Bar(x=DatasetBar["Zone"], y=DatasetBar["GeburtenF"], name = "Weiblich") #creating the bar chart with plotly

DatasetDonut = DonutChart()
MaleFemale = ["Male","Female"]
values = [DatasetDonut["Male"],DatasetDonut["Female"]] #creating piechart 
trace3 = go.Pie(labels=MaleFemale, values=values, hoverinfo='label+percent', textinfo='value')

DatasetLine = LineChart()
tracemale = go.Scatter(x=DatasetLine["Year"],y=DatasetLine["Male"], name = "Männlich")
tracefemale = go.Scatter(x=DatasetLine["Year"],y=DatasetLine["Female"], name = "Weiblich")
tracesumme = go.Scatter(x=DatasetLine["Year"],y=DatasetLine["Summe"], name = "Summe") #creating lines for timeseries

app = dash.Dash()
app.layout = html.Div([
    html.Div(children=[
    html.H1(children='Dashboard: Geburten in Zürich'),
    html.Div(children='''Ein Dashboard mit Visualisationen für den Kurs Data Visualisation Concepts.'''),
    dcc.Graph(
        id='bar',
        figure={
            'data': [trace1, trace2],
            'layout':
            go.Layout(title='Geburten pro Zone im Jahre 2015', barmode='stack')
        })
    ]),
    html.Div([
        html.Div([
            dcc.Graph(
                    id='g1', 
                    figure={
            'data': [trace3],
            'layout':
            go.Layout(title='Prozentualer Anteil im Jahre 2015')
        })
        ], className="six columns"),

        html.Div([
            
            dcc.Graph(
                    id='Timeseries', 
                    figure={
            'data': [tracemale,tracefemale,tracesumme],
            'layout':
            go.Layout(title='Geburten über die Jahre hinweg')
        }
                    )
        ], className="six columns"),
    ], className="column")
    
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
