from pydantic import BaseModel, Field

class User(BaseModel):
    #id: int
    #name: str = Field(min_length=5, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)
    #is_active: bool = True

    class Config:
        schema_extra = {
            "example": {
                #"id": 1,
                #"name": "John Doe",
                "email": "",
                "password": "123456"
            }
        }