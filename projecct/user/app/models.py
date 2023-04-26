from tortoise import Model,fields
from tortoise import Tortoise

class Registration(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(100)
    father=fields.CharField(100)
    section=fields.CharField(100)
    roll=fields.CharField(10)
    school=fields.CharField(100)
    address=fields.CharField(100)


Tortoise.init_models(["app.models"],"models")