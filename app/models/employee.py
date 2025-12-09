from sqlalchemy import Column,Integer,String
from app.db.session import Base

class Employee(Base):
    __tablename__ = "employees"
    
    emp_id = Column(Integer,primary_key=True,index=True)
    emp_firstname = Column(String(30),nullable=False)
    emp_midname = Column(String(30),nullable=True)
    emp_lastname = Column(String(30),nullable=False)
    emp_email = Column(String(50),unique=True,index=True,nullable=False)
    emp_age = Column(Integer,nullable=False)