#Created by Aswin KS

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import hold, go_app, run_js
from pymongo import MongoClient
from pywebio.session import hold
import time


# Establish a connection to MongoDB
client = MongoClient('mongodb://db:27017/')
# Access the database and collection
db = client['mydatabase']
collection = db['mycollection']


def button_app():
    put_html(r"""<h1  align="center"><strong> SIMPLE CRUD WEBAPP </strong></h1>""")  # App Name in Main screen

    put_code("This docker container connect to mongodb container running on port : 27017, Created by Aswin KS", 'python')
    put_code("Main aim of this app is to demonstrate how 2 containers communicate", 'python')
    name = input("Enter the name", type="text", required=True)
    age = input("Enter the age", type=NUMBER, required=True)
    country = input("Enter your country", type="text", required=True)
    mail = input("Enter the Email ID", type="text", required=True)
    put_html('<a href="/">Add new Data</a>')
    document = {'name': name, 'age': age, 'country': country,'mail': mail}
    collection.insert_one(document)
    # Adding Progress bar
    put_text(" ")
    put_processbar('bar')
    for i in range(1, 8):
        set_processbar('bar', i / 7)
        time.sleep(0.1)
    view_record()

def view_record():
    # Establish a connection to MongoDB
    client = MongoClient('mongodb://db:27017/')

    # Access the database and collection
    db = client['mydatabase']
    collection = db['mycollection']

    # Retrieve all documents
    documents = collection.find()

    # Create table data
    data = [['Name', 'Age', 'Country', 'Email ID']]
    for document in documents:
        name = document['name']
        age = document['age']
        country = document['country']
        mail = document['mail']
        data.append([name, age, country, mail ])

    # Display the table
    put_table(data)


if __name__ == '__main__':
    start_server(button_app, port=8080)
