from fastapi import FastAPI
from app.controller.employee_router import router as emp_router

app = FastAPI(title="crud_empl")

app.include_router(emp_router)
