from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    done: int = 0

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
