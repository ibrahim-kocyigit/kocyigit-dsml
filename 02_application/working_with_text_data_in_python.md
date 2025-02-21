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



```

## 3. Changing Case
```python

```

## 4. Formatting Settings
```python

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

