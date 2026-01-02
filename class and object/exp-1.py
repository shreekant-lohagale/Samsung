class Car:
    color = "red"
    brand = "BMW"
    
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")

car = Car()
car.start()
car.stop()

class Student:
    name = "John"
    age = 21
    email_id = "john@example.com"
    
    def study(self):
        print("student is studying")

    def attend_class(self):
        print("student is attending class")

    def take_exam(self):
        print("student is taking exam")
        
student = Student()
student.study()
student.attend_class()
student.take_exam()