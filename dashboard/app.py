#!/usr/bin/env python3
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

path = "https://github.com/curso-visualizacion/practicas_diploma/blob/2022/Practica2/migrantes_chile.xlsx?raw=true"
dataset = pd.read_excel(path)
dataset.loc[:, "total"] = dataset.iloc[:, 4:].sum(axis=1)

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)


if __name__ == "__main__":
    app.run_server(debug=True)
