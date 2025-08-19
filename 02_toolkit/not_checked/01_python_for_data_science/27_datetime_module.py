# 27_datetime_module.py

from datetime import date, time, datetime, timedelta

# =======================================
# 1. INTRODUCTION TO DATETIME OBJECTS
# =======================================
# - The `datetime` module provides classes for working with dates and times.
# - Key object types:
#   - `date`: Represents a date (year, month, day).
#   - `time`: Represents a time (hour, minute, second, microsecond).
#   - `datetime`: A combination of a date and a time.
#   - `timedelta`: Represents a duration or the difference between two dates/times.


# =======================================
# 2. GETTING THE CURRENT DATE AND TIME
# =======================================
# - These functions retrieve the current time from your local system.

# Get the current date and time
now_local = datetime.now()
# Based on your context, this should be around: 2025-06-18 15:49:35

# Get just the current date
today = date.today()

# It's often best practice to work with UTC (Coordinated Universal Time)
# to avoid ambiguity with timezones, especially in web applications.
now_utc = datetime.utcnow()

print("--- Getting Current Time ---")
print(f"Current local datetime: {now_local}")
print(f"Current UTC datetime:   {now_utc}")
print(f"Today's date:           {today}")
print("-" * 30)


# =======================================
# 3. CREATING SPECIFIC DATETIME OBJECTS
# =======================================
# - You can construct objects for any specific date or time.

# Create a specific date
independence_day = date(2026, 7, 4)

# Create a specific datetime
new_years_eve = datetime(year=2025, month=12, day=31, hour=23, minute=59)

print("--- Creating Specific Objects ---")
print(f"US Independence Day 2026: {independence_day}")
print(f"New Year's Eve 2025:      {new_years_eve}")

# Accessing individual components
print(f"The year of New Year's Eve is: {new_years_eve.year}")
print(f"The month is: {new_years_eve.month}")
print(f"The hour is: {new_years_eve.hour}")
print("-" * 30)


# =======================================
# 4. FORMATTING DATES WITH `strftime`
# =======================================
# - `strftime` (string format time) converts a datetime object into a formatted string.
# - You provide a "format code" string to specify the output format.
# - Common format codes:
#   %Y: Year with century (e.g., 2025)
#   %m: Month as a number (01-12)
#   %d: Day of the month (01-31)
#   %H: Hour (24-hour clock, 00-23)
#   %M: Minute (00-59)
#   %S: Second (00-59)
#   %A: Full weekday name (e.g., Wednesday)
#   %B: Full month name (e.g., June)

print("--- Formatting with strftime ---")
print(f"Current datetime: {now_local}")
print(f"ISO Format (YYYY-MM-DD):   {now_local.strftime('%Y-%m-%d')}")
print(f"Readable US Format:        {now_local.strftime('%B %d, %Y')}")
print(f"Full Details:              {now_local.strftime('%A, %B %d at %H:%M:%S')}")
print("-" * 30)


# =======================================
# 5. PARSING STRINGS WITH `strptime`
# =======================================
# - `strptime` (string parse time) is the inverse of strftime.
# - It converts a string into a datetime object, given a matching format code.
# - The format code MUST EXACTLY match the string's format.

date_string = "25/12/2025"
format_code = "%d/%m/%Y"

try:
    parsed_date = datetime.strptime(date_string, format_code)
    print("--- Parsing with strptime ---")
    print(f"Original string: '{date_string}'")
    print(f"Parsed datetime object: {parsed_date}")
    print(f"The parsed day is: {parsed_date.day}")
except ValueError as e:
    print(f"Error parsing date string: {e}")

print("-" * 30)


# =======================================
# 6. DATE ARITHMETIC WITH `timedelta`
# =======================================
# - A `timedelta` object represents a duration.
# - You can add or subtract timedeltas from datetime objects.
# - You can also subtract two dates to get the timedelta between them.

# Create a duration of 30 days and 12 hours
duration = timedelta(days=30, hours=12)

# What is the date and time 30.5 days from now?
future_date = now_local + duration

# How many days until New Year's Day 2026?
new_years_2026 = datetime(2026, 1, 1)
time_until_ny = new_years_2026 - now_local

print("--- Date Arithmetic with timedelta ---")
print(f"Current datetime: {now_local.strftime('%Y-%m-%d %H:%M')}")
print(f"30.5 days from now will be: {future_date.strftime('%Y-%m-%d %H:%M')}")
print(f"Days until New Year's 2026: {time_until_ny.days}")
print(f"Total time until NY 2026: {time_until_ny}")


# --- End of File ---