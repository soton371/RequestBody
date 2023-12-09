from mongoengine import Document, StringField, IntField, ListField
from pydantic import BaseModel
from fastapi import Body


class Employee(Document):
    emp_id = IntField()
    name = StringField()
    age = IntField()
    teams = ListField()


# for add new employee
class NewEmployee(BaseModel):
    emp_id: int
    name: str
    age: int = Body(None, gt=18)
    teams: list
