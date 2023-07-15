import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

# Read the CSV file
df = pd.read_csv(input_path)

# Perform a simple operation
df['numbers'] = df['numbers'] * 2

# Write the result to the output CSV file
df.to_csv(output_path, index=False)
