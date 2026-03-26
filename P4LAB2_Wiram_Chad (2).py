# Chad Wiram
# 3/23/2026
# P4LAB2
# Using a while loop


# Set choice to be the empty string
choice = ""

#Keep running so long as choice is not no
while choice != "no":
    print()
    user_int = int(input(f"Enter an integer: "))
    print()
    
    if user_int >= 0:
        #show the math
        for i in range(1,13):
            print(f"{user_int} * {i} = {user_int * i}")
    else:
        print("This program does not handle negative numbers!!!")
    
    # Allow user to give input on running again
    print()
    choice = input(f"Would  you like to run program again [yes/no]: ")

#Loop breaks here
print()
print("Hope you enjoyed the program, goodbye!")