import json

from fastapi import FastAPI
from mongoengine import connect

from models import Employee, NewEmployee

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)


@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/get_all_employees')
def get_all_employees():
    employees = json.loads(Employee.objects().to_json())
    return {"employees": employees}


@app.post("/add_employee")
def add_employee(employee: NewEmployee):
    new_employee = Employee(
        emp_id=employee.emp_id,
        name=employee.name,
        age=employee.age,
        teams=employee.teams)

    new_employee.save()
    return {"message": "Employee add successfully"}
