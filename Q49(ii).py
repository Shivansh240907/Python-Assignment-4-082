import Q49
# Student details and marks for 5 subjects (out of 100 each)
student_name = "Shivansh"
subject_marks = [99, 97, 96, 94, 93]

# Use functions from the custom module
total = Q49.calculate_total(subject_marks)
percentage = Q49.calculate_percentage(subject_marks)
grade = Q49.assign_grade(percentage)

# Display the report card
print("--- Student Report Card ---")
print(f"Name       : {student_name}")
print(f"Marks      : {subject_marks}")
print(f"Total      : {total} / {len(subject_marks) * 100}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
