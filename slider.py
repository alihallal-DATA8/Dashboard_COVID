import dash
import pandas as pd
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Create figure
#fig = go.Figure()

# Add traces, one for each slider step
#for step in np.arange(0, 9, 0.1):
    # fig.add_trace(
    #     go.Scatter(
    #         visible=False,
    #         line=dict(color="#00CED1", width=6),
    #         name="𝜈 = " + str(step),
    #         x=np.arange(0, 10, 0.01),
    #         y=np.sin(step * np.arange(0, 10, 0.01))))

# Make 10th trace visible
# fig.data[10].visible = True

# # Create and add slider
# steps = []
# for i in range(len(fig.data)):
#     step = dict(
#         method="update",
#         args=[{"visible": [False] * len(fig.data)},
#               {"title": "Slider switched to step: " + str(i)}],  # layout attribute
#     )
#     step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
#     steps.append(step)

# sliders = [dict(
#     active=10,
#     currentvalue={"prefix": "Age: "},
#     pad={"t": 90},
#     steps=steps
# )]

#fig.update_layout()



df = pd.read_csv('donnees-hospitalieres-classe-age-covid19-2021-02-18-19h03.csv', sep=';', parse_dates=['jour'] , 
                      index_col='jour')

# df = df.groupby([df.index,'reg','cl_age90']).sum().reset_index().set_index(['jour'])


# def cumulative_sum(df, feature_name, by_reg= False):   
#     '''return the cumulative sum of a column whose name is called  feature_name
    
#     input:
#     -----
#     df: pandas Dataframe, rawdata 
#     feature_name: str, name of a colomn in df, which is seperated data day by day
    
#     return:
#     -------
#     cumulative sum of the feature_name by days regardless of age group
    
#     '''
#     if by_reg == True:
#          return  pd.DataFrame(df.groupby(['reg',df.index,'cl_age90']).sum().groupby('reg')[feature_name].cumsum()) 
#     else:
#         return pd.DataFrame(df.groupby(['reg', df.index,'cl_age90']).sum().groupby('jour').sum()[feature_name].cumsum())


# df_age = cumulative_sum(df, 'hosp', by_reg = True)
# df = df_age.reset_index().set_index(['jour'])        

# df_uncumlated = []
# for region in df.reg.unique():
#     for age in df.cl_age90.unique():
#         df_mod = df[(df.reg == region) & (df.cl_age90 == age)]
#         df_mod.dc = df_mod.dc.diff()
#         df_mod.rad = df_mod.rad.diff()
#         df_uncumlated.append(df_mod)

# df = pd.concat(df_uncumlated)        

#fig = px.line(df, x=df.index, y="dc", color="reg")


# Define and connect the dynamic 
@app.callback(Output('example-graph', 'figure'),
              Input('my-slider', 'value'))
def fig_dynm(filter):
    print(filter)
    #df_filter = df[(df['cl_age90'] <= int(filter))&(df['reg']==1)]
    df_filter = df[df['cl_age90'] <= int(filter)]
    fig = px.scatter(df_filter, x=df_filter.index, y="hosp", color="reg")
    #fig = px.scatter(df_filter, x=df_filter.index, y="hosp")
    return fig

app.layout = html.Div(children=[
    html.H1(children='Number of Hosp in different regions according to the ages of patients'),

    html.Div(children='''
        Dash: Change the slider to see the cumulative Hosp number under certain ages in each region.
    '''),


    dcc.Graph(
        id='example-graph'
    ),
    dcc.Slider(
        id='my-slider',
        min=0,
        max=99,
        step=None,
        value=9,
        marks={
            0: '0',
            9: '10',
            19: '20',
            29: '30',
            39: '40',
            49: '50',
            59: '60',
            69: '70',
            79: '80',
            89: '90',
            99: '100'
        },
    ),
])




if __name__ == '__main__':
    app.run_server(debug=True)