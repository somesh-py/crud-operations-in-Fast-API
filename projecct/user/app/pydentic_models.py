from pydantic import BaseModel


class Reg(BaseModel):
    name: str
    father: str
    section: str
    roll: str
    school: str
    address: str


class Regget(BaseModel):
    id: int


class RegUpdate(BaseModel):
    id: int
    name: str
    father: str
    section: str
    roll: str
    school: str
    address: str

class Regdelete(BaseModel):
    id:int