# Chad Wiram
# 2/24/2026
# P2LAB2
# Program using dictionary with key and value pairs

print()

# Dictionary
car_dict = {
"Camaro": 18.21,
"Prius": 52.36,
"ModelS": 110,
"Silverado": 26
}

#Dictionary key variable
keys = car_dict.keys()

print(keys)
print()

# Enter vehicle name
car = input(f"Enter a vehicle to see it's mpg: ")
print()

# Check dictionary for vehicle mpg
if car in keys:
    print(f"The {car} gets {car_dict[car]} mpg.")
    print()

    # Ask for number of miles to drive car
    miles = float(input(f"How many miles will you drive the {car}: "))
    print()

    # Calculate gas needs
    gas = miles / car_dict[car]

    # Display results of gas needed
    print(f"{gas:.2f} gallon(s) of gas are needed to drive the {car} {miles} miles.")
    print()

# Statement if vehicle not in dictonary
else:
    print("Sorry, that vehicle is not in the database!")
