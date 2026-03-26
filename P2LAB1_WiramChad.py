# Chad Wiram
# 2/16/2026
# P2LAB2
# This lab will calculate diameter, circumference and area of a circle from a library

import math

print()

# Get radius from user as a float
radius = float(input("What is the radius of the circle? "))

print()

# Calculate diameter
diameter = 2 * radius

# Display diameter with 1 decimal place
print(f"The diameter of the circle is {diameter:.1f}")

print()

# Calculate circumference
circumference = 2 * math.pi * radius

# Display the circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}")

print()

# Calculate area
area = math.pi * math.pow(radius, 2)

# Display area with 3 decimal places
print(f"The area of the circle is {area:.3f}")