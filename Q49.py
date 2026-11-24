
def calculate_total(marks):
    """Returns the sum of a list of marks."""
    return sum(marks)

def calculate_percentage(marks, max_marks_per_subject=100):
    """Returns the overall percentage."""
    total_obtained = sum(marks)
    total_maximum = len(marks) * max_marks_per_subject
    return (total_obtained / total_maximum) * 100

def assign_grade(percentage):
    """Returns a letter grade based on the percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
