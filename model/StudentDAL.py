from .DB_Context import db

from entity.Student import Student
from datetime import datetime, date, time

collection = db["Students"]

def getAll() -> list:
    students = []

    for d in collection.find():
        students.append(studentDocToStudent(d))

    return students 


def get(id: int) -> Student:
    query = { "id": id }
    doc = collection.find_one(query)
    return studentDocToStudent(doc)


def remove(id: int):
    query = { "id": id }
    collection.delete_one(query)


def update(student: Student):
    query = {
        "name" : student.name,
        "department": student.department,
        "birthDate": datetime.combine(student.birthDate, time()) 
    }
    collection.update_one({"id" : student.id}, {"$set": query})


def insert(name: str, department: str, birthDate: date):
    query = {
        "id": getNextSequence("userid"),
        "name" : name,
        "department": department,
        "birthDate": datetime.combine(birthDate, time()) 
    }
    collection.insert_one(query)


def studentDocToStudent(doc) -> Student:
    return Student(
        id = int(doc["id"]),
        name = doc["name"],
        department = doc["department"],
        birthDate = doc["birthDate"].date()
    )

def getNextSequence(name):
    ret = db["counters"].find_and_modify(
        query = { "_id": name },
        update = { "$inc": { "seq": 1 } }
    )
    return ret["seq"]
