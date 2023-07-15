import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model(input_path):
    df = pd.read_csv(input_path)
    X = df.drop('anomaly', axis=1)
    y = df['anomaly']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    model_path = os.path.join('models', 'model.joblib')
    joblib.dump(model, model_path)

train_model(sys.argv[1])
