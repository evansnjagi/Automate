# Modules
from src.load_data import load_dataset

filepath = "data/student-mat.csv"

X = load_dataset(filepath)

print(X[:5])