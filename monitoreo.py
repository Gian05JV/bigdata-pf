#pip install dash
#pip install dash-core-components
#pip install dash-html-components
#pip install dash-bootstrap-components
#pip install pandas
#pip install plotly

import dash
from dash import dash_table
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dbisesion


df = pd.DataFrame(list(dbisesion.consulta_sensores()))
df2 = pd.DataFrame((dbisesion.consulta_sensores()))
'''del df2['_id']
df2.to_csv('wordsclean.csv', index=False)'''
df3 = pd.read_csv('wordsclean.csv')
listadf3 = list(df3)


#crear dash en el servidor web de Flask
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
def create_dash(flask_app):
    app = dash.Dash(server=flask_app, name="Dashboard", external_stylesheets=[dbc.themes.UNITED], url_base_pathname="/dash/")

    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1('Dashboard', style={'textAlign': 'center', 'color': '#7FDBFF'}),
        html.Br(),
        dcc.Dropdown(
            options=[{'label':i, 'value': i} for i in df.columns],
            id='dropdown',
            placeholder='Selecciona una opción',
            style={"width": "99%", "offset": 1, 'backgroundColor': colors['background'], 'color': colors['text']},
            clearable=False,
        ),
        html.Div(style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}, children=[
            dcc.Graph(id='histogram')

        ]),
        html.Div(style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}, children=[
            dcc.Graph(id='scatter')

        ]),
        html.Div(style={'width': '99%', 'display': 'inline-block', 'padding': '0 20'}, children=[
            dcc.Graph(id='piechart')
        ]),
        html.Hr(),
        html.H6('Utilizando técnicas de procesamiento de texto y análisis de frecuencia de palabras, se identifican las palabras ofensivas más utilizadas en el contexto del proyecto. Esto puede proporcionar una visión clara de las palabras que son más comunes en el lenguaje ofensivo y que podrían ser el foco principal de atención.', style={'textAlign': 'center', 'color': '#7FDBFF'})
    ])

    #callbacks

    @app.callback(
        Output(component_id='histogram', component_property='figure'),
        Output(component_id='scatter', component_property='figure'),
        Output(component_id='piechart', component_property='figure'),
        Input(component_id='dropdown', component_property='value'),
    )

    def update_hist(feature):
        fig = px.histogram(df, x=feature)
        fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])
        fig2 = px.scatter(df, x=feature)
        fig2.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])
        fig2.update_xaxes(showgrid=False)
        piechart = px.pie(data_frame=df, names=feature)
        piechart.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'],
                          font_color=colors['text'])
        #fig3 = px.pie(df, x=feature)
        return fig, fig2, piechart
