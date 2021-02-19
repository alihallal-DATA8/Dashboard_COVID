import dash
import pandas as pd
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('donnees-hospitalieres-classe-age-covid19-2021-02-18-19h03.csv', sep=';', parse_dates=['jour'] , 
                      index_col='jour')

fig = px.line(df, x=df.index, y="dc", color="reg")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])




if __name__ == '__main__':
    app.run_server(debug=True)