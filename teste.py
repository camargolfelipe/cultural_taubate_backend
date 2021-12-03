import pymongo
from connection import collection

id = "kaioh@gmail.com"
username = "kaiosantos"
password = "123"

resultado = collection.find_one({"ID":id})  

dbAcc = resultado['ID']
if dbAcc == id:
    print("Ja existe")

cadastro = {"ID": f"{id}", "username": f"{username}","password": f"{password}"}
print(cadastro)
collection.insert_one(cadastro)
#return redirect(url_for("index"))

resultado = collection.find({"ID":f"{id}"})  
def login():
    for i in resultado:
        dbPass = i['password']
        dbAcc = i['ID']
        if dbAcc == id and dbPass == password:
            print("Logado")
        else:
            print("Eroou")
        
        