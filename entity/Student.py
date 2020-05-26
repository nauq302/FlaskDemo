import datetime

class Student:
    id: int
    name: str
    department: str
    birthDate: datetime.date

    def __init__(self, id, name, department, birthDate):
        self.id = id
        self.name = name
        self.department = department
        self.birthDate = birthDate


fakeData: list = [
    Student(1, 'Nguyen Minh Quan', 'Software Engineering', datetime.date(1999, 10, 30)),
    Student(2, 'Tran Hoai Phan Anh', 'Software Engineering', datetime.date(1999, 10, 30))
]

fakeDataCount: int = 2


