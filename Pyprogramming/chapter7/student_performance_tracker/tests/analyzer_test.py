from src.analyze import Analyzer
from src.load_data import load_dataset
# Data

filepath = "data/student-mat.csv"
X = load_dataset(filepath)

repo_analyzer = Analyzer(X)

age_result = repo_analyzer.analyze_age_results("age_result.png")

print(age_result)