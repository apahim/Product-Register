import sqlite3
import os
import time


class manager:
    def __init__(self):
        self.store = ""
        self.model = ""
        self.serial_number = ""

    def add(self):
        running = True
        while running:
            print("---------------ADD A PRODUCT---------------")
            self.store = input("Store :")
            time.sleep(0.2)
            self.model = input("Model :")
            time.sleep(0.2)
            self.serial_number = input("Serial_Number :")
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO products\
                           (Store, Model, Serial_Number )VALUES(?,?,?)""",
                           (self.store, self.model, self.serial_number))
            db.commit()
            add_more = input("Would you like to do another register? (Y/N):")
            if add_more == "y".lower():
                continue
            else:
                db.close()
                running = False
                print("Thank you for add your product!")
                time.sleep(2)
                self.menu()

    def update(self):
        pass

    def remove(self):
        pass

    def get_list(self):
        count = 0
        count_2 = 0
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("cls")
        print("---------------Regiters---------------")
        time.sleep(5)
        cursor.execute("SELECT store, model, serial_number FROM products")
        results = cursor.fetchall()
        print(results)
        time.sleep(0.50)

    def terminate(self):
        pass

    def menu(self):
        print("---------------MENU---------------")
        print("1 :) Add")
        print("2 :) Update")
        print("3 :) Remove")
        print("4 :) List")
        print("5 :) Terminate")

        opt = input("Choose a option: ")
        if opt == 1:
            self.add()

        elif opt == 2:
            self.update()

        elif opt == 3:
            self.remove()

        elif opt == 4:
            self.get_list()

        elif opt == 5:
            self.terminate()

        else:
            opt > 5
            print("Type a number between 1 and 5")
            self.menu()

    def main(self):
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(3)
            print("DataBase Connected")
            time.sleep(3)
            self.menu()

        else:
            print("DataBase does not exist")
            time.sleep(3)
            print("Creating the DataBase")
            db = sqlite3.connect("connection")
            time.sleep(3)

            cursor = db.cursor()
            cursor.execute("""CREATE TABLE products
                            (store TEXT, model TEXT, serial_number TEXT)""")

            print("Connection already Created")
            time.sleep(3)
            print("Database created sucessfuly")
        self.menu()


products_manager = manager()
products_manager.main()
