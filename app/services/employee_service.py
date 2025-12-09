from sqlalchemy.orm import Session
from app.schemas import employee_schema
from pydantic import EmailStr
from app.models.employee import Employee
from fastapi import HTTPException,status
from typing import List

def get_employee_by_email( email:EmailStr, db:Session)->Employee:
    employee = db.query(Employee).filter(Employee.emp_email == email).first()
    return employee

def get_employee_by_id( id:int, db:Session)->Employee:
    employee = db.query(Employee).filter(Employee.emp_id == id).first()
    return employee

def create_employee( emp_data:employee_schema.EmployeeCreate, db:Session)->Employee:
    exist_employee = get_employee_by_email(emp_data.emp_email,db)
    
    if exist_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{emp_data.emp_email} is already in the database. Try with different one"
        )
    
    new_employee_data = Employee(**emp_data.model_dump())
    db.add(new_employee_data)
    db.commit()
    db.refresh(new_employee_data)
    return new_employee_data

def all_employee( db:Session)->List[type[Employee]]:
    employees = db.query(Employee).offset(0).all()
    return employees

def update_employee( id:int, emp_data:employee_schema.EmployeeUpdate, db:Session)->Employee:
    exist_employee = get_employee_by_id(id,db)
    
    if not exist_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found to update"
        )
    
    updaet_data = emp_data.model_dump(exclude_unset=True)
        
    for key,value in updaet_data.items():
        setattr(exist_employee,key,value)
        
    db.commit()
    db.refresh(exist_employee)
        
    return exist_employee
        
def delete_employee( id:int, db:Session):
    exist_employee = get_employee_by_id(id,db)
    
    if not exist_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found with this ID"
        )
        
    db.delete(exist_employee)
    db.commit()
    return {
        f"Deleted successfully"
    }