class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("\n========== Student Details ==========")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.calculate_grade()}")
        print("=====================================")

    def calculate_grade(self):
        if self.marks < 0 or self.marks >100:
            raise  ValueError("Marks must be between 0 and 100.")
        if self.marks >=90:
            return "A+"
        elif self.marks >=80:
            return "A"
        elif self.marks >=70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >=50:
            return "D"
        else:
            return "Fail"
        
