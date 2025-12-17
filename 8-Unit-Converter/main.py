# Project 8: Unit Converter
# Description: Convert common everyday units (distance, weight, temperature, height, volume, length, speed, area)

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

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def mph_to_kmh(mph):
    return mph * 1.60934

def kmh_to_mph(kmh):
    return kmh / 1.60934

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqm_to_sqft(sqm):
    return sqm / 0.092903

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
    print("9. Liters → Gallons")
    print("10. Gallons → Liters")
    print("11. Inches → Centimeters")
    print("12. Centimeters → Inches")
    print("13. Miles/hour → Kilometers/hour")
    print("14. Kilometers/hour → Miles/hour")
    print("15. Square feet → Square meters")
    print("16. Square meters → Square feet")
    print("17. Quit")

    while True:
        choice = input("Enter choice (1-17): ")

        if choice == "17":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                value = float(input("Enter miles: "))
                print(f"{value} miles = {miles_to_km(value):.2f} km")
            elif choice == "2":
                value = float(input("Enter kilometers: "))
                print(f"{value} km = {km_to_miles(value):.2f} miles")
            elif choice == "3":
                value = float(input("Enter pounds: "))
                print(f"{value} lbs = {pounds_to_kg(value):.2f} kg")
            elif choice == "4":
                value = float(input("Enter kilograms: "))
                print(f"{value} kg = {kg_to_pounds(value):.2f} lbs")
            elif choice == "5":
                value = float(input("Enter Fahrenheit: "))
                print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
            elif choice == "6":
                value = float(input("Enter Celsius: "))
                print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
            elif choice == "7":
                feet = int(input("Enter feet: "))
                inches = int(input("Enter inches: "))
                print(f"{feet} ft {inches} in = {feet_inches_to_cm(feet, inches):.2f} cm")
            elif choice == "8":
                cm = float(input("Enter centimeters: "))
                feet, inches = cm_to_feet_inches(cm)
                print(f"{cm} cm = {feet} ft {inches} in")
            elif choice == "9":
                value = float(input("Enter liters: "))
                print(f"{value} L = {liters_to_gallons(value):.2f} gallons")
            elif choice == "10":
                value = float(input("Enter gallons: "))
                print(f"{value} gallons = {gallons_to_liters(value):.2f} L")
            elif choice == "11":
                value = float(input("Enter inches: "))
                print(f"{value} in = {inches_to_cm(value):.2f} cm")
            elif choice == "12":
                value = float(input("Enter centimeters: "))
                print(f"{value} cm = {cm_to_inches(value):.2f} in")
            elif choice == "13":
                value = float(input("Enter mph: "))
                print(f"{value} mph = {mph_to_kmh(value):.2f} km/h")
            elif choice == "14":
                value = float(input("Enter km/h: "))
                print(f"{value} km/h = {kmh_to_mph(value):.2f} mph")
            elif choice == "15":
                value = float(input("Enter square feet: "))
                print(f"{value} sq ft = {sqft_to_sqm(value):.2f} sq m")
            elif choice == "16":
                value = float(input("Enter square meters: "))
                print(f"{value} sq m = {sqm_to_sqft(value):.2f} sq ft")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    converter()
