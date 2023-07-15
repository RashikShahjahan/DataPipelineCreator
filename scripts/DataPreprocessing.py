import sys
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # Normalize the data to the range [0, 1]
    scaler = MinMaxScaler()
    df[['heart_rate', 'activity_level']] = scaler.fit_transform(df[['heart_rate', 'activity_level']])
    
    df.to_csv(output_path, index=False)

preprocess_data(sys.argv[1], sys.argv[2])
