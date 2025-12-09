from fastapi import APIRouter,HTTPException,status
from app.services import employee_service
from app.schemas import employee_schema
from sqlalchemy.orm import Session
from app.db.session import get_db
from fastapi.params import Depends

router = APIRouter(prefix="/employee",tags=["employee"])

@router.post("/", response_model=employee_schema.SingleEmployee, status_code=status.HTTP_201_CREATED)
def create_employee_endpoint( emp_data:employee_schema.EmployeeCreate, db:Session = Depends(get_db)):
    return employee_service.create_employee(emp_data,db)

@router.get("/", response_model=list[employee_schema.SingleEmployee],status_code=status.HTTP_200_OK)
def get_all_employee_endpoint( db:Session = Depends(get_db)):
    return employee_service.all_employee(db)

@router.get("/{id}", response_model=employee_schema.SingleEmployee, status_code=status.HTTP_200_OK)
def employee_by_id( id:int, db:Session = Depends(get_db)):
    employee = employee_service.get_employee_by_id(id,db)
    
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user found with this id {id}"
        )
    
    return employee
    
@router.put("/{id}",response_model=employee_schema.SingleEmployee, status_code=status.HTTP_200_OK)
def update_employee_data( id:int, emp_data:employee_schema.EmployeeUpdate, db:Session = Depends(get_db)):
    updated_employee = employee_service.update_employee(id,emp_data,db)
    
    if not updated_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Can not update the existing data of {id}"
        )
        
    return updated_employee

@router.delete("/{id}", response_model=employee_schema.SingleEmployee, status_code=status.HTTP_200_OK)
def delete_employee_end( id:int, db:Session = Depends(get_db)):
    result = employee_service.delete_employee(id,db)
    return result