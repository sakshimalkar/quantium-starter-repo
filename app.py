# app.py
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Sample data for the graph
df = pd.DataFrame({
    "Region": ["North", "South", "East", "West"],
    "Value": [10, 20, 30, 40]
})

fig = px.bar(df, x="Region", y="Value", title="Regional Values")

# Create the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Dashboard", id="header"),
    dcc.Graph(id="graph", figure=fig),
    dcc.Dropdown(
        id="region-picker",
        options=[
            {"label": "North", "value": "North"},
            {"label": "South", "value": "South"},
            {"label": "East", "value": "East"},
            {"label": "West", "value": "West"},
        ],
        value="North"
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
