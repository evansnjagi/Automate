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

## `In` and `not in` operators

In: It's a simple but powerful way of searching patterns in Python.

Example:

```python
name = "Evans"
if E in name:
    print("Yes, Available")
else:
    print("No, Not in the name")
```
Task:

Write a program that stores this text `"The system detected a theft at midnight"`, then check if the `theft` exists.If yes, print `Alart: Theft detected`. If not, print `No threat`.

Bonus make the string case sensitive.

To get the solution, run the following bash command

```bash
code alert.py
```

To get the Python output, run this command

```bash
python alert.py
```

## f-strings

f-strings allows us to insert variables or expressions directly inside a string.

Example:

```python
name = "Evans"
age = 25

print(f"My name is {name} and I am {age} years old")
```

In data science we can use f-strings to dynamically name files. Example

```python
date = "2026-05-01"

filename = f"report_{date}.csv"
```

Task:

write a program that stores 

```r
model_name = "Theft Detection Model"
accuracy = 0.93
```
and output the following message: `The Theft Detection Model has an accuracy of 93.0%`

## Changing the case

`.lower`: Used to convert a string to lower case
`.upper` : Does the opposite of `.lower`. It convert a string to upper case.

These two methods do NOT change the original string.

Task:

Write a program that stores: `user_input = "DaTa ScIeNcE"`. Convert it to lowercase and uppercase and print both results.

To get the source code, run the following command:

```bash
code string_case.py
```

Finally, to get the output run the following command.

```bash
python string_case.py
```

## String validation methods(`isX()`).

These methods are used to check what kind of characters are in a string.

They return either `True` or `False`.

Common methods includes:

1. `isalpha()` - Check if a string contains letters only.

Example:

"hello".isalpha() - Retruns True.
"hello123".isalpha() - Returns False.
2. `isalnum()` - Checks for letters and numbers.

Example:

"user122".isalnum() - Return True

If there is a space in between, it returns False.

Example:

"user 123".isalnum()

The above will return false because a space is not either a letter or a number.

3. `isdecimal()` - Checks for numbers only.

Example:

"123".isdecimal() - Returns True.

If the number is not an integer, the function will return false. 

Example:

"123.3".isdecimal() - Returns false.

4. `isspace()`- Checks for only spaces, tabs and newlines.

Example:

" ".isspace() - Returns true

5. `istitle()` - Checks if the characters/ string are in a title case.

Example:

"This Is A Tittle".istitle() - Return true

The above methods are used in data cleaning pipeline. By doing the following:
- Prevent errors during integer conversion
- Filter invalid data 

Example:
```python
username = "user_123"

if username.isalnum():
    print("Valid")
else:
    print("Invalid")
```
- Remove noise in NLP. 

Example:

```python
words = ["data", "science", "AI", "123"]

clean_words = [w for w in words if words.isalpha()]
```

Task:

Write a program that:

1. Asks users for input
    - Age
    - User name
2. Validate user's input
    - Age must be an integer
    - User name must contain letters and numbers
3. The program should print:
    - "Valid input" if all tests pass
    - "Invalid input" if one of the test fails.

Solution.

Run the bash command to get the script `string_validation.py`

```bash
code string_validation.py
```

To run it, run the following code

```bash
python string_validation.py
```
### The `split()` and `join()` functions

The `split()` breaks the text and returns a list. What happens is that it scans for white space or custom split characters.

The `join()` combines strings by reconstructing texts together. This method is highly optimized compared to using the `+` concatenation method. 

Concatinting strings calls for creationg of a new string first. Remember, strings are immutable and so before joining them one must create a new string to hold the old one together with the added new string. Then, the old string is copied, and later the temporary objects destroyed. 

The string concatenation method is computationary heavy and takes alot of memory which can lead to issues if you are working on a very big string.

Example: An optimized alternative.

```python
name_message = "My name is   Evans"

# Split message
new_message = name_message.split()

# Join message list
cleaned_message = " ".join(new_message)
```

Worked script example.

You are given a text `"I love Data Science`, make all the characters in the string to be lower case.

Open:

```bash
make split_join.py
```

Run the script:

```bash
python split_join.py
```

Expected output:

```r
i love data science
```

Steps taken:

While solving the above problem, the following are steps to follow:

1. Split the message
2. Using a list comprehension, convert singled string to lower case strings.
3. Join the converted strings together to form a sentence. The sentence is really one big string. 
4. Print out the results for inspection.

Application:

1. Tokenization in NLP processing.
2. Cleaning dataset
3. Cleaning scraped data
4. Cleaning messy user input data

## Sting justification

`rjust()` - Righ justification

Example usage:

```python
"Hello".rjust(8, "-")
```

Expected output:

```raw
---"Hello"
```

`ljust()` - Left justification

Example usage:

```pyhton
"string".ljust(8, "*")
```
Expected results:

```r
"string"**
```

`center()` - Centeing

Example:

```python
"python".center(10, "-")
```

Results:

```raw
--"python"--
```

Intuition:

padding = width - len(text)