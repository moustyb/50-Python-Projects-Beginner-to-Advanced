# Project 7: Age Calculator
# Description: Calculate a person's age in years, months, and days from their birthdate

from datetime import datetime

def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        return "Error: Please enter date in YYYY-MM-DD format."

    today = datetime.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Adjust if negative values occur
    if days < 0:
        months -= 1
        days += (today.replace(day=1) - birthdate.replace(day=1)).days
    if months < 0:
        years -= 1
        months += 12

    return f"Age: {years} years, {months} months, {days} days"

def age_calculator():
    print("🎂 Welcome to the Age Calculator!")
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    result = calculate_age(birthdate_str)
    print(result)

if __name__ == "__main__":
    age_calculator()
