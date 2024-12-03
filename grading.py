# Calculating Grades

# Write a program that will average 3 numeric exam grades,
# return an average test score, a corresponding letter grade,
# and a message stating whether the student is passing.

# Average    Grade
# 90+        A
# 80-89      B
# 70-79      C
# 60-69      D
# 0-59       F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

# Taking exam grades as input
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Store grades in a list
grades = [exam_one, exam_two, exam_three]

# Calculate the total sum of grades
total = 0
for grade in grades:
    total += grade

# Calculate average
avg = total / len(grades)

# Determine the letter grade
if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:
    letter_grade = "B"
elif 70 <= avg < 80:
    letter_grade = "C"
elif 60 <= avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print each exam grade
for grade in grades:
    print("Exam: " + str(grade))

# Print average and letter grade
print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Determine if the student is passing or failing
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
