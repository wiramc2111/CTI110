# Chad Wiram
# 2/24/2026
# P2HW1
# Program for Travel Budet with width spacing

# Program purpose
print()
print("This program calculates and displays travel expenses")
print()

#Create budget questions
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))

#Calculations based off questions
remain_balance = budget - (gas + accomodation + food)

print()
print("------------Travel Expenses------------")
print(f"{"Location:":<20s} {destination}")
print(f"{"Initial Budget:":<20s} ${budget:.2f}")
print(f"{"Fuel:":<20s} ${gas:.2f}")
print(f"{"Accomadation:":<20s} ${accomodation:.2f}")
print(f"{"Food:":<20s} ${food:.2f}")
print('-' * 39)
print()
print(f"{"Remaining Balance:":<20s} ${remain_balance:.2f}")
print()