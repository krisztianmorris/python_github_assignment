# Welcome message
print("Welcome to my Python program!")

# Ask user for input
hours = input("How many hours did you study today? ")

# Try to convert input to a number
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate weekly hours
weekly_hours = hours * 7

# Display result
print(f"You are on track to study {weekly_hours} hours this week.")