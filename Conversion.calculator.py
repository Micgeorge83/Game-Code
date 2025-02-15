"""   Unit converting calculator takes in a number (user iputted) and return its converted result based on the selected method options:
Opt 1 
Tempature >
    1. celcius to farhenheit
    2. farhenheit to celcius
Opt 2
Length  
    1. centimeter to inches
    2. inches to feet
    3. feet to miles
    4. miles to to meters
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def centimeter_to_inches(centimeter):
    return centimeter / 2.54

def inches_to_feet(inches):
    return inches / 12

def feet_to_miles(feet):
    return feet / 5280

def miles_to_meters(miles):
    return miles * 1609.344


def main():
    choice = int(input("Welcome! Please choose either 1. Temperature or 2. Length conversions: "))

    if choice == 1:
        print("Temperatures")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        opt1_choice = input("Choose a conversion type: ")
        if opt1_choice == "1":
            celsius = float(input("Enter Temp in Celsius: "))
            print(f"{celsius} C is equal to {celsius_to_fahrenheit(celsius)} F")
        elif opt1_choice == "2":
            fahrenheit = float(input("Enter Temp in Fahrenheit: "))
            print(f"{fahrenheit} F is equal to {fahrenheit_to_celsius(fahrenheit)} C")
        else:
            print("Invalid option, try again!")

    elif choice == 2:
        print("Length")
        print("1. Centimeter to Inches")
        print("2. Inches to Feet")
        print("3. Feet to Miles")
        print("4. Miles to Meters")
        opt2_choice = input("Choose a conversion type: ")
        if opt2_choice == "1":
            centimeter = float(input("Enter length in Centimeters: "))
            print(f"{centimeter} cm is equal to {centimeter_to_inches(centimeter)} in")
        elif opt2_choice == "2":
            inches = float(input("Enter length in Inches: "))
            print(f"{inches} in is equal to {inches_to_feet(inches)} ft")
        elif opt2_choice == "3":
            feet = float(input("Enter length in Feet: "))
            print(f"{feet} ft is equal to {feet_to_miles(feet)} miles")
        elif opt2_choice == "4":
            miles = float(input("Enter length in Miles: "))
            print(f"{miles} mi is equal to {miles_to_meters(miles)} meters")
        else:
            print("Invalid option, try again!")
    else:
        print("Invalid main choice, try again!")

if __name__ == "__main__":
    main()



