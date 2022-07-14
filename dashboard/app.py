#!/usr/bin/env python3
from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

path = "https://github.com/curso-visualizacion/practicas_diploma/blob/2022/Practica2/migrantes_chile.xlsx?raw=true"
dataset = pd.read_excel(path)
dataset.loc[:, "total"] = dataset.iloc[:, 4:].sum(axis=1)

# First exercise
first_exercise = go.Figure()
continents = dataset.Continent.unique()
for cont in continents:
    first_exercise.add_trace(
        go.Histogram(x=dataset[dataset.Continent == cont]["total"], name=cont)
    )

first_exercise.update_layout(barmode="stack")
# first_exercise.update_layout(barmode="overlay")
# first_exercise.update_traces(opacity=0.75)


# Second exercise
def compare_countries_data(df, continents, year="total"):
    values = []
    for continent in continents:
        temp = df[df.Continent == continent]
        values.append(temp[year].sum())

    return values


def compare_countries_plot(df, continents, year="total"):
    second_exercise = go.Figure()
    second_exercise.add_trace(
        go.Bar(x=continents, y=compare_countries_data(df, continents))
    )
    return second_exercise


second_exercise = compare_countries_plot(dataset, ["Asia", "Europa"])


# Third exercise
third_exercise = go.Figure(
    data=[
        go.Bar(
            name="2010",
            x=["Asia", "Europa"],
            y=compare_countries_data(dataset, ["Asia", "Europa"], 2010),
        ),
        go.Bar(
            name="2015",
            x=["Asia", "Europa"],
            y=compare_countries_data(dataset, ["Asia", "Europa"], 2015),
        ),
    ]
)

# Fourth exercise
america = dataset[dataset.Continent == "América"]
america.set_index("Country", inplace=True)
america = america.sort_values("total")[-5:]
fourth_exercise = go.Figure()
fourth_exercise.add_trace(
    go.Pie(labels=america.index.values, values=america.total, textinfo="label+percent")
)


# fifth exercise
fifth_exercise = go.Figure()
dataset.set_index("Country", inplace=True)
top3 = dataset.sort_values("total", ascending=False)[:3]
for country in top3.index:
    df = dataset.loc[country, range(2005, 2017)]
    fifth_exercise.add_trace(go.Box(y=df, name=country))


app.layout = html.Div(
    children=[
        html.H1(children="Distribución de migrantes por continente"),
        dcc.Graph(id="histogram", figure=first_exercise),
        html.H1(children="Comparación de migrantes por continente"),
        dcc.Graph(id="bar", figure=second_exercise),
        dcc.Graph(id="bar2", figure=third_exercise),
        html.H1(children="Comparación de migrantes por pais de América"),
        dcc.Graph(id="pie", figure=fourth_exercise),
        html.H1(
            children="Comparación de migrantes de los tres paises con más migrantes"
        ),
        dcc.Graph(id="box", figure=fifth_exercise),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
