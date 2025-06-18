def average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers: return 0
    return sum(numbers) / len(numbers)

# The following block runs only when this script is executed directly
if __name__ == '__main__':
    print("Running math_utils.py as a script.")
    test_data = [1, 2, 3]
    print(f"Testing average function: {average(test_data)}")
