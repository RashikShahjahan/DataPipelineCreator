import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(0)

# Generate synthetic data
num_samples = 100
heart_rate = np.random.normal(60, 10, num_samples)  # Normal distribution with mean 60 and standard deviation 10
activity_level = np.random.choice([0, 1, 2], num_samples)  # Activity level: 0 (low), 1 (medium), 2 (high)
anomaly = np.random.choice([0, 1], num_samples, p=[0.95, 0.05])  # 5% of the samples are anomalies

# Create a DataFrame
df = pd.DataFrame({
    'heart_rate': heart_rate,
    'activity_level': activity_level,
    'anomaly': anomaly
})

# Write the DataFrame to a CSV file
df.to_csv('test.csv', index=False)
