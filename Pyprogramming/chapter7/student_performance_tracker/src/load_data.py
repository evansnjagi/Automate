import pandas as pd

def load_dataset(filepath):
    """"
    Load the dataset into a matrix: X_i = (Age, studytime, failures, health, absences, G3)

    Parameter:
    filepath(str): The location of the dataset

    Return
    data(dict): A formatted dictinary
    """
    df = pd.read_csv(filepath, sep=";")

    # Features
    features = ["age", "studytime", "failures", "health", "absences", "G3"]

    X = df[features]

    return X.to_dict(orient = "records")