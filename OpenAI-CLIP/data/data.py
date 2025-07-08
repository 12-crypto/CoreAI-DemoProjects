import pandas as pd

# Read the original CSV
input_file = "data/captions.csv"  # Adjust path if needed
output_file = "data/captions_with_id.csv"

# Read the CSV
df = pd.read_csv(input_file)

# Add an id column that numbers rows from 0 to len(df)-1
df['id'] = range(len(df))

# Save to new CSV
df.to_csv(output_file, index=False)

print(f"New CSV file with 'id' column saved at: {output_file}")
