import uvicorn
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from core.models import ContactModel, User, UserInDB
from core.logics import *
from src.urls import API_HOST, API_PORT

from logs.config import logger

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    logger.info(f"get_current_user {user}")
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
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
