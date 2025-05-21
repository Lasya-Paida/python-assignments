def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_student_details(name="Alice", age=22, course="Python")