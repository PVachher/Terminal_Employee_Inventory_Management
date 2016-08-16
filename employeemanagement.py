#IMPORT CALLS

import pickle
from inventorymanagement import *
#from fp

# -----------------------------------------------------------------------------#
#                               CLASSES DEFINATION                             #

# EMPLOYEE DEFINATION #
class employee(object):
    def __init__(self):
        self.__first_name = ""
        self.__surname = ""
        self.__address = ""
        self.__city = ""
        self.__product_division = ""
        self.__dobday = 0
        self.__dobmonth = 0
        self.__dobyear = 0
        self.__dojday = 0
        self.__dojmonth = 0
        self.__dojyear = 0
        self.__dojdate = ""
        self.__targets = 0
        self.__bonus = 0
        self.__salary = 60000
        self.__final1 = ""
        self.__final2 = ""

    def valueinput(self):
        self.__first_name = raw_input("1. First Name : ")
        self.__surname = raw_input("2. Surname : ")
        self.__address = raw_input("3. Address : ")
        self.__city = raw_input("4. City : ")
        self.__product_division = raw_input("5. Product Division : ").lower()
        print "6. Date of Birth"
        self.__dobday = input("    Day : ")
        self.__dobmonth = input("    Month : ")
        self.__dobyear = input("    Year : ")
        print "7. Date of Joining"
        self.__dojday = input("    Day : ")
        self.__dojmonth = input("    Month : ")
        self.__dojyear = input("    Year : ")

    def dobconsolidate(self):
        if len(self.__final1) < 3:
            self.__final1 += str(self.__dobday)
            self.__final1 += "/"
            self.__final1 += str(self.__dobmonth)
            self.__final1 += "/"
            self.__final1 += str(self.__dobyear)

    def dojconsolidate(self):
        if len(self.__final2) < 3:
            self.__final2 += str(self.__dojday)
            self.__final2 += "/"
            self.__final2 += str(self.__dojmonth)
            self.__final2 += "/"
            self.__final2 += str(self.__dojyear)

    def generaterecord(self):
        self.dobconsolidate()
        self.dojconsolidate()
        print "1. Name              :", self.__first_name, self.__surname
        print "2. Address           :", self.__address
        print "3. Product Division  :", self.__product_division
        print "4. Date of Birth     :", self.__final1
        print "5. Date of Joining   :", self.__final2
        print "6. Targets Achieved  :", self.__targets
        print "7. Bonus             :", "Rs.", self.__bonus
        print "8. Salary            :", "Rs.", self.__salary

    def patchspot(self):
        return [self.__first_name, self.__first_name + " " + self.__surname, self.__product_division]

    def updatefirstname(self, new):
        self.__first_name = new
    def updatesurname(self,new):
        self.__surname = new
    def updateaddress(self,new):
        self.__address = new
    def updateproduct(self,new):
        self.__product_division = new
    def sale(self,amount,quantity):
        self.__bonus += amount * 0.02
        self.__targets += quantity

# -----------------------------------------------------------------------------#
#                                FUNCTION DEFINATION                           #

# MAIN MENU - 1
def mainmenu1():
    print "_________________________________", "Main Menu", "_________________________________"
    print ""
    print "1. Employee Management"
    print "2. Inventory Management"
    print "0. Exit"
    print ""
    a = input("Choice(1/2/0): ")
    return a

# MAIN MENU - 2
def mainmenu2():
    print "____________________________", "Employee Directory", "____________________________"
    print ""
    print "1. Add New Employee"
    print "2. Show Employee Records"
    print "3. Search Employee Directory"
    print "4. Delete Employee Record"
    print "5. Modify Employee Record"
    print "0. Return to Main Menu"
    print ""
    a = input("Choice(1/2/3/4/5/0): ")
    return a

# MAIN MENU - 3
def mainmenu3():
    print "____________________________", "Employee Search", "____________________________"
    print ""
    print "1. Search By User ID"
    print "2. Search By Name"
    print "3. Search By Product Division "
    print "0. Return to Previous Menu "
    print ""
    a = input("Choice(1/2/3/0): ")
    return a

# SUB MENU - 1
def submenu1():
    print "____________________________", "Modifying Employee Credentials", "____________________________"
    print ""
    print "Enter 1 to modify First Name"
    print "Enter 2 to modify Surname"
    print "Enter 3 to modify Address"
    print "Enter 4 to modify Product Division"
    print "0. Return to Previous Menu "
    print ""
    a = raw_input("Choice(1,2,3,4/0): ").split()
    return a

# SYNC WITH MASTER DB
def sync(data):
    pickle.dump(data, open("Databases/employeedatabase.db", "wb"))

#SEARCH
def searchid(userid):
    details = masterdatabase[userid]
    details.generaterecord()


# -----------------------------------------------------------------------------#
#                             MASTER WORKSPACE                                 #


while True:
    print ""
    mainmenu1var = mainmenu1()
    # OPTION 1 - MAIN MENU 1
    if mainmenu1var == 1:
        while True:
            masterdatabase = pickle.load(open("Databases/employeedatabase.db","rb"))
            print ""
            mainmenu2var = mainmenu2()


            # OPTION 1 - MAIN MENU 2
            if mainmenu2var == 1:
                a = input("How many Employees do you wish to add? ")
                while a != 0:
                    a -= 1
                    print ""
                    b = input("Employee ID: ")
                    if b in masterdatabase :
                        print "Error, The Employee ID is already taken"
                        a += 1
                        continue
                    c = employee()
                    c.valueinput()
                    masterdatabase[b] = c
                sync(masterdatabase)
                print "Employee Credentials synced with Database"


            # OPTION 2 - MAIN MENU 2
            elif mainmenu2var == 2:
                for counter in masterdatabase:
                    print ""
                    print ".............................................................................."
                    print ""
                    print "Employee ID:", counter
                    (masterdatabase[counter]).generaterecord()

            # OPTION 3 - MAIN MENU 2
            elif mainmenu2var == 3:
                while True:
                    mainmenu3var = mainmenu3()
                    # OPTION 1 - MAIN MENU 3
                    if mainmenu3var == 1:
                        userid = input("Enter User ID of the Employee: ")
                        if userid not in masterdatabase:
                            print ""
                            print ".............................................................................."
                            print "                     No Employee with this User ID"
                            print ".............................................................................."
                            print ""
                        else:
                            print ""
                            print ".............................................................................."
                            print "Employee ID:", userid
                            searchid(userid)
                            print ".............................................................................."
                            print ""

                    # OPTION 2 - MAIN MENU 3
                    elif mainmenu3var == 2:
                        username = raw_input("Enter Name of the Employee: ")
                        flag = 0
                        for counter in masterdatabase:

                            if (masterdatabase[counter]).patchspot()[0].lower() == username.lower() or (masterdatabase[counter]).patchspot()[1].lower() == username.lower():
                                print ".............................................................................."
                                print ""
                                print "User ID:", counter
                                (masterdatabase[counter]).generaterecord()
                                print ""
                                flag = 1
                        if flag == 0:
                            print ""
                            print "The Employee with name", username, "does not exist in the master database"
                            print ""


                    # OPTION 3 - MAIN MENU 3
                    elif mainmenu3var == 3:
                        productdiv = raw_input("Enter Product Division: ")
                        flag = 0
                        for counter in masterdatabase:

                            if (masterdatabase[counter]).patchspot()[2].lower() == productdiv.lower():
                                print ".............................................................................."
                                print ""
                                print "User ID:", counter
                                (masterdatabase[counter]).generaterecord()
                                print ""
                                flag = 1
                        if flag == 0:
                            print ""
                            print "The Product Division", productdiv, "does not exist in the master database"
                            print ""

                    # OPTION 0 - MAIN MENU 3
                    elif mainmenu3var == 0:
                        break

                    # Else Condition - Main
                    else:
                        print ""
                        print "Incorrect Option entered!"
                        print ""

            # OPTION 4 - MAIN MENU 2
            elif mainmenu2var == 4:
                userid = input("Enter User ID of Employee to be Deleted: ")
                if userid not in masterdatabase:
                    print ""
                    print ".............................................................................."
                    print "                     No Employee with this User ID"
                    print ".............................................................................."
                    print ""
                else:
                    print ""
                    print "Found Employee with ID:", userid
                    query = raw_input("Are you sure that you want to delete the following Employee? ")
                    if query == 'Y' or query == 'y' or query == "Yes" or query == "yes":
                        del masterdatabase[userid]
                    print ""
                sync(masterdatabase)

            elif mainmenu2var == 5:
                userid = input("Enter User ID of the Employee: ")
                if userid not in masterdatabase:
                    print ""
                    print ".............................................................................."
                    print "                     No Employee with this User ID"
                    print ".............................................................................."
                    print ""
                else:
                    print ""
                    submenu1var = submenu1()
                    if submenu1var == '0':
                        break
                    for counter in submenu1var:
                        if counter == '1':
                            updatedname = raw_input("Enter updated First Name: ")
                            masterdatabase[userid].updatefirstname(updatedname)
                        elif counter == '2':
                            updatedsurname = raw_input("Enter updated Surname: ")
                            masterdatabase[userid].updatesurname(updatedsurname)
                        elif counter == '3':
                            updatedaddress = raw_input("Enter updated Address: ")
                            masterdatabase[userid].updateaddress(updatedaddress)
                        elif counter == '4':
                            updatedproduct = raw_input("Enter updated Product Division: ")
                            masterdatabase[userid].updateproduct(updatedproduct)

                    sync(masterdatabase)
                    print "Employee Credentials updated in Database"
            elif mainmenu2var == 0:
                break
            else:
                print ""
                print "Incorrect Option entered!"
                print ""

    elif mainmenu1var == 2:
        a = inventory()
        a.menu()

