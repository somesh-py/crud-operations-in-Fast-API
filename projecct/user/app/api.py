from fastapi import APIRouter
from .pydentic_models import Reg, Regget, RegUpdate,Regdelete
from .models import Registration

app = APIRouter()


@app.post("/registration/")
async def StudentRegistration(data: Reg):
    if await Registration.filter(roll=data.roll).exists():
        return {"status": False, "messages": "roll number already exists"}
    else:
        data = await Registration.create(name=data.name, father=data.father, section=data.section,
                                         roll=data.roll, school=data.school, address=data.address)
        return data


@app.get("/alldata/")
async def getalldata():
    data = await Registration.all()
    return data


@app.post("/onedata/")
async def getidgate(data: Regget):
    data = await Registration.get(id=data.id)
    return data

@app.put("/update/")
async def updateone(data: RegUpdate):
    data = await Registration.filter(id=data.id).update(name=data.name, father=data.father, section=data.section, roll=data.roll, school=data.school, address=data.address)
    return data

@app.delete("/deleteone/{id}")
async def deleteone(data:Regdelete):
    data=await Registration.filter(id=data.id).delete()
    return {"status":True,"messages":"data deleted sucessfully"}