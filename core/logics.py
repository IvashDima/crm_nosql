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


