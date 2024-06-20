from pydantic import BaseModel, EmailStr

# why install Pydantic  because it helps in Easily manages the Validation in the Schema

# Creates a User Instance

#baseModel is Used to define  data models with Type validation and  serialization in simple and clear manner 
class User(BaseModel):
    username: str  # Tell that username should be string in nature
    email: EmailStr  # using EmailStr  It basically validate that the email is valid or not
    password: str 


class Login(BaseModel):
    email: EmailStr
    password: str


class LinkID(BaseModel):
    username: str
    linked_id: str
