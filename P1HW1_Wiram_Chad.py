# Chad Wiram
# 2/4/2026
# P1HW1
# Calculate math problems using Python

print()
print("-----Calculating Exponents-----")
print()

#Create exponent variables
base_value = int(input("Enter an integer as the base: "))
exponent_value = int(input("Enter an integer as the exponent: "))


# Exponent results
exponent_result = base_value ** exponent_value

# Print Exponent results
print()
print(f"{base_value} raised to the power of {exponent_value} is {exponent_result} !!")
print()

print("-----Addition and Subtraction-----")
print()
# Add and Subtract variables
start_integer = int(input("Enter a starting integer: "))
add_integer = int(input("Enter an integer to add: "))
subtract_integer = int(input("Enter an integer to subtract: "))

# Add and Subtract results
final_result = start_integer + add_integer - subtract_integer

#Print Add/Subtract 
print()
print(f"{start_integer} + {add_integer} - {subtract_integer} is equal to {final_result}")
print()