import os
import json
import time
from datetime import datetime
import requests




class dataStore:
    def __init__(self):
        self.path=None



    def directory(self):
        file_name = input("file name :")
        parent_dir = input("path of directory ex-:'C:/Users/....' :")
        if parent_dir == "":
            parent_dir=("C:/Users/sai.DESKTOP-F5UOO5H/PycharmProjects/work")  #local store


        self.path= os.path.join(parent_dir, file_name)
        with open(self.path,"a+") :
            pass




        print("Directory '% s' created" % file_name)

    def creation(self):



        registry_key = input("key :")
        registry_value = input("value :")
        r = requests.get(registry_value).text

        load = json.loads(r)
        load2 = json.dumps(load)
        save = open(self.path, "a")
        file = open(self.path, "r")

        key = None
        for line in file:
            fields = line.split("-")
            # len(fields)!=0:

            key = fields[0]

            value = fields[1]

        if str(key).strip(" ") == registry_key:
            print("the key already exits")
        else:
            save = open(self.path, "a")
            save.write(registry_key)
            save.write("-")
            save.write(load2)
            save.write("+")
            timeinput = (input("enter the time to live :"))
            save.write(timeinput)
            save.write("+")
            save.write(str(int(time.time())))
            save.write("\n")


    def read(self):




        read_file=str(input("key to read :"))
        save = open(self.path, "a")
        file = open(self.path, "r")

        for line in file:
            fields = line.split("-")
            key = fields[0]
            value = fields[1]


            if str(key).strip(" ") == read_file:
                print("the value of key is :",value)

                timestamp = line.split("+")
                key2 = timestamp[1]
                created_time =int(timestamp[2]) #created time
                print("the time to live :",key2)
                print("time created :",(str().strip("\n")))
                print (created_time)
                current_time=int(time.time()) #current time
                print (current_time)

                time_to_live=(created_time-current_time)
                if time_to_live > int(key2) :
                    print("cannot read, exceed time to live")
                else:
                    print(timestamp[0].split("-")[1])

    def delete(self):
        read_file = str(input("key to delete :"))
        save = open(self.path, "a")
        file = open(self.path, "r")

        for line in file:
            fields = line.split("-")
            key = fields[0]
            value = fields[1]
            if str(key).strip(" ") == read_file:
                timestamp = line.split("+")
                key2 = timestamp[1]
                created_time = int(timestamp[2])  # created time
                current_time = int(time.time())  # current time
                time_to_live = (created_time - current_time)
                if time_to_live > int(key2):
                    print("cannot delete, exceed time to live")
                else:
                    fname = self.path

                    f = open(fname)

                    output = []

                    for line in f:

                        if not read_file in line:
                            output.append(line)

                    f.close()

                    f = open(fname, 'w')

                    f.writelines(output)

                    f.close()

def main():


    ds = dataStore()

    ds.directory()

    while True :
        select = input("choose \n1-create\n2-read\n3-delete\n4-exit:")
        if select == "1":
            ds.creation()
        elif select == "2":

            ds.read()
        elif select == "3":
            ds.delete()
        elif select== "4":
            exit(0)
        else:
            print("enter the correct option")




if __name__ == '__main__':
    main()
