# Chad Wiram
# 2/26/2026
# P2HW2
# Calculating results from a list with width formatting

# Creat list
mod_list = []

print()
# Get variable to get grade from user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

# Append the variable to the list
mod_list.append(mod1)
mod_list.append(mod2)
mod_list.append(mod3)
mod_list.append(mod4)
mod_list.append(mod5)
mod_list.append(mod6)

# Create average variable
mod_avg = sum(mod_list) / len(mod_list)

print("------------Results------------")
print(f"{'Lowest Grade:':<20}{min(mod_list)}")
print(f"{'Highest Grade:':<20}{max(mod_list)}")
print(f"{'Sum of Grades:':<20}{sum(mod_list)}")
print(f"{'Average:':<20}{mod_avg:.2f}")
print('-' * 40)
print()
