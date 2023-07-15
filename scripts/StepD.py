import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)

df['numbers'] = df['numbers'] / 2

df.to_csv(output_path, index=False)
