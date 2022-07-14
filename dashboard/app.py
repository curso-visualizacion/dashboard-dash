#!/usr/bin/env python3
from dash import Dash, html

app = Dash(__name__)
app.layout = html.Div(children="Hello World")

if __name__ == "__main__":
    app.run_server(debug=True)
