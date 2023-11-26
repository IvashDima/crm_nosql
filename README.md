# crm_nosql

# CRM_NOSQL

CRM_NOSQL is a Customer relationship management system, which helps to hold contact's databases and fixes the history of all actions with them. 

# Description:

CRM_NOSQL allows to:
- login by user
- store contact's data in MongoDB database,
- have access via api,
- read, create, edit, delete data.

## Installation

Install the MongoDB: use the [documentation](https://www.mongodb.com/docs/manual/installation/) and follow the tutorial to install MongoDB on your computer based on the operating system you use.

Install the MongoDB shell to be able to interact with the database from a terminal, follow the installation terminal [here](https://www.mongodb.com/docs/mongodb-shell/install/).

Run:
pip install -r requirements.txt

## Usage

1. Run:
python main.py  
to run api server.

2. You can checks methods via  Swagger: 
http://localhost:4558/docs#/

3. Connect to the database from a terminal to check data in MongoDB.
Run the following commands:

mongosh
use CrmDatabase
db.contacts.find()

4. Show log: Log file is located in the root folder of the application with name: my_log_{currentdate}.log.

5. Run TESTs: 
pytest -v test_api.py

## Support

Feel free to contact me by e-mail at dnytsyk@gmail.com if you have any questions related to my project.

## Roadmap

In future releases, I will plan to add features:
- graphic user interface,
- clients products,
- functional users and roles.

## Authors and acknowledgment

I appreciate my teachers in ReDI school teaching me and support while creating the project.