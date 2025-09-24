from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from models import TaskStatus

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Employee Schemas
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: str
    position: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    position: Optional[str] = None

class Employee(EmployeeBase):
    id: int
    created_at: datetime
    tasks: List["Task"] = []
    
    class Config:
        from_attributes = True

# Task Schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    employee_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[datetime] = None
    employee_id: Optional[int] = None

class Task(TaskBase):
    id: int
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    employee: Optional["EmployeeBase"] = None
    
    class Config:
        from_attributes = True

# Authentication Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Update forward references
Employee.model_rebuild()
Task.model_rebuild()