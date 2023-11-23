from core.models import ContactModel
from pymongo import MongoClient


class CrmDatabase:
    # mongo_uri = "mongodb://localhost:27017/crm_database.db"
    # mongodb+srv://admin:Password123@mycluster.zvhn1zi.mongodb.net/?retryWrites=true&w=majority
    # mongodb+srv://admin:Password123@localhost/?retryWrites=true&w=majority
    client = MongoClient("localhost", 27017)#(mongo_uri)
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


    # result = contacts_collection.insert_one({
    #         "name": "test4",
    #         "gender": "male",
    #         "age": 20,
    #         "email": "t4@com"
    #     })
    # print(result)

    # result = contacts_collection.replace_one({"name": "test2"},{
    #         "name": "test3",
    #         "gender": "female",
    #         "age": 22,
    #         "email": "t3@i.com"
    #     })
    # print(result)

    # result = contacts_collection.delete_one({"name": "test1"})
    # print(result)

    # print("STATUS!!!\n")
    # contacts1 = contacts_collection.find({})
    # for cont in contacts1:
    #     print(cont)

    # contacts = contacts_collection.find({"name":"test2"})
    # for cont in contacts:
    #     print(cont)

    
# print("test_func")
# contacts2 = CrmDatabase().getAllContacts()
# for cont in contacts2:
#     print(cont)