# Project 6: Unit Converter
# Description: Convert common everyday units (distance, weight, temperature, height)

def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def feet_inches_to_cm(feet, inches=0):
    return (feet * 30.48) + (inches * 2.54)

def cm_to_feet_inches(cm):
    feet = int(cm // 30.48)
    inches = round((cm % 30.48) / 2.54)
    return feet, inches

def converter():
    print("🔄 Welcome to the Unit Converter!")
    print("Choose conversion:")
    print("1. Miles → Kilometers")
    print("2. Kilometers → Miles")
    print("3. Pounds → Kilograms")
    print("4. Kilograms → Pounds")
    print("5. Fahrenheit → Celsius")
    print("6. Celsius → Fahrenheit")
    print("7. Feet/Inches → Centimeters")
    print("8. Centimeters → Feet/Inches")
    print("9. Quit")

    while True:
        choice = input("Enter choice (1-9): ")

        if choice == "9":
            print("Goodbye!")
            break

        try:
            if choice in ["1", "2"]:
                value = float(input("Enter distance: "))
                if choice == "1":
                    print(f"{value} miles = {miles_to_km(value):.2f} km")
                else:
                    print(f"{value} km = {km_to_miles(value):.2f} miles")

            elif choice in ["3", "4"]:
                value = float(input("Enter weight: "))
                if choice == "3":
                    print(f"{value} lbs = {pounds_to_kg(value):.2f} kg")
                else:
                    print(f"{value} kg = {kg_to_pounds(value):.2f} lbs")

            elif choice in ["5", "6"]:
                value = float(input("Enter temperature: "))
                if choice == "5":
                    print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
                else:
                    print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")

            elif choice == "7":
                feet = int(input("Enter feet: "))
                inches = int(input("Enter inches: "))
                print(f"{feet} ft {inches} in = {feet_inches_to_cm(feet, inches):.2f} cm")

            elif choice == "8":
                cm = float(input("Enter height in cm: "))
                feet, inches = cm_to_feet_inches(cm)
                print(f"{cm} cm = {feet} ft {inches} in")

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    converter()
