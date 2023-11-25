import uvicorn
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

from src.urls import API_HOST, API_PORT
from logs.config import logger

from core.logics import *

app = FastAPI()


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = auth_check(form_data)
    logger.info(f"login {user.username}")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    logger.info(f"read_users_me {current_user}")
    return current_user

@app.get("/")
def getAccess():
    return {"msg": "Hello World"}


@app.get("/contacts")
def getContacts():
    result = read_contacts()
    return {"data" : result}

@app.get("/contacts/{contact_name}")
def getContactByName(contact_name: str):
    result = read_contact_by_name(contact_name)
    return result

@app.post("/add_contact")
def addContact(contact: ContactModel):
    result = add_contact(contact)
    logger.info(f"Contact {contact.name} added successful")
    return result

@app.put("/contacts/{contact_name}")
def updateContact(contact_name: str, contact: ContactModel):
    result = edit_contacts(contact_name, contact)
    
    logger.info(f"Contact {contact_name} updated successful")
    return result

@app.delete("/contacts/{contact_name}")
def deleteContact(contact_name: str):
    result = remove_contacts(contact_name=contact_name)
    logger.info(f"Contact {contact_name} deleted successful")
    return result


class ExternalAPI():
    @staticmethod
    def startAPI():
        uvicorn.run("api:app",
                host = API_HOST,
                port = API_PORT,
                reload=True,
                log_level="info")
