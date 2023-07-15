# Personal Data Processing and Machine Learning Pipeline

This project provides an open-source, self-hosted framework for creating data pipelines for personal data, such as personal health data. The framework allows you to execute a series of Python scripts in a specific order, as defined by a prerequisite map. The scripts can be used for data processing and machine learning tasks, such as data preprocessing, feature engineering, model training, model evaluation, and anomaly detection.

## Requirements

    Python 3.7 or higher
    Ray library
    NetworkX library
    Pandas library
    Scikit-learn library
    Joblib library

## Starting Ray

Before running the pipeline, you need to start a Ray cluster. You can do this by running the following command in your terminal:


``ray start --head``

This will start a Ray cluster on your local machine that you can connect to. If you want to stop the Ray cluster, you can use the following command:


``ray stop``

## Usage

Define your pipeline in a JSON file. Each key in the JSON file represents a script, and the corresponding value is an object with two properties: "host" (the host where the script should be executed) and "prerequisites" (an array of scripts that must be executed before the current script). Here's an example:


    {
        "DataPreprocessing": {
            "host": "localhost",
            "prerequisites": []
        },
        "FeatureEngineering": {
            "host": "localhost",
            "prerequisites": ["DataPreprocessing"]
        },
        "ModelTraining": {
            "host": "localhost",
            "prerequisites": ["FeatureEngineering"]
        }
    }


Write your scripts following the structure shown in the example below. Each script should take an input file and an output file as command-line arguments, perform some operation on the input data, and write the result to the output file:


    import sys
    import pandas as pd
    
    def main(input_path, output_path):
        df = pd.read_csv(input_path)
        # Perform some operation on df
        df.to_csv(output_path, index=False)
    
    main(sys.argv[1], sys.argv[2])


 Run the main script with the path to your pipeline JSON file and the path to your input data file as command-line arguments:


    python3 pipeline_creator.py pipeline.json input.csv


The script will execute the scripts in your pipeline in the order defined by the prerequisite map. The interaction between the scripts can be specified by the user.
## Privacy

As this is a self-hosted solution, all your personal data stays with you. The pipeline runs locally on your machine or on a server you control. No data is sent to any third-party servers.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.