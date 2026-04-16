# Student performance tracker

As a learning phase, this project analyses students achievements in portugal schools.

The project will depen dictionary(Python data type) understanding.

## Objectives
- Load students data
- Analyze grades
- Identify top-performing student
- Find least-performing students
- Build a summary of the results

## Structure

Example structure used in this project:

```bash
student_performance_tracker
├── README.md
├── data/
├── notebooks/
├── main.py
├── requirements.txt
├── src/
└── tests/

5 directories, 3 files
```

## Data

The dataset used is downloaded from UCI official source for learning purposes. In this project, it is saved in the `data/` folder as a zip file named: `students+performance.zip`

### Unzip the dataset

To unzip the file use the command below:

```bash
unzip data/students_performance.zip
```
You'll get two files `student+performance.zip` and `student.zip`. We'll go ahead and unzip the student zipped file as shown below:

```bash
unzip student.zip
```

A couple of files shows up but we are interested in `student-mat.csv`.

**Note**: We will be working with `student-math.csv` file for this project.


## Inspect the data

Inside the `01_understanding_data.ipynb` file, we are going to explore some basic properties of the `student-math.csv` file.

### Uncovered
- There are 396 students
- 33 features are included
- No missing values
- Useful features: 
    - Age
    - studytime
    - failures
    - health
    - absences

Useful features will form a matrix $X \in \mathbb{R}^{396 \times 5}$ as $X_i = (Age, studytime, failures, health, absences)$

## Load the data


## Requirements

This project use the following packages:
- pandas - Loading, cleaning, and understaning data
- matplotlib - Data visualization

Usage:

```bash
pip install -r requirements.txt
```
