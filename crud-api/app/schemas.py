from pydantic import BaseModel

class TareaBase(BaseModel):
    titulo: str
    descripcion: str
    hecha: bool

class TareaCrear(TareaBase):
    pass

class TareaActualizar(TareaBase):
    pass

class Tarea(TareaBase):
    id: int

    class Config:
        orm_mode = True