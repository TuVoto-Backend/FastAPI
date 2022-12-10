from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from rich import print
from bson import ObjectId
from enum import Enum
from datetime import date


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class VotoBase(BaseModel):
    dni_votante:str
    dni_candidato:str
    
class VotoCreate(VotoBase):
    pass

class Voto(VotoBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "dni_votante": "77500025",
                "dni_candidato": "72863125"
            }
        }
        



