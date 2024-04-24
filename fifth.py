# Initialize variables for total grade points and number of courses
total_grade_points = 0
num_courses = 6

# Initialize list to store grades and corresponding grade points
grades = []
grade_points = []

# Take input for grades of 6 courses
for i in range(num_courses):
    grade = input("Enter the grade for course {}: ".format(i+1))
    grades.append(grade)

# Assign grade points based on grades
for grade in grades:
    if grade == 'A+' or 'a+':
        grade_points.append(4.0)
    elif grade == 'A' or 'a':
        grade_points.append(4.0)
    elif grade == 'A-' or 'a-':
        grade_points.append(3.7)
    elif grade == 'B+' or 'b+':
        grade_points.append(3.3)
    elif grade == 'B' or 'b':
        grade_points.append(3.0)
    elif grade == 'B-' or 'b-':
        grade_points.append(2.7)
    elif grade == 'C+' or 'c+':
        grade_points.append(2.3)
    elif grade == 'C' or 'c':
        grade_points.append(2.0)
    elif grade == 'C-' or 'c-':
        grade_points.append(1.7)
    elif grade == 'D' or 'd':
        grade_points.append(1.0)
    else:
        grade_points.append(0.0)

# Calculate total grade points
total_grade_points = sum(grade_points)

# Calculate GPA for the semester
gpa = total_grade_points / num_courses

# Print the Grade Points and GPA for the semester
print("Total Grade Points for the semester:", total_grade_points)
print("GPA for the semester:", gpa)
