from core.models import ContactModel
from pymongo import MongoClient


class CrmDatabase():
    client = MongoClient("localhost", 27017)
    database = client.crm_database

    contacts_collection = database.contacts
    # contracts_collection = database.contracts
    # genders_collection = database.genders
    # leads_collection = database.leads
    # products_collection = database.products
    # users_collection = database.users

    def __init__(self) -> None:
        pass

    def insertContact(self, contact: ContactModel):
        return self.contacts_collection.insert_one({
            "name": contact.name,
            "gender": contact.gender,
            "age": contact.age,
            "email": contact.email
        })

    def getAllContacts(self):
        return self.contacts_collection.find({})

    def getContactByName(self, contact_name: str):
        print(self.contacts_collection.find({"name": contact_name}))
        c = self.contacts_collection.find({"name": contact_name})[0]
        print(c)
        return ContactModel(
                name=c["name"],
                gender=c["gender"],
                age=c["age"],
                email=c["email"])

    def updateContactByName(self, contact_name: str, contact: ContactModel):
        return self.contacts_collection.replace_one({"name": contact_name},{
            "name": contact.name,
            "gender": contact.gender,
            "age": contact.age,
            "email": contact.email
        })

    def deleteContactByName(self, contact_name: str):
        return self.contacts_collection.delete_one({"name": contact_name})