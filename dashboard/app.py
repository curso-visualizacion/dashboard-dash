#!/usr/bin/env python3
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

path = "https://github.com/curso-visualizacion/practicas_diploma/blob/2022/Practica2/migrantes_chile.xlsx?raw=true"
dataset = pd.read_excel(path)
dataset.loc[:, "total"] = dataset.iloc[:, 4:].sum(axis=1)
dataset.columns = dataset.columns.astype(str)
dataset.set_index("Country", inplace=True)

column_options = [{"label": col, "value": col} for col in dataset.columns[4:]]

controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Year"),
                dcc.Dropdown(
                    id="year",
                    options=column_options,
                    value="total",
                ),
            ]
        ),
    ],
    style={"height": "100%"},
)

app.layout = dbc.Container(
    [
        html.H1("Distribución"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=3),
                dbc.Col(
                    dcc.Graph(id="histogram"),
                    md=9,
                ),
            ],
            align="center",
        ),
    ],
    className="p-5",
)


@app.callback(
    Output(component_id="histogram", component_property="figure"),
    Input(component_id="year", component_property="value"),
)
def update_histogram(input_value):
    fig = go.Figure()
    continents = dataset.Continent.unique()
    for cont in continents:
        fig.add_trace(
            go.Histogram(x=dataset[dataset.Continent == cont][input_value], name=cont)
        )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
