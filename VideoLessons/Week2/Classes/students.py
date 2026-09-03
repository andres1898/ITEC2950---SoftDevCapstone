class Student:
    #initializer values
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    #what will be show in the print()
    def __str__(self):
        return f'{self.name}, {self.school_id}, gpa: {self.gpa}'


alex = Student('Alex', 'abcd', 3.0)
print(alex)

alex.gpa = 4
print(alex)