from main import dataStore
import time
import requests
import json
ds=dataStore()

ds.directory()
path= ds.path

def create(timeofcreation=time.time()):
    registry_key = input("key :")
    registry_value = input("value :")
    r = requests.get(registry_value).text


    load = json.loads(r)
    load2 = json.dumps(load)
    save = open(path, "a")
    file = open(path, "r")

    key = None
    for line in file:

        fields = line.split("-")
        #len(fields)!=0:

        key = fields[0]

        value = fields[1]


    if str(key).strip(" ") == registry_key:
        print("the key already exits")
    else:
        save = open(path, "a")
        save.write(registry_key)
        save.write("-")
        save.write(load2)
        save.write("+")
        timeinput=(input("enter the time to live :"))
        save.write(timeinput)
        save.write("+")
        save.write(str(int(timeofcreation)))
        save.write("\n")


        #  json object :  https://jsonplaceholder.typicode.com/todos/1

