from student_system import School

data = {
    1: {'Name': 'Prathamesh Navale', 'Email': 'prathamesh.navale24@pcu.edu.in'},
    2: {'Name': 'Shreekant Lohagale', 'Email': 'shreekant.logahale24@pcu.edu.in'}
}

s = School(data)
while True:
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Create Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display All")
    print("5. Exit")
        
    choice = input("Select operation (1-5): ")

    if choice == '1':
        s.create_student()
    elif choice == '2':
        s.update_student()
    elif choice == '3':
        s.delete_student()
    elif choice == '4':
        s.display_students()
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")