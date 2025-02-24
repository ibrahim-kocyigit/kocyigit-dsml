# Understanding Expressions and Variables in Data Science

In this example, we’ll explore how variables and mathematical expressions are used to solve real-world problems, such as calculating the cost of participating in a raffle fundraiser. This concept is fundamental in data science, where we often use expressions to model and analyze data.

---

### 1. **The Problem**
A local hospital is holding a raffle fundraiser. The cost of participating is given by the expression:
```
5t + 3
```
Here:
- **t** is a variable representing the number of tickets purchased.
- **5t + 3** calculates the total cost based on the number of tickets.

---

### 2. **Evaluating the Expression**
To find the total cost for different numbers of tickets, we substitute the value of **t** into the expression and compute the result.

#### Example 1: When **t = 1**
```python
t = 1
total_cost = 5 * t + 3  # Expression: 5t + 3
print(total_cost)  # Output: 8
```
**Explanation**:
- Substitute **t = 1** into the expression: `5 * 1 + 3`.
- Perform multiplication first (order of operations): `5 * 1 = 5`.
- Then add 3: `5 + 3 = 8`.

---

#### Example 2: When **t = 8**
```python
t = 8
total_cost = 5 * t + 3  # Expression: 5t + 3
print(total_cost)  # Output: 43
```
**Explanation**:
- Substitute **t = 8** into the expression: `5 * 8 + 3`.
- Perform multiplication first: `5 * 8 = 40`.
- Then add 3: `40 + 3 = 43`.

---

#### Example 3: When **t = 10**
```python
t = 10
total_cost = 5 * t + 3  # Expression: 5t + 3
print(total_cost)  # Output: 53
```
**Explanation**:
- Substitute **t = 10** into the expression: `5 * 10 + 3`.
- Perform multiplication first: `5 * 10 = 50`.
- Then add 3: `50 + 3 = 53`.

---

### 3. **Why This Matters in Data Science**
In data science, we often use expressions like this to:
- **Model relationships**: For example, predicting costs, revenues, or other outcomes based on input variables.
- **Perform calculations**: Automating computations for large datasets.
- **Analyze scenarios**: Evaluating different scenarios by changing the values of variables.

---

### 4. **Python Code Example: Putting It All Together**
Let’s write a Python program to calculate the total cost for multiple values of **t**:

```python
# Function to calculate total cost
def calculate_total_cost(t):
    return 5 * t + 3

# List of ticket quantities
ticket_quantities = [1, 8, 10]

# Calculate and print total cost for each quantity
for t in ticket_quantities:
    total_cost = calculate_total_cost(t)
    print(f"Total cost for {t} ticket(s): ${total_cost}")
```

**Output**:
```
Total cost for 1 ticket(s): $8
Total cost for 8 ticket(s): $43
Total cost for 10 ticket(s): $53
```

---

### 5. **Key Takeaways**
1. **Variables**: Represent values that can change (e.g., **t** for the number of tickets).
2. **Expressions**: Combine variables and constants to perform calculations (e.g., `5t + 3`).
3. **Order of Operations**: Follow rules like multiplication before addition.
4. **Applications in Data Science**: Use expressions to model relationships, automate calculations, and analyze data.

---

### 6. **Real-World Data Science Example**
Imagine you’re analyzing fundraising data for the hospital. You could use a similar expression to calculate total revenue based on the number of tickets sold:
```python
# Example: Calculating total revenue
def calculate_total_revenue(tickets_sold, price_per_ticket, fixed_cost):
    return tickets_sold * price_per_ticket + fixed_cost

tickets_sold = 100
price_per_ticket = 5
fixed_cost = 3
total_revenue = calculate_total_revenue(tickets_sold, price_per_ticket, fixed_cost)
print(f"Total revenue: ${total_revenue}")  # Output: Total revenue: $503
```

This approach can be extended to analyze larger datasets and optimize fundraising strategies.

---

By understanding how to use variables and expressions, you can solve real-world problems and build models for data analysis in data science!