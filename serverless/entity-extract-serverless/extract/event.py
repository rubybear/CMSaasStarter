from pydantic import BaseModel

class Body(BaseModel):
    file: str
    schema_string: str

class Event(BaseModel):
    body: Body
