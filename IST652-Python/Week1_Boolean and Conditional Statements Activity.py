# -----------------------------------------------------------------------------------
# Title: 1.4 Boolean and Conditional Statements Activity
# Name: Sathish Kumar Rajendiran
# Date: 06/29/2020
# -----------------------------------------------------------------------------------
# Exercise:
#         Boolean and Conditional Statements Activity

score = input("Enter Score: ")
# print(type(score))
try:
    s = float(score)
    if (s >= 0) and (s <= 1):
        if s >= 0.9:
            print("Grade: A")
        if(s >= 0.8) and (s < 0.9):
            print("Grade: B")
        if (s >= 0.7) and (s < 0.8):
            print("Grade: C")
        if (s >= 0.6) and (s < 0.7):
            print("Grade: D")
        if s < 0.6:
            print("Grade: F")
    else:
        print("Bad Score")

except ValueError:
    print("Bad Score")

# Enter Score: 0.95
# Grade: A

# Enter Score: perfect
# Bad Score

# Enter Score: 10.0
# Bad Score

# Enter Score: 0.75
# Grade: C

# Enter Score: 0.5
# Grade: F
