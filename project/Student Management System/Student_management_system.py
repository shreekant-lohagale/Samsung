#student management system
#Developed the Student Management System using following operation 
#Create student details
#Update student details
#Delete student details
#Display student details

student_db = {}
def create_student(student_id, name, age, grade):
    student_db[student_id] = {
        'Name': name,
        'Age': age,
        'Grade': grade
    }
    print(f"Student {name} created successfully.")
def update_student(student_id, name=None, age=None, grade=None):
    if student_id in student_db:
        if name:
            student_db[student_id]['Name'] = name
        if age:
            student_db[student_id]['Age'] = age
        if grade:
            student_db[student_id]['Grade'] = grade
        print(f"Student {student_id} updated successfully.")
    else:
        print("Student not found.")
def delete_student(student_id):
    if student_id in student_db:
        del student_db[student_id]
        print(f"Student {student_id} deleted successfully.")
    else:
        print("Student not found.")
def display_students():
    if student_db:
        for student_id, details in student_db.items():
            print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}")
    else:
        print("No students found.")
# Example usage
create_student(1, "Alice", 20, "A")
create_student(2, "Bob", 22, "B")
display_students()
update_student(1, age=21)
display_students()
delete_student(2)
display_students()