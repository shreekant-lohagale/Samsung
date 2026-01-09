class School:
    def __init__(self, data):
        self.data = data

    def create_student(self):
        try:
            student_id = int(input("Enter new Student ID: "))
        except ValueError:
            print("(!) Error: ID must be a number.")
            return

        if student_id in self.data:
            print(f"(!) Error: Student ID {student_id} already exists.")
            return
            
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
            
        if not name or not email:
            print("(!) Error: Name and Email cannot be empty.")
            return

        self.data[student_id] = {
            'Name': name,
            'Email': email
        }
        print(f"Success: Student {name} added.")

    def update_student(self):
        try:
            student_id = int(input("Enter Student ID to update: "))
        except ValueError:
            print("(!) Error: ID must be a number.")
            return

        if student_id not in self.data:
            print(f"(!) Error: ID {student_id} not found.")
            return

        print(f"Updating data for: {self.data[student_id]['Name']}")
        print("Leave fields blank to keep current value.")
            
        new_name = input("Enter new Name: ").strip()
        new_email = input("Enter new Email: ").strip()

        if new_name:
            self.data[student_id]['Name'] = new_name
        if new_email:
            self.data[student_id]['Email'] = new_email  
        print("Success: Details updated.")
        
    def delete_student(self):
        try:
            student_id = int(input("Enter Student ID to delete: "))
        except ValueError:
            print("(!) Error: ID must be a number.")
            return

        if student_id in self.data:
            removed = self.data.pop(student_id)
            print(f"Success: Removed {removed['Name']} from system.")
        else:
            print(f"(!) Error: ID {student_id} not found.")

    def display_students(self):
        print("\n--- Current Student List ---")
        if not self.data:
            print("No records found.")
        else:
            print(f"{'ID':<5} | {'Name':<25} | {'Email'}")
            print("-" * 60)
            for s_id, details in self.data.items():
                print(f"{s_id:<5} | {details['Name']:<25} | {details['Email']}")
        print("----------------------------\n")