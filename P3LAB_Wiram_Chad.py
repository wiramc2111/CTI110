# Chad Wiram
# 3/1/2026
# P3LAB
# Determine amount of coins needed for a specified amount

print()
# Get amount of money from user as a float
user_money = float(input(f"Enter the amount of money as a float: $"))

# Move the decimal 2 place to the right to make an int
user_money_int = (user_money * 100)
user_money_int = int(round(user_money_int, 2))

#################################################### DOLLARS
# Use floor division to determine dollars in user_money_int
dollars = user_money_int // 100

# Use modulus division to determine remainer of user_money_int after floor division
user_money_int = user_money_int % 100

#################################################### QUARTERS
# Use floor division to determine quarters in remainder of user_money_int
quarters = user_money_int // 25

# Use floor division to determine quarters in remainder of user_money_int
user_money_int = user_money_int % 25

#################################################### DIMES
# Use floor division to determine dimes in remainder of user_money_int
dimes = user_money_int // 10

# Use modulus division to determine dimes in remainer of user_money_int after floor division
user_money_int = user_money_int % 10

#################################################### NICKELS
# Use floor division to determine nickels in remainder of user_money_int
nickels = user_money_int // 5

# Use modulus division to determine nickels in remainer of user_money_int after floor division
user_money_int = user_money_int % 5

#Determin the pennies
pennies = user_money_int

print()
############## DISPLAY COINS IF NEEDED
if dollars > 0:
    if dollars == 1:
        print(f"{dollars} Dollar")
    if dollars > 1:
        print(f"{dollars} Dollars")
        
if quarters > 0:
    if quarters == 1:
        print(f"{quarters} Quarter")
    if quarters > 1:
        print(f"{quarters} Quarters")
        
if dimes > 0:
    if dimes == 1:
        print(f"{dimes} Dime")
    if dimes > 1:
        print(f"{dimes} Dimes")
        
if nickels > 0:
    if nickels == 1:
        print(f"{nickels} Nickel")
    if nickels > 1:
        print(f"{nickels} Nickels")
        
if pennies > 0:
    if pennies == 1:
        print(f"{pennies} Penny")
    if pennies > 1:
        print(f"{pennies} Pennies")
else:
    print("No Change")
