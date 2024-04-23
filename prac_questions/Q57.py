def second_lowest_total_marks(students):
    # Sort the students based on total marks
    sorted_students = sorted(students, key=lambda x: sum(x[1]))
    print(sorted_students)

    # Find the second lowest total marks
    '''lowest_total_marks = sorted_students[0][1]
    for student in sorted_students:
        if sum(student[1]) > lowest_total_marks:
            return sum(student[1])'''

# Fixed data for quick testing
students = [
    ("Alice", [80, 85, 90]),
    ("Bob", [75, 80, 85]),
    ("Charlie", [70, 75, 80])
]

# Find the second lowest total marks
second_lowest_marks = second_lowest_total_marks(students)

# Print the result
print("Second lowest total marks of any student(s):", second_lowest_marks)
