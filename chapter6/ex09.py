# A certain CS professor gives 100 point exams that are graded  of the scale below.

# A : 90-100
# B : 80-89
# C : 70-79
# D : 60-69
# F : 0-59

# Write a function, grade(score) that returns a letter grade for a score.

def grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80 and score < 90:
        print("Grade: B")
    elif score >= 70 and score < 80:
        print("Grade: C")
    elif score >= 60 and score < 70:
        print("Grade: D")
    else:
        print("Grade: F")   

def main():
    score = int(input("What was your score? "))
    grade(score)
main()
