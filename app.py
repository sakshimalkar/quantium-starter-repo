import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load the data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Div(
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                ),
            ],
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        dcc.Graph(id="sales-graph")
    ],
    style={
        "width": "80%",
        "margin": "auto",
        "fontFamily": "Arial"
    }
)

# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[
            filtered_df["Region"].str.lower() == selected_region
        ]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        }
    )

    fig.update_layout(
        title="Pink Morsels Sales Over Time",
        template="plotly_white"
    )

    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
