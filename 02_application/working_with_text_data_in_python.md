# Working with Text Data in Python

* [1. Example Data Used Through This Cheat Sheet](#1-example-data-used-through-this-cheat-sheet)
* [2. String Lengths and Substrings](#2-string-lengths-and-substrings)
* [3. Changing Case](#3-changing-case)
* [4. Formatting Settings](#4-formatting-settings)
* []()
* []()
* []()
* []()
* []()
* []()

---

## 1. Example Data Used Through This Cheat Sheet
Throughout this cheat sheet, we’ll be using two pandas series named suits and rock_paper_scissors.
```python
import pandas as pd

suits = pd.Series(["clubs", "Diamonds", "hearts", "Spades"])
rock_paper_scissors = pd.Series(["rock ", " paper", "scissors"])
```

## 2. String Lengths and Substrings
```python
# Get the number of characters with .str.len()
suits.str.len() # Returns 5 8 6 6

# Get substrings by position with .str[]
suits.str[2:5] # Returns "ubs" "amo" "art" "ade"

# Get substrings by negative position with .str[]
suits.str[:-3] # "cl" "Diamo" "hea" "Spa

# Remove whitespace from the start/end with .str.strip()
rock_paper_scissors.str.strip() # "rock" "paper" "scissors"

# Pad strings to a given length with .str.pad()
suits.str.pad(8, fillchar="_") # "___clubs" "Diamonds" "__hearts" "__Spades"
```

## 3. Changing Case
```python
# Convert to lowercase with .str.lower()
suits.str.lower() # "clubs" "diamonds" "hearts" "spades"

# Convert to uppercase with .str.upper()
suits.str.upper() # "CLUBS" "DIAMONDS" "HEARTS" "SPADES"

# Convert to title case with .str.title()
pd.Series("hello, world!").str.title() # "Hello, World!"

# Convert to sentence case with .str.capitalize()
pd.Series("hello, world!").str.capitalize() # "Hello, world!"
```

## 4. Formatting Settings
```python
# Generate an example DataFramed named df
df = pd.DataFrame({"x": [0.123, 4.567, 8.901]})
#    x
#  0 0.123
#  1 4.567
#  2 8.901

# Visualize and format table output
df.style.format(precision = 1)
```

## 5. Section
Exp
```python

```

## 6. Section
Exp
```python

```

## 7. Section
Exp
```python

```

## 8. Section
Exp
```python

```

---

##### _Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1671098753/Marketing/Blog/Working_With_Text_Data_in_Python.pdf)_

