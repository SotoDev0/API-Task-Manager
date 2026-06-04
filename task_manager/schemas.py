#Validacion de datos que entran y salen de la API
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# --- Usuarios ---
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True


# --- Tareas ---
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True


# --- Auth ---
class Token(BaseModel):
    access_token: str
    token_type: str
