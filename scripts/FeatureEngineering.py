import sys
import pandas as pd

def create_features(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # Create a new feature that's the square of the 'heart_rate' feature
    df['heart_rate_squared'] = df['heart_rate'] ** 2
    
    df.to_csv(output_path, index=False)

create_features(sys.argv[1], sys.argv[2])
