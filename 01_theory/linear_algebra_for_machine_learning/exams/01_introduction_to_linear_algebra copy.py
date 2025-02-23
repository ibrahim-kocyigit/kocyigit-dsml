import numpy as np

# Consider the following data representing information about different books:
# Each row: [Price (€), Number of Pages, Year Published]

books = np.array([
    [12.50, 250, 2015],
    [9.99, 180, 2010],
    [24.00, 450, 2020],
    [15.75, 320, 2018]
])

# 1. Vector Operations:

# a) Create a vector 'prices' containing the prices of all books.
prices = # YOUR CODE HERE

# b) Create a vector 'pages' containing the number of pages of all books.
pages = # YOUR CODE HERE

# c) Calculate the average price of the books.  Store it in 'average_price'.
average_price = # YOUR CODE HERE
print(f"Average price: {average_price}")

# d) Add 2 Euros to the price of each book. Store the updated prices in 'updated_prices'.
updated_prices = # YOUR CODE HERE
print(f"Updated prices: {updated_prices}")

# e)  Subtract 50 pages from each book.  Store the updated page counts in 'updated_pages'.
updated_pages = # YOUR CODE HERE
print(f"Updated pages: {updated_pages}")

# 2. Matrix Operations:

# a) Create a new matrix 'books_2018_or_later' containing only the books published in 2018 or later.
#    (Hint: Use boolean indexing)
books_2018_or_later = # YOUR CODE HERE
print(f"Books from 2018 or later:\n{books_2018_or_later}")

# b) Increase the price of all books in the original 'books' matrix by 10%.
#    Store the result back in 'books'.
# YOUR CODE HERE (modify 'books' in place)
print(f"Books matrix with 10% price increase:\n{books}")

# 3. Combined Operations and Scalars:

# a) Find the maximum number of pages among all books. Store it in 'max_pages'.
max_pages = # YOUR CODE HERE
print(f"Max pages: {max_pages}")

# b) Find the minimum price among all books. Store it in 'min_price'.
min_price = # YOUR CODE HERE
print(f"Min price: {min_price}")

# c) Calculate the difference between the maximum and minimum prices. Store in 'price_range'.
price_range = # YOUR CODE HERE
print(f"Price Range: {price_range}")

# 4. (Bonus - a bit more challenging):
#    Calculate how many books have *more* pages than the *average* number of pages.
#    Store this count in 'num_books_above_avg_pages'.

num_books_above_avg_pages = # YOUR CODE HERE
print(f"Number of books with above-average pages: {num_books_above_avg_pages}")