# Working with Text Data in Python

* [1. Example Data Used Through This Cheat Sheet](#1-example-data-used-through-this-cheat-sheet)
* [2. String Lengths and Substrings](#2-string-lengths-and-substrings)
* [3. Changing Case](#3-changing-case)
* [4. Formatting Settings](#4-formatting-settings)
* [5. Splitting Strings](#5-splitting-strings)
* [6. Joining or Concatenating Strings](#6-joining-or-concatenating-strings)
* [7. Detecting Matches](#7-detecting-matches)
* [8. Extracting Matches](#8-extracting-matches)
* [9. Replacing Matches](#9-replacing-matches)

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
# Get the number of characters
suits.str.len() # Returns 5 8 6 6

# Get substrings by position with
suits.str[2:5] # Returns "ubs" "amo" "art" "ade"

# Get substrings by negative position
suits.str[:-3] # "cl" "Diamo" "hea" "Spa

# Remove whitespace from the start / end
rock_paper_scissors.str.strip() # "rock" "paper" "scissors"

# Pad strings to a given length
suits.str.pad(8, fillchar="_") # "___clubs" "Diamonds" "__hearts" "__Spades"
```

## 3. Changing Case
```python
# Convert to lowercase
suits.str.lower() # "clubs" "diamonds" "hearts" "spades"

# Convert to uppercase
suits.str.upper() # "CLUBS" "DIAMONDS" "HEARTS" "SPADES"

# Convert to title case
pd.Series("hello world").str.title() # "Hello World"

# Convert to sentence case
pd.Series("hello world").str.capitalize() # "Hello world"
```

## 4. Formatting Settings
```python
# Generate an example DataFrame named df
df = pd.DataFrame({'x': [0.123, 4.567, 8.901]})
#    x
# 0  0.123
# 1  4.567
# 2  8.901

# Visualize and format table output
df.style.format(precision=1)
#    x
# 0  0.1
# 1  4.5
# 2  8.9
```

## 5. Splitting Strings
```python
# Split strings into list of characters
suits.str.split(pat="")

# [, "c" "l" "u" "b" "s", ]
# [, "D" "i" "a" "m" "o" "n" "d" "s", ]
# [, "h" "e" "a" "r" "t" "s", ]
# [, "S" "p" "a" "d" "e" "s", ]

# Split strings by a separator
suits.str.split(pat="a")

# ["clubs"]
# ["Di", "monds"]
# ["he", "rts"]
# ["Sp", "des"]

# Split strings and return DataFrame
suits.str.split(pat="a", expand=True)

#    0      1
# 0  clubs  None
# 1  Di     monds
# 2  he     rts
# 3  Sp     des
```

## 6. Joining or Concatenating Strings
```python
# Combine two strings
suits + "5" = # "clubs5" "Diamonds5" "hearts5" "Spades5"

# Collapse character vector to string
suits.str.cat(sep=", ") # "clubs, Diamonds, hearts, Spades"

# Duplicate and concatenate
suits * 2 # "clubsclubs" "DiamondsDiamonds" "heartshearts" "SpadesSpades"
```

## 7. Detecting Matches
```python
# Detect if a regex pattern is present in strings
suits.str.contains("[ae]") # False True True True

# Count the number of matches
suits.str.count("[ae]") # 0 1 2 2

# Locate the position of substrings
suits.str.find("e") # -1 -1 1 4
```

## 8. Extracting Matches
```python
# Extract matches from strings
suits.str.findall(".[ae]") # [] ["ia"] ["he"[ ["pa", "de"]

# Extract capture groups
suits.str.extractall("([ae])(.)")
#            0 1
#   match
# 1 0        a m
# 2 0        e a
# 3 0        a d
#   1        e s

# Get subset of strings that match
suits[suits.str.contains("d")] # "Diamonds" "Spades"
```

## 9. Replacing Matches
```python
# Replace a regex match with another string
suits.str.replace("a", "4") # "clubs" "Di4monds" "he4rts" "Sp4des"

# Remove a suffix
suits.str.removesuffix # "club" "Diamond" "heart" "Spade"

# Replace a substring
rhymes = pd.Series(["vein", "gain", "deign"])
rhymes.str.slice_replace(0, 1, "r") # "rein" "rain" "reign"
```

---

##### _Source: [Datacamp](https://media.datacamp.com/legacy/image/upload/v1671098753/Marketing/Blog/Working_With_Text_Data_in_Python.pdf)_

