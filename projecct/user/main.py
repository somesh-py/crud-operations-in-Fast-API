from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app import api as StudentAPiroute

app=FastAPI()
app.include_router(StudentAPiroute.app,tags=['apis'])


register_tortoise(
    app,
    db_url="postgres://postgres:root@127.0.0.1/crud_1",
    modules={'models':['app.models']},
    generate_schemas=True,
    add_exception_handlers=True
)