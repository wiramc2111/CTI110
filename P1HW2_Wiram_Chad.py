# Chad Wiram
# 2/4/2026
# P1HW2
# Program for Travel Budget

# Program purpose
print()
print("This program calculates and displays travel expenses")
print()

#Create budget questions
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))

#Calculations based off questions
remain_balance = budget - (gas + accomodation + food)

print()
print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomadation: {accomodation}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remain_balance}")
print()