import numpy as np

# Consider the following data representing information about different books:
# Each row: [Price (€), Number of Pages, Year Published]

books = np.array(
    [[12.50, 250, 2015], [9.99, 180, 2010], [24.00, 450, 2020], [15.75, 320, 2018]]
)

# 1. Vector Operations:

# a) Create a vector 'prices' containing the prices of all books.
prices = books[:, 0]

# b) Create a vector 'pages' containing the number of pages of all books.
pages = books[:, 1]

# c) Calculate the average price of the books.  Store it in 'average_price'.
average_price = np.mean(prices)
print(f"Average price: {average_price}")

# d) Add 2 Euros to the price of each book. Store the updated prices in 'updated_prices'.
updated_prices = prices + 2
print(f"Updated prices: {updated_prices}")

# e)  Subtract 50 pages from each book.  Store the updated page counts in 'updated_pages'.
updated_pages = pages - 50
print(f"Updated pages: {updated_pages}")

# 2. Matrix Operations:

# a) Create a new matrix 'books_2018_or_later' containing only the books published in 2018 or later.
#    (Hint: Use boolean indexing)
years = books[:, 2]
is_2018_or_later = years >= 2018
books_2018_or_later = books[is_2018_or_later]
print(f"Books from 2018 or later:\n{books_2018_or_later}")

# b) Increase the price of all books in the original 'books' matrix by 10%.
#    Store the result back in 'books'.
books[:, 0] = books[:, 0] * 1.1
print(f"Books matrix with 10% price increase:\n{books}")

# 3. Combined Operations and Scalars:

# a) Find the maximum number of pages among all books. Store it in 'max_pages'.
max_pages = books[:, 1].max()
print(f"Max pages: {max_pages}")

# b) Find the minimum price among all books. Store it in 'min_price'.
min_price = books[:, 0].min()
print(f"Min price: {min_price}")

# c) Calculate the difference between the maximum and minimum prices. Store in 'price_range'.
price_range = books[:, 0].max() - min_price
print(f"Price Range: {price_range}")

# 4. (Bonus - a bit more challenging):
#    Calculate how many books have *more* pages than the *average* number of pages.
#    Store this count in 'num_books_above_avg_pages'.

is_above_avg_pages = pages > np.mean(pages)
books_above_avg_pages = books[is_above_avg_pages]
num_books_above_avg_pages = len(books_above_avg_pages)
print(f"Number of books with above-average pages: {num_books_above_avg_pages}")
