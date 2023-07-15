import sys
import pandas as pd
import joblib
import os

def detect_anomalies(input_path, output_path):
    df = pd.read_csv(input_path)
    
    model_path = os.path.join('models', 'model.joblib')
    model = joblib.load(model_path)
    
    df['anomaly'] = model.predict(df.drop('anomaly', axis=1))
    df.to_csv(output_path, index=False)

detect_anomalies(sys.argv[1], sys.argv[2])
