from uuid import uuid4
from pydantic import BaseModel, Field, EmailStr
from typing import Dict
from src.date_format import datetime, currentdatetime

class Base(BaseModel):
    ext_id: str = Field(default_factory=lambda: uuid4().hex)
    created: datetime = Field(default=currentdatetime)

class ContactModel(Base):
    name: str = Field(max_length=50)#(max=50)
    gender: str
    age: int
    email: EmailStr = Field(examples=['marcelo@mail.com'])

contact_list: Dict[int, ContactModel] = {}

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str


# from email_validator import validate_email, EmailNotValidError

# email = "my+address@example.org"

# try:
#   emailinfo = validate_email(email, check_deliverability=False)
#   email = emailinfo.normalized
# except EmailNotValidError as e:
#   print(str(e))