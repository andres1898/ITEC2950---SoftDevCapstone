from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'{self.name}, {self.school_id}, gpa: {self.gpa}'

alex = Student('Alex', 'abcd', 3.7)
print(alex)
print(alex.gpa)
