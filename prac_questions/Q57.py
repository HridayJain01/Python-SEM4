def second_lowest_total_marks(students):
    # Sort the students based on total marks
    sorted_students = sorted(students, key=lambda x: sum(x[1]))

    # Find the second lowest total marks
    lowest_total_marks = sorted_students[0][1]
    for student in sorted_students:
        if sum(student[1]) > lowest_total_marks:
            return sum(student[1])

# Input the number of students
num_students = int(input("Enter the number of students: "))

# Input names and marks of each student
students = []
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    marks = list(map(int, input(f"Enter the marks of student {i+1} (space-separated): ").split()))
    students.append((name, marks))

# Find the second lowest total marks
second_lowest_marks = second_lowest_total_marks(students)

# Print the result
print("Second lowest total marks of any student(s):", second_lowest_marks)
