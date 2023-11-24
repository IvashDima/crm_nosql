from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr
from typing import Dict
# from src.date_format import *


class Base(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    # created: datetime = Field(default_factory=currentdatetime)


class ContactModel(Base):
    name: str = Field(max_length=50)#(max=50)
    gender: str
    age: int
    email: EmailStr

contact_list: Dict[int, ContactModel] = {}



from email_validator import validate_email, EmailNotValidError

email = "my+address@example.org"

try:
  emailinfo = validate_email(email, check_deliverability=False)
  email = emailinfo.normalized
except EmailNotValidError as e:
  print(str(e))