# Strings and Text Editing

Strings are a sequence of characters. Basically, they are data containers holding text and characters.

In data science strings can contain information about the following:

1. Logs
2. Reviews
3. Structured data: Json data

## String literal

A string literal is an actual text written directly into our code.

Example:
Run this command to open `string_literal.py` file and run it in the bash command line
```bash
code string_literal.py
python string_literal.py
```

## Escape sequences

These are special characters that are used to represent something that is hard or imposible to type in the actual code.

Example of escape characters in Python

|Escape characters| What they do|
|-----------------|-------------|
|\n| Create a new line|
|\t| Tab|
|\\\| Backslash character|
|\\'| Single quote|

There are many more escape characters.

We have a program that print the strings below:

Name:    Evans
Age:     25

Location: Nairobi

To get the string run the code below in bash terminal

```bash
code escape_sequence.py
python escape_sequence.py
```

## Raw string

These are strings where escape sequences are ignore.

They are created by adding an `r` before the string.

Example:

```bash
code raw_string.py
python raw_string.py
```

Raw strings are heavily used in: 

1. File paths
2. Regular expressions
3. Working with logs: i.e detecting security logs or system monitoring.

## Multi-line strings

These are strings that pass multiple lines. They are created using tripple quotation marks: either `"""your string"""` or `'''your string'''`.

Example:

```python
# Multi-string 

multi_string = """
    Name: Evans

    Role: Data scientist

    Goal: Build a theft detection system
"""

print(multi_string)
```

## Indexing and slicing.

Indexing: You get one piece of the string.
Slicing: You get a protion of the string.

To get an example usage, use the command below.

```bash
code indexing_slicing.py
```

Then run the code using this code:

```bash
python indexing_slicing.py
```