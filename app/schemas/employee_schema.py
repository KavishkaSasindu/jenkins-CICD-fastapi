from pydantic import BaseModel,EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    emp_firstname:str
    emp_midname: Optional[str] = None
    emp_lastname:str
    emp_email:EmailStr
    emp_age:int
    
class EmployeeCreate(EmployeeBase):
    pass

class SingleEmployee(EmployeeBase):
    emp_id:int
    
    class Config:
        from_attributes = True
        
class EmployeeUpdate(EmployeeBase):
    emp_firstname:Optional[str] = None
    emp_midname: Optional[str] = None
    emp_lastname:Optional[str] = None
    emp_email:Optional[EmailStr] = None
    emp_age:Optional[int] = None