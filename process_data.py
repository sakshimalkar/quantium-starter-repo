import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Get all CSV files
csv_files = list(data_path.glob("*.csv"))

# Read and combine CSVs
df_list = [pd.read_csv(file) for file in csv_files]
df = pd.concat(df_list, ignore_index=True)

# Filter only Pink Morsels
df = df[df["product"] == "Pink Morsels"]

# Create Sales column
df["Sales"] = df["quantity"] * df["price"]

# Select required columns
final_df = df[["Sales", "date", "region"]]

# Rename columns
final_df = final_df.rename(columns={
    "date": "Date",
    "region": "Region"
})

# Save output file
final_df.to_csv("formatted_output.csv", index=False)

print("formatted_output.csv created")
