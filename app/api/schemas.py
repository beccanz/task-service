from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, constr

from app.domain.task_status import TaskStatus



class TaskCreate(BaseModel):
    title: constr(strip_whitespace=True, min_length=1, max_length=255)
    description: Optional[constr(max_length=1000)] = None


class TaskRead(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    title: Optional[constr(strip_whitespace=True, min_length=1, max_length=255)] = None
    description: Optional[constr(max_length=1000)] = None
    status: Optional[TaskStatus] = None

    class Config:
        extra = "forbid"
