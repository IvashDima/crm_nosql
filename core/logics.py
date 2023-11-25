from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated

from database import CrmDatabase
from core.models import ContactModel, User, UserInDB


db = CrmDatabase()

# class ContactFunctions():
def read_contacts():
    all_contacts = db.getAllContacts()
    result = []
    for contact in all_contacts:
        del contact["_id"]
        result.append(contact)
    return result

def read_contact_by_name(contact_name):
    result = db.getContactByName(contact_name).model_dump()
    return result

def add_contact(contact: ContactModel):
    db.insertContact(contact)
    return {"message": "successful"}

def edit_contacts(contact_name: str, contact: ContactModel):
    db.updateContactByName(contact_name, contact)
    return {"message": "successful"}

def remove_contacts(contact_name: str):
    db.deleteContactByName(contact_name=contact_name)
    return {"message": "successful"}


# class CoreFunctions():
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

def fake_hash_password(password: str):
    return "fakehashed" + password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def auth_check(form_data):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user

