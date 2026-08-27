#Timothy Duong
#CTC 389 Lab 6

students = ["Andrew", "Brittney", "Carlos", "Diana", "Eric"]

def print_student_list(students):
    index = 0
    for student in students:
        print(index, student)
        index = index + 1

print("Current list of student names:")
print_student_list(students)

print("----------Menu----------")
print("1. Add student to list")
print("2. Modify student name")
print("3. Remove student")
print("------------------------")

option = int(input())

if option == 1:
    name = input("Enter a student name: ")
    students.append(name)
    print("The list of students is now:")
    print_student_list(students)
elif option == 2:
    print_student_list(students)
    index_to_change = int(input("Enter the index of the name you want to modify: "))
    name =  input("Enter a new name for the student: ")
    students[index_to_change] = name
    print("The list of students is now:")
    print_student_list(students)
elif option == 3:
    print_student_list(students)
    index_to_remove = int(input("Enter the index of the name you want to remove: "))
    students.pop(index_to_remove)
    print("The list of students is now:")
    print_student_list(students)
