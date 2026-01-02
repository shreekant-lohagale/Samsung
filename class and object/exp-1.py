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

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
print("Sum:", Math.add(5, 10))

class Employee:
    def __init__(self, name, eid, salary):
        self.name = name
        self.eid = eid
        self.salary = salary
    def __str__(self):
        return f"Employee Name: {self.name}, ID: {self.eid}, Salary: {self.salary}"
    
print((Employee("Alice", 101, 50000)))