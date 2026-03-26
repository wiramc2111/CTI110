# Chad Wiram
# 3/25/2026
# P4HW1
# This program will ask for number of scores entered and then calculate average and give letter grade

# Get number of scores to be entered
print()
score_num = int(input(f"How many scores do you want to enter: "))

# List for scores entered
scores = []

# Loop to capture number of scores user entered
print()
for i in range(1, score_num +1):
    while True:
        score =  float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print()
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

# Score variables
low_score = min(scores)
scores.remove(low_score)
avg_score = sum(scores) / len(scores)

# Display results
print()
print("----------------Results-----------------")
print(f"{'Lowest Score':<20}: {low_score:.1f}")
print(f"{'Modified List':20}: {scores}")
print(f"{'Scores Average':20}: {avg_score:.2f}")

# IF statement for letter grade
if 90 <= avg_score <= 100:
    print(f"{'Grade':<20}: A")

elif 80 <= avg_score < 90:
    print(f"{'Grade':<20}: B")

elif 70 <= avg_score < 80:
    print(f"{'Grade':<20}: C")
    
elif 60 <= avg_score < 70:
    print(f"{'Grade':<20}: D")

elif 0<= avg_score < 60:
    print(f"{'Grade':<20}: F")
print('-' * 40)
print()
            