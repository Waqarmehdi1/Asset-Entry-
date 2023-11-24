python
class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def highest_grade(self):
        return max(self.grades)

    def lowest_grade(self):
        return min(self.grades)

    def display_data(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade()}")
        print(f"Highest Grade: {self.highest_grade()}")
        print(f"Lowest Grade: {self.lowest_grade()}")