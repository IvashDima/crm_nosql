import uvicorn
from fastapi import FastAPI

from database import CrmDatabase, ContactModel


app = FastAPI()
db = CrmDatabase()

@app.get("/contacts")
def getContacts():
    all_contacts = db.getAllContacts()
    result = []
    for contact in all_contacts:
        del contact["_id"]
        result.append(contact)
    return {"data" : result}

@app.get("/contacts/{contact_name}")
def getContactByName(contact_name: str):
    return db.getContactByName(contact_name).model_dump()

@app.post("/contacts")
def addContact(contact: ContactModel):
    db.insertContact(contact)
    return {"message": "successful"}

@app.put("/contacts/{contact_name}")
def updateContact(contact_name: str, contact: ContactModel):
    db.updateContactByName(contact_name, contact)
    return {"message": "successful"}

@app.delete("/contacts/{contact_name}")
def deleteContact(contact_name: str):
    db.deleteContactByName(contact_name=contact_name)
    return {"message": "successful"}

class ExternalAPI():
    @staticmethod
    def startAPI():
        uvicorn.run("api:app",
                host='0.0.0.0',
                port=4558,
                reload=True,
                log_level="info")
        
# print("test_test_func")
# contacts2 = db.getAllContacts()
# for cont in contacts2:
#     print(cont)
