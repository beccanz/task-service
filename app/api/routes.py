from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.db.models import Task
from app.api.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()



@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/db-test")
async def db_test(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(1))
    return {"db_ok": result.scalar()}

@router.post(
    "/tasks",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(payload: TaskCreate, db: AsyncSession = Depends(get_db)):
    task = Task(
        title=payload.title,
        description=payload.description,
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


@router.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(task_id: UUID, db: AsyncSession = Depends(get_db)):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("/tasks", response_model=List[TaskRead])
async def list_tasks(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Task).limit(limit).offset(offset)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.patch("/tasks/{task_id}", response_model=TaskRead)
async def update_task(task_id: UUID, payload: TaskUpdate, db: AsyncSession = Depends(get_db)):
    task = await db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title is not None:
        task.title = payload.title

    if payload.description is not None:
        task.description = payload.description

    if payload.status is not None:
        task.status = payload.status  # state machine comes next

    await db.commit()
    await db.refresh(task)
    return task
