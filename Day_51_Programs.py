"""
Input:
{
    "Alice": {"Maths": 90, "Science": 80},
    "Bob": {"Maths": 80, "Science": 70}
}
Output:
{"Alice": 85, "Bob": 75}

"""
student_marks = {"Alice": {"Maths": 90, "Science": 80},
                 "Bob": {"Maths": 80, "Science": 70}}
average_marks = {}
for student, marks in student_marks.items():
    marks_list = list(marks.values())
    average = sum(marks_list) / len(marks_list)
    average_marks[student] = average
print(average_marks)
