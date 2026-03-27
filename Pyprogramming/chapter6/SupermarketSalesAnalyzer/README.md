# Supermarket sales analyzer 
---

This project is designed to analyze sales data from a supermarket. It demonstrated core programming and data science concepts, including:

- File handling
- List 
- Data processing
- Modular programming
- Git version control

## Objective

- Read sales data from a file
- Process and analyze the data
- Generate miningful insights such as:

    - Total sales per products
    - Total sale per day
- Build a clean, modular and scalable codebase.

## Project structure

```bash
.
├── README.md
├── data
│   └── sales.txt
├── modules
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── data_loader.cpython-312.pyc
│   └── data_loader.py
├── structure.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   └── test_data_loader.cpython-312.pyc
    └── test_data_loader.py

6 directories, 11 files
```

# Data format

The input file (`sales.txt`) follows this structure:

```r
date,product,quantiy,price
2026-03-20,Apples,10,30
```

## Features (Current)

The project has following features: 

- Read the sales data from the text file.

    Example:

    ```python
    with open(filepath, "r") as file:
        lines = file.readlines()
    ```

- Remove **NULL** terminator (\n) and unrequired header elements.

    Example:

    ```python
    for line in lines[1:]:
        line = line.strip().split(",")
    ```

- Convert data into a structured Python object (list of dictionaries)

    Example:

    ```python
    sales_data.append(
        {
            "date": date,
            "product": product,
            "quantity": quantity,
            "price": price
        }
    )
    ```

## Get started

### Step 1. Clone the repository

Example:

```bash
git clone <your repository url>
cd SupermarketSalesAnalyzer
```

### Step 2. Run the test scipt

Example usage:

```bash
python -m tests.test_data_loder
```

## Concept covered

The followed are concepts learned and applied:

- Python sequences (lists, strings, tuples, etc)
- Tuple unpack
- Reference and mutability
- File handling
- Modular programming

## Autor

Evans N. karago

## Licence

This project is for education purposes.