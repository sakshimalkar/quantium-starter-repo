import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load the data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsels Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
