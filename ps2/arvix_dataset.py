import pandas as pd
import json

# Path where you saved the extracted JSON file
dataset_path = r"H:\research paper\research paper.json"

# Initialize an empty list to store data
data = []

# Read JSON file line by line
with open(dataset_path, 'r') as f:
    for line in f:
        # Parse each line as JSON
        data.append(json.loads(line))

# Convert data to DataFrame
df = pd.DataFrame(data)

# Ensure the 'update_date' column is in datetime format
df['update_date'] = pd.to_datetime(df['update_date'])

# Filter for years 2021 to 2025
filtered_df = df[(df['update_date'].dt.year >= 2023) & (df['update_date'].dt.year <= 2025)]

# Keep only 'title' and 'abstract' columns
filtered_df = filtered_df[['title', 'abstract']]

# Save filtered dataset to CSV
filtered_df.to_csv('filtered_data.csv', index=False)
