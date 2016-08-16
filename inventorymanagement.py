#### IMPORT CALLS
import pickle
import os
import time
from datetime import datetime
#-------------------- CLASS DEFINATION --------------------------#

class inventory(object):

    #######################################################################################################################################

    def __init__(self):
        self.product_code = ''
        self.product_name = ''
        self.product_quantity = 0
        self.count = 0
        self.product_SP = 0
        self.product_company = ''
        self.product_VAT = 0
        self.product_minorderquantity = 0
        self.product_addname=''
        self.tempdict={}
        self.globalinventorydatabase1={}
        self.usermainmenuinput_inventory = 0
        self.salespersonid = 0
        self.today = ''

    #######################################################################################################################################

    #######################################################################################################################################

    def addnewproduct(self):

        print '______________________________ Add New Product _______________________________'
        print
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        self.tempdict = {}
        self.product_code = raw_input('Product Code: ')
        self.product_name = raw_input('Product Name: ')
        flag = 0

        if self.existancecheckercode(self.product_code)[0] == False:

            flag = 1

            if self.existancecheckername(self.product_name)[0] == False:

                flag = 2
                self.product_company = raw_input('Product Company Name: ')
                self.product_description = raw_input('Product Description :')
                self.product_quantity = input('Product Quantity: ')
                self.product_SP = input('Product Selling Price: ')
                self.product_VAT = input('Product VAT: ')
                self.tempdict['Code']=self.product_code
                self.tempdict['Description'] = self.product_description
                self.tempdict['Company'] = self.product_company
                self.tempdict['Quantity'] = self.product_quantity
                self.tempdict['SP'] = self.product_SP
                self.tempdict['VAT'] = self.product_VAT
                self.globalinventorydatabase1[self.product_name] = self.tempdict
                choice3 = self.product_name
                for x in globalinventorydatabase:
                    tedict = globalinventorydatabase[x]
                    if x == choice3:
                        print
                        print 'Name :',x
                        for y in tedict:
                            print y,':',tedict[y]
                print
                print 'SUBMENU :-'
                menu = ['1. To confirm addition','2. To reenter product information']
                for hi in menu:
                    print hi
                choice = input('Submenu choice')
                if choice == 1:

                    globalinventorydatabase.update(self.globalinventorydatabase1)
                    pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                    print
                    print 'Product successfully added'

                elif choice == 2:
                    self.addnewproduct()
                else:
                    print 'Wrong choice inputted'
                    self.reedit()
                    if self.reedit() == 2:
                        self.addnewproduct()

        if flag == 0:
            print 'The product code you entered already exists'
            self.reedit()
            if self.reedit() == 2:
                self.addnewproduct()

        elif flag == 1:
            print 'The product name you entered already exists'
            self.reedit()
            if self.reedit() == 2:
                self.addnewproduct()

        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def menu(self):
        mainmenu = ['1. Add Stocks','2. Remove Stocks','3. Add New Product','4. Remove Product','5. Make Sales','6. Edit ',
                    '7. Search Inventory','8. View Inventory','9. Search Sales Records',
                    '10. View full value of stocks','11. To check sales between 2 dates','12. To check sales for a specific date','13. Go Back',
                    '14. To add new customer information','15. To view customer information']
        print
        print '______________________________ Inventory Menu _______________________________'
        print ""
        for choice in mainmenu:
            print choice
        print
        self.usermainmenuinput_inventory = input('Choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14): ')
        print
        if self.usermainmenuinput_inventory == 1:
            self.addstocks()
        elif self.usermainmenuinput_inventory == 2:
            self.removestocks()
        elif self.usermainmenuinput_inventory == 3:
            self.addnewproduct()
        elif self.usermainmenuinput_inventory == 4:
            self.removeproduct()
        elif self.usermainmenuinput_inventory == 6:
            self.editinformation()
        elif self.usermainmenuinput_inventory == 7:
            self.inventorysearch()
        elif self.usermainmenuinput_inventory == 8:
            self.inventorylistout()
        elif self.usermainmenuinput_inventory == 9:
            self.billsearch()
        elif self.usermainmenuinput_inventory == 13:
            pass
        elif self.usermainmenuinput_inventory == 5:
            self.entersales()
        elif self.usermainmenuinput_inventory == 10:
            self.fullvalue()
        elif self.usermainmenuinput_inventory == 11:
            self.salesdates()
        elif self.usermainmenuinput_inventory == 12:
            self.salescheck()
        elif self.usermainmenuinput_inventory == 14:
            self.savecustomerinformation()
        elif self.usermainmenuinput_inventory == 16:
            self.wow()
        elif self.usermainmenuinput_inventory == 15:
            self.viewcustomerinformation()
        else:
            usermainmenuinput_inventory = input('Main menu choice')
            self.transfer(usermainmenuinput_inventory)

    #######################################################################################################################################

    #######################################################################################################################################

    def entersales(self):
        print '______________________________ Enter Sales _______________________________'
        print
        globalemployeedatabase = pickle.load(open("Databases/employeedatabase.db", "rb"))
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        d = globalcompanydatabase['sales']
        self.count = 1
        for x in d:
            self.count = x+1
        print '1. To use existing customer information\n2. To add new customer information'
        choice2 = input('1/2 : ')
        while choice2 not in [1,2]:
            choice2 = input('Choice(1/2): ')
        if choice2 == 2:
            print "Bill Number: ", self.count
            customername = raw_input('Customer Name :')
            customeradd1 = raw_input('Customer Address(Line 1) :')
            customeradd2 = raw_input('Customer Address(Line 2) :')
            customercity = raw_input('Customer City :')
            customerno = raw_input('Customer Phone Number :')
            customeremail = raw_input('Customer Email :')
            print
            print '1. To save this customer information\n2. To continue'
            choice3 = input('Choice(1/2) : ')
            if choice3 == 1:
                tempdict = {}
                tempdict['address1'] = customeradd1
                tempdict['address2'] = customeradd2
                tempdict['City'] = customercity
                tempdict['Phone Number'] = customerno
                tempdict['email'] = customeremail
                globalcompanydatabase['Customers'][customername] = tempdict
                print 'Customer Information saved'
                print

        elif choice2 == 1:
            customername = raw_input('Customer Name :')
            if customername in globalcompanydatabase['Customers']:
                d1 = globalcompanydatabase['Customers'][customername]
                customeradd1 = d1['address1']
                customeradd2 = d1['address2']
                customerno = d1['Phone Number']
                customeremail = d1['email']
                customercity = d1['City']

        tdict = {}
        self.today = time.strftime("%d/%m/%Y")
        tdict['Name'] = customername
        tdict['Address'] = customeradd1 +', ' + customeradd2
        tdict['City'] = customercity
        tdict['Phone Number'] = customerno
        tdict['Email'] = customeremail
        tempdict = {}
        chr = 'Y'
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        self.salespersonid = (input("Employee ID: "))

        if self.salespersonid in globalemployeedatabase:
            tempdict['Salesperson id'] = self.salespersonid
        while self.salespersonid not in globalemployeedatabase:
            print 'Employee id does not exist'
            self.salespersonid = (input("Employee ID: "))
        tempdict['Salesperson id'] = self.salespersonid
        while chr == 'Y':
            prcode = raw_input('Product Code: ')
            d1 = self.existancecheckercode(prcode)
            if d1[0] == True:
                print "Price: ", globalinventorydatabase[d1[1]]['SP']
                quantity = input('Quantity: ')
                if self.quantitychecker(d1[1],quantity) == True:
                        l5.append(d1[1])
                        price = globalinventorydatabase[d1[1]]['SP']
                        l4.append(d1[1])
                        l1.append(prcode)
                        l2.append(quantity)
                        l3.append(price)
                        l6.append(globalinventorydatabase[d1[1]]['Description'])
                else:
                    print 'Stock going negative'
                    self.reedit()
                    if self.reedit() == 2:
                        self.entersales()
            else:
                print 'The product does not exist'
                print '1. To go to main menu\n2. To go to enter customer information again\n3. To continue entering product names'
                choice = input('Choice(1/2/3) : ')
                flag = 0
                while choice != 1 or choice != 2 or choice != 3:
                    if choice == 1:
                        self.menu()
                    elif coice == 2:
                        self.entersales()
                    elif choice == 3:
                        flag = 1
                        break
                    choice = input()
                if flag == 1:
                    continue

            chr = raw_input('Enter more sales? (Y/N): ')
            print
        self.shipping = 0
        print '1. To Enter Shipping and Handling Charges\n2. To not enter Shipping and Handling Charges'
        choice1 = input('Choice(1/2) : ')
        if choice1 == 1:
            self.shipping = input('Enter shipping and handling charges : ')
        tempdict['Customer Information'] = tdict
        tempdict['Product Code'] = l1
        tempdict['Product Name'] = l5
        tempdict['Description'] = l6
        tempdict['Quantity'] = l2
        tempdict['Price'] = l3
        totalprice = 0
        temp = globalcompanydatabase['Customers'][customername]['Salesrecord']
        temp['Bills'].append(self.count)
        for x in range(len(l1)):
            totalprice += l3[x] * l2[x]
        tempdict['Total amount of sales'] = totalprice
        d[self.count] = tempdict
        count1 = 0
        temp['Total sales'] += totalprice + (totalprice * 2 / 100) + self.shipping
        for i in l4:
            globalinventorydatabase[i]['Quantity'] -= l2[count1]
            count1 += 1
        tempdict['Date'] = self.today
        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        pickle.dump(globalcompanydatabase, open("Databases/companymanagement.db", "wb"))
        print 'Database Synced'
        print
        print 'Stocks left after Sales :-'
        for x in range(len(l4)):
            print 'Product Name :',l4[x]
            print 'Stocks :',globalinventorydatabase[l4[x]]['Quantity']
            print
        self.billgeneration()

    #######################################################################################################################################

    #######################################################################################################################################

    def billgeneration(self):
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        d = globalcompanydatabase['sales'][self.count]
        ifile = open("InvoiceTemplate/InvoiceTemplate.txt","r")
        str1 = ifile.readlines()
        ifile.close()
        string = ''
        for x in range(3):
            string += str(str1[x])
        string += d['Customer Information']['Name']
        for x in range(57 - len(globalcompanydatabase['sales'][self.count]['Customer Information']['Name'])):
            string += ' '
        string += str1[3][57:len(str1[3])+1]

        string += d['Customer Information']['Address']
        for x in range(57 - len(d['Customer Information']['Address'])):
            string += ' '
        string += str1[4][57:len(str1[4])+1]

        string += d['Customer Information']['City']
        for x in range(57 - len(globalcompanydatabase['sales'][self.count]['Customer Information']['City'])):
            string += ' '
        string += str1[5][57:len(str1[5])+1]

        string += d['Customer Information']['Phone Number']
        for x in range(57 - len(globalcompanydatabase['sales'][self.count]['Customer Information']['Phone Number'])):
            string += ' '
        string += str1[6][57:len(str1[6])+1]
        string += d['Customer Information']['Email']
        for x in range(57 - len(d['Customer Information']['Email'])):
            string += ' '
        string += str1[7][57:len(str1[7])+1]
        string += str1[8]
        string += str1[9]
        string += 'Invoice Number : ' + str(self.count) + '\n'
        string += 'Date :  ' + self.today + '\n'#str[11]
        for x in range(12,16):
            string += str1[x]
        l = []
        l.append(string)
        totalamount = 0
        for x in range(len(d['Price'])):
            flag = 0
            string = ''
            string += '   '
            string += str(x+1)
            for y in range(3):
                string += ' '
            for z in range(6):
                string += ' '
            string += str(d['Product Code'][x])
            for c in range(10 - len(str(d['Product Code'][x])) ):
                string += ' '

            string100 = []
            if len(d['Description'][x]) <= 36:

                string += str(d['Description'][x])
                for abcd in range(42 - len(str(d['Description'][x]))):
                    string += ' '

            else:
                string100 = d['Description'][x].split()
                string102 = string100[:]
                string101 = ''
                for xy in range(len(string102)):
                    if len(string101 + string102[xy]) >= 36:
                        string += string101
                        string101 = ''
                        break
                    else:

                        string101 += string102[xy] + ' '
                        string100.remove(string102[xy])
                string += ' ' * 7
                flag = 1

            string += str(d['Quantity'][x])
            for ab in range(3 - len(str(d['Quantity'][x])) + 8):
                string += ' '
            string += str(d['Price'][x])
            for abc in range(14 - len(str(d['Price'][x])) + 4):
                string += ' '
            totalprice = d['Quantity'][x] * d['Price'][x]
            string += str(totalprice)
            totalamount += totalprice
            string += '\n'
            if flag != 1:
                l.append(string)
                l.append('\n')
            else:
                l.append(string)
                string101 = ''
                for x in string100:
                    if len(string101 + x) <= 36:
                        string101 += x + ' '
                    else:
                        l.append(' '*23)
                        l.append(string101 + '\n')
                        string101 = x + ' '
                l.append(' '*23)
                l.append(string100[-1] + '\n')
                l.append('\n')

        for hello in range(15,17):
            l.append(str1[hello])

        string = ''
        string += str1[17][0:94]
        string += str(totalamount) + '\n'
        l.append(string)
        string = ''
        string += str(str1[18][0:94])
        string += str(totalamount * 2/100)
        string += '\n'
        l.append(string)
        string = ''
        choice1 = 0
        if self.shipping != 0:
            string += ' ' * 77 + 'Shipping    : Rs.'
            string += str(self.shipping) + '\n'
        l.append(string)
        l.append(str1[19])
        string = ''
        string += str(str1[20][0:94])
        string += str(totalamount + (totalamount * 2/100) + self.shipping)
        string += '\n'
        l.append(string)
        l.append(str1[21])
        for x in range(22,len(str1)):
            l.append(str1[x])
        ifile = open("BillsGenerated/hello2.txt","w")
        ifile.writelines(l)
        ifile.close()
        os.rename('BillsGenerated/hello2.txt',"BillsGenerated/Bill Number- "+ str(self.count)+".txt")
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def billsearch(self):
        print '______________________________ Bill Search _______________________________'
        print
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        billnumber = input('Enter Bill Number : ')
        print
        d = globalcompanydatabase['sales']
        if billnumber in d:
            print 'Bill Number            :',billnumber
            print 'Bill Date              :',d[billnumber]['Date']
            print 'Salesperson id         :',d[billnumber]['Salesperson id']
            print
            print 'Customer Information :-'
            print
            print '    Name                   :',d[billnumber]['Customer Information']['Name']
            print '    Address                :',d[billnumber]['Customer Information']['Address']
            print '    City-Pincode           :',d[billnumber]['Customer Information']['City']
            print '    Phone Number           :',d[billnumber]['Customer Information']['Phone Number']
            print '    Email Address          :',d[billnumber]['Customer Information']['Email']
            print
            print 'Products Sold :-'
            print
            for x in range(len(d[billnumber]['Price'])):
                print '    Product Code           :',d[billnumber]['Product Code'][x]
                print '    Product Name           :',d[billnumber]['Product Name'][x]
                print '    Product Description    :',d[billnumber]['Description'][x]
                print '    Quantity Sold          :',d[billnumber]['Quantity'][x]
                print '    Selling Price          :','Rs.',d[billnumber]['Price'][x]
                print '    Total price            :','Rs.',d[billnumber]['Price'][x] * d[billnumber]['Quantity'][x]
                print
            print 'Total amount of sales  :','Rs.',d[billnumber]['Total amount of sales'] + (d[billnumber]['Total amount of sales'] * 2 / 100 )
        else:
            print 'Bill number does not exist'
            print '1. to go back to main menu\n2. Enter bill number again'
            choice = input('1/2')
            if choice == 1:
                self.menu()
            elif choice == 2:
                self.billsearch()
            else:
                while choice not in [1,2]:
                    print 'Reenter menu choice'
                    choice = input('Choice(1/2) : ')
        self.menu()
    #######################################################################################################################################

    #######################################################################################################################################

    def removeproduct(self):
        print '______________________________ Remove Product _______________________________'
        print
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        submenu3 = ['1. to remove with product name','2. to remove with product code','3. to remove a company']
        for x in submenu3:
            print x
        print
        choice6 = input('Choice(1/2/3) : ')
        if choice6 == 1:
            chr = 'y'
            while chr == 'y':
                name1 = raw_input('Enter product name')
                qwerty = self.existancecheckername(name1)


                if qwerty[0] == True:
                    name2 = raw_input('Reenter product name')
                    if name1 == name2:

                        print 'SUBMENU :-'
                        menu = ['1. To confirm deletion','2. To reenter product information','3. to go to main menu']
                        for hi in menu:
                            print hi
                        choice = input('Choice(1/2/3) : ')
                        if choice == 1:
                            del globalinventorydatabase[name1]
                            pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                            print 'Product with name',name1,'successfully deleted'
                            chr = 'n'
                        elif choice == 2:
                            self.removeproduct()
                        elif choice == 3:
                            self.menu()
                        else:
                            print 'Wrong choice inputted'
                            self.reedit()
                            if self.reedit() == 2:
                                self.removeproduct()

                    else:
                        print 'Entries do not match'
                        self.reedit()
                        if self.reedit() == 2:
                            self.removeproduct()
                else:
                    print 'Product Name does not exist'
                    print '1. To enter product name again\n2. To go back to main menu'
                    asd = input('Choice(1/2) : ')
                    if asd == 1:
                        chr = 'y'
                    else:
                        self.menu()


        elif choice6 == 2:
            code1 = raw_input('Enter product code')
            code2 = raw_input('Reenter product code')
            if code1 == code2:

                d = self.existancecheckercode(code1)
                if d[0] == True:
                    print '1. To confirm deletion\n2. To reenter product information\n3. to go to main menu'
                    choice = input('Choice(1/2/3)')
                    if choice == 1:
                        del globalinventorydatabase[d[1]]
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'Product with code',code1,'successfully deleted'
                    elif choice == 2:
                        self.removeproduct()
                    elif choice == 3:
                        self.menu()
                    else:
                        print 'Wrong choice inputted'
                        self.reedit()
                        if self.reedit() == 2:
                            self.removeproduct()

            else:
                print 'Entries do not match'
        elif choice6 == 3:
            company1 = raw_input('Enter company name')
            company2 = raw_input('Reenter company name')
            if company1 == company2:
                for x in globalinventorydatabase:
                    tdict=globalinventorydatabase[x]
                    if tdict['Company'] == company1:
                        print '1. To confirm deletion\n2. To reenter product information\n3. to go to main menu'
                        choice = input('Choice(1/2/3)')
                        if choice == 1:
                            del globalinventorydatabase[x]
                            pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                            print 'All products with company name',company1,'successfully deleted'
                        elif choice == 2:
                            self.removeproduct()
                        elif choice == 3:
                            self.menu()
                        else:
                            print 'Wrong choice inputted'
                            self.reedit()
                            if self.reedit() == 2:
                                self.removeproduct()
                    break


            else:
                print 'Entries do not match'
        else:
            print 'Wrong submenu choice entered'
            self.reedit()
            if self.reedit() == 2:
               self.removeproduct()
        print
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def inventorylistout(self):
        print '______________________________ Full Inventory _______________________________'
        print
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        for x in globalinventorydatabase:
            tdict = globalinventorydatabase[x]
            print
            print 'Name :',x
            for y in tdict:
                print y,':',tdict[y]

        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def removestocks(self):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        print "_______________________________ Remove Stocks ________________________________"
        print ""
        print '1. Product Code\n2. Product Name\n3. Main Menu'
        print
        choice1 = input('Choice(1/2/3) : ')
        print ""
        while choice1 not in [1,2,3]:
            print 'Incorrect option'
            choice1 = input('Choice(1/2/3) : ')
        if choice1 == 1:
            while True:
                code = raw_input('Product Code: ')
                d = existancecheckercode(code)
                if d[0] == True:
                    d1 = d[1]
                    print "Product Name :",d[1]
                    print 'Current Stock :', globalinventorydatabase[d1]['Quantity']
                    tempstock = input('Stock to be Removed: ')
                    tempstock1 = input('Re-Enter Stock to be Removed: ')
                    if tempstock == tempstock1:
                        globalinventorydatabase[d1]['Quantity'] -= tempstock
                        print 'Inventory has Succesfully been Updated'
                        print 'New stocks :',globalinventorydatabase[d1]['Quantity']
                        break
                else:
                    print "Incorrect Product Code"
                    print ""


        elif choice1 == 2:
            while True:
                name = raw_input('Product Name: ')
                if name in globalinventorydatabase:
                    print 'Current Stock :', globalinventorydatabase[name]['Quantity']
                    adstock = input('Stock to be Removed: ')
                    adstock1 = input('Re-Enter Stock to be Removed: ')
                    if adstock == adstock1:
                        globalinventorydatabase[name]['Quantity'] -= adstock
                        print 'Inventory has Succesfully been Updated'
                        print 'New stocks :',globalinventorydatabase[name]['Quantity']
                        break
                else:
                    print 'Incorrect Product Name'
                    print ""

        elif choice1 == 3:
            self.menu()



        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def addstocks(self):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        print "________________________________ Add Stocks ________________________________"
        print
        response = 'y'
        while response == 'y':
            code = raw_input('Product Code: ')
            d = self.existancecheckercode(code)
            d1 = d[1]
            if d[0] == True:
                print "Product Name :",d[1]
                print 'Current Stock :', globalinventorydatabase[d1]['Quantity']
                print
                tempstock = input('Enter Stocks to be Added    : ')
                tempstock1 = input('Re-Enter Stocks to be  Added: ')
                if tempstock == tempstock1:
                    globalinventorydatabase[d1]['Quantity'] += tempstock
                    print 'Stock Successfully Synced'
                    print 'New stocks :',globalinventorydatabase[d1]['Quantity']
                    response = 'n'
                else:
                    print 'Please Re-Enter'
                    print
            else:
                print 'Incorrect Product Code'
                print

        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def inventorysearch(self):
        print '______________________________ Inventory Search _______________________________'
        print
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        print '1. to search with product name\n2. to search with product code\n3. to search with company name'
        choice2 = input('Choice(1/2/3) : ')
        if choice2 == 1:
            choice3 = raw_input('Enter name of product: ')
            print
            if choice3 in globalinventorydatabase:
                print 'Name :',choice3
                for x in globalinventorydatabase[choice3] :
                    print x,':',globalinventorydatabase[choice3][x]
            else:
                print 'Product does not exist'

        elif choice2 == 2:
            choice4 = raw_input('Enter the product code: ')
            d = self.existancecheckercode(choice4)
            if d[0] == True:
                print 'Name :',d[1]
                for x in globalinventorydatabase[d[1]]:
                    print x,':',globalinventorydatabase[d[1]][x]

        elif choice2 == 3:
            choice7 = raw_input('Enter name of the company: ')
            print
            flag = 0
            for x in globalinventorydatabase:
                tedict = globalinventorydatabase[x]
                if tedict['Company'] == choice7:
                    flag = 1
                    print
                    print 'Name :',x
                    for y in tedict:
                        print y,':',tedict[y]
            if flag == 0:
                print "Company does not exist"
                self.reedit()
                if self.reedit() == 2:
                   self.inventorysearch()
        else:
            print 'Wrong submenu choice entered'
            self.reedit()
            if self.reedit() == 2:
               self.inventorysearch()

        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def existancecheckername(self, id):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        if id in globalinventorydatabase:
            l = []
            l.append(True)
            l.append(id)
        else:
            l = []
            l.append(False)
            l.append('Nonexistant')
            return l

    #######################################################################################################################################

    #######################################################################################################################################

    def existancecheckercode(self,id):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        flag = 0
        for i in globalinventorydatabase:
            id1 = globalinventorydatabase[i]
            if id == id1['Code']:
                flag = 1
                l = []
                l.append(True)
                l.append(i)
                return l

        if flag != 1:
            l = []
            l.append(False)
            l.append('Nonexistant')
            return l

    #######################################################################################################################################

    #######################################################################################################################################

    def editinformation(self):
        print '______________________________ Edit Formation _______________________________'
        print
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        print '1. to edit code\n2. to edit product name\n3. to edit selling price\n4. to edit VAT\n5. to edit product description'

        print
        choice8 = input('Choice(1/2/3/4/5): ')
        if choice8 == 1:
            tempcode = raw_input('Enter original product code: ')
            d = self.existancecheckercode(tempcode)
            if d[0] == True:
                newtempcode = raw_input('Enter the new code: ')
                newtempcode1 = raw_input('Enter the new code: ')
                d1 = self.existancecheckercode(newtempcode)
                if d1[0] == False:
                    if newtempcode == newtempcode1:
                        d2 = globalinventorydatabase[d[1]]
                        d2['Code'] = newtempcode
                        print 'Code successfully changed'
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                    else:
                        print 'Two entries do not match'
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    print 'Entries do not match'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()

            else:
                print 'Product code does not exist'
                self.reedit()
                if self.reedit() == 2:
                    self.editinformation()

        elif choice8 == 2:
            tempname = raw_input('Enter original product name: ')
            d = self.existancecheckername(tempname)
            if d[0] == True:
                newtempname = raw_input('Enter new name: ')
                newtempname1 = raw_input('Reenter new name: ')
                if newtempname1 == newtempname:
                    i = d[1]
                    tempdict = {}
                    tempdict = globalinventorydatabase[i]
                    del globalinventorydatabase[i]
                    globalinventorydatabase.update(tempdict)
                    print 'Name successfully changed'
                    pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                else:
                    print 'Entries do not match'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()

            else:
                 print 'Name entered does not exist'
                 self.reedit()
                 if self.reedit() == 2:
                    self.editinformation()

        elif choice8 == 3:
            globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
            print '1. to edit using code\n2. to edit using product name'
            print
            choice9 = input('Choice(1/2): ')
            if choice9 == 1:
                tempcode = raw_input('Enter original product code: ')
                d = self.existancecheckercode(tempcode)
                if d[0] == True:
                    tempsp = input('Enter new selling price: ')
                    tempsp1 = input('Reenter new selling price: ')
                    print
                    if tempsp == tempsp1:
                        globalinventorydatabase[d[1]]['SP'] = tempsp
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'Selling price successfully changed'
                        print "New Selling Price",tempsp
                    else:
                        print "Entries do not match"
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    'Product with entered code does not exist'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()

            elif choice9 == 2:
                tempname = raw_input('Enter product name: ')
                if tempname in globalinventorydatabase:
                    print 'Current selling price :',globalinventorydatabase[tempname]['SP']
                    tempsp = input('Enter new selling price: ')
                    tempsp1 = input('Reenter new selling price: ')
                    if tempsp == tempsp1:
                        globalinventorydatabase[tempname]['SP'] = tempsp
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'Selling price successfully changed'
                    else:
                        print 'Entries do not match'
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    print 'The entered product name does not exist'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()
            else:
                print 'Wrong choice entered'
                self.reedit()
                if self.reedit() == 2:
                    self.editinformation()

        elif choice8 == 4:
            globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
            print '1. to edit using code\n2. to edit using product name'
            print
            choice9 = input('Choice(1/2): ')
            if choice9 == 1:
                tempcode = raw_input('Enter original product code: ')
                d = self.existancecheckercode(tempcode)
                if d[0] == True:
                    print 'Current VAT :',globalinventorydatabase[d[1]]['VAT'],'%'
                    tempvat = input('Enter new VAT: ')
                    tempvat1 = input('Reenter new VAT: ')
                    print
                    if tempvat == tempvat1:
                        globalinventorydatabase[d[1]]['VAT'] = tempvat
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'VAT successfully changed'
                        print "New VAT",tempvat,'%'
                    else:
                        print "Entries do not match"
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    'Product with entered code does not exist'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()
            elif choice9 == 2:
                tempname = raw_input('Enter product name: ')
                if tempname in globalinventorydatabase:
                    print 'VAT :',globalinventorydatabase[tempname]['VAT']
                    tempvat = input('Enter new VAT: ')
                    tempvat1 = input('Reenter new VAT: ')
                    if tempvat == tempvat1:
                        globalinventorydatabase[tempname]['VAT'] = tempvat
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'VAT successfully changed'
                    else:
                        print 'Entries do not match'
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    print 'The entered product name does not exist'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()
            else:
                print 'Wrong choice entered'
                self.reedit()
                if self.reedit() == 2:
                    self.editinformation()


        elif choice8 == 5:
            globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
            print '1. to edit using code\n2. to edit using product name'
            print
            choice9 = input('Choice(1/2): ')
            if choice9 == 1:
                tempcode = raw_input('Enter original product code: ')
                d = self.existancecheckercode(tempcode)
                if d[0] == True:
                    print 'Current Description :',globalinventorydatabase[d[1]]['Description']
                    tempdes = raw_input('Enter new description: ')
                    tempdes1 = raw_input('Reenter new description: ')
                    print
                    if tempdes == tempdes1:
                        globalinventorydatabase[d[1]]['Description'] = tempdes
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'Descriptione successfully changed'
                        print "New Selling Price : Rs.",tempdes
                    else:
                        print "Entries do not match"
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    'Product with entered code does not exist'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()

            elif choice9 == 2:
                tempname = raw_input('Enter product name: ')
                if tempname in globalinventorydatabase:
                    print 'Current Description :',globalinventorydatabase[tempname]['Description']
                    tempdes = raw_input('Enter new Description: ')
                    tempdes1 = raw_input('Reenter new Description: ')
                    if tempdes == tempdes1:
                        globalinventorydatabase[tempname]['Description'] = tempdes
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'Description successfully changed'
                    else:
                        print 'Entries do not match'
                        self.reedit()
                        if self.reedit() == 2:
                            self.editinformation()
                else:
                    print 'The entered product name does not exist'
                    self.reedit()
                    if self.reedit() == 2:
                        self.editinformation()
            else:
                print 'Wrong choice entered'
                self.reedit()
                if self.reedit() == 2:
                    self.editinformation()
        else:
            print 'Wrong submenu choice entered'
            self.reedit()
            if self.reedit() == 2:
               self.editinformation()

        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def reedit(self):
        submenu5 = ['1. to go back to main menu','2. to go back to submenu']
        print
        for c in submenu5:
            print c
        choic = input('Sub menu choice')
        if choic == 1:
            self.menu()
        elif choic == 2:
            return 2

    #######################################################################################################################################

    #######################################################################################################################################

    def quantitychecker(self,name,quantity):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        if name in globalinventorydatabase:
            if globalinventorydatabase[name]['Quantity'] >= quantity:
                return True
            else:
                print 'Not enough quantity'
    #######################################################################################################################################

    #######################################################################################################################################

    def fullvalue(self):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        fullquantity = 0
        fullprice = 0
        for x in globalinventorydatabase:
            fullquantity += globalinventorydatabase[x]['Quantity']
            fullprice += (globalinventorydatabase[x]['Quantity'] * globalinventorydatabase[x]['SP'])
        print 'Value of all stocks is : Rs.',fullprice
        print 'Quantity of stocks is :',fullquantity,'piece[s]'

    #######################################################################################################################################

    #######################################################################################################################################

    def salesdates(self):
        print '___________________________________ Sales ____________________________________'
        print
        d1 = pickle.load(open("Databases/companymanagement.db", "rb"))
        chr1 = 'y'
        chr2 = 'y'
        chr3 = 'y'
        todate = ''
        while chr3 == 'y':
            while chr1 == 'y':
                fromdate = '12/12/1999'#raw_input('Enter date in the format(From) : DD/MM/YYYY : ')
                if fromdate[0:2].isdigit() and fromdate[2] == '/' and fromdate[3:5].isdigit() and fromdate[5] == '/' and fromdate[6:10].isdigit():
                    if fromdate[0:2] <= '31' and fromdate[3:5] <= '12' and fromdate[6:-1] <= '2016':

                        chr1 = 'n'
                    else:
                        chr1 = 'y'
                        print 'Invalid date'
                        print
                else:
                    chr1 = 'y'
                    print 'Invalid Date'
                    print

            while chr2 == 'y':
                todate = '12/12/2016'#raw_input('Enter date in the format(To) : DD/MM/YYYY : ')
                if todate[0:2].isdigit() and todate[2] == '/' and todate[3:5].isdigit() and todate[5] == '/' and todate[6:10].isdigit():
                    if todate[0:2] <= '31' and todate[3:5] <= '12' and todate[6:10] <= '2016':
                        if  todate[6:10] > fromdate[6:10]:
                            chr2 = 'n'
                            chr3 = 'n'
                            break
                        elif todate[6:10] == fromdate[6:10]:
                            if todate[3:5] > fromdate[3:5]:
                                chr2 = 'n'
                                chr3 = 'n'
                                break
                            elif todate[3:5] == fromdate[3:5]:
                                if todate[0:2] > fromdate[0:2]:
                                    chr2 = 'n'
                                    chr3 = 'n'
                                    break
                                else:
                                    print 'To date entered if before the after date'
                                    print '1. To enter from date again\n2. To enter to date again'
                                    choice = input('1/2 : ')
                                    if choice == 1:
                                        chr3 = 'y'
                                        chr2 = 'y'
                                        chr1 = 'y'
                                    elif choice == 2:
                                        chr2 = 'y'
                            else:
                                print 'To date entered if before the after date'
                                print '1. To enter from date again\n2. To enter to date again'
                                choice = input('1/2 : ')
                                if choice == 1:
                                    chr3 = 'y'
                                    chr2 = 'y'
                                    chr1 = 'y'
                                elif choice == 2:
                                    chr2 = 'y'
                        else:
                            print 'To date entered if before the after date'
                            print '1. To enter from date again\n2. To enter to date again'
                            choice = input('1/2 : ')
                            if choice == 1:
                                chr3 = 'y'
                                chr2 = 'y'
                                chr1 = 'y'
                            elif choice == 2:
                                chr2 = 'y'
                    else:
                        chr2 = 'y'
                        print 'Invalid date'
                        print
                else:
                    chr2 = 'y'
                    print 'Invalid Date'
                    print

        d = d1['sales']
        totalquantity = 0
        totalsales = 0
        billno = []
        date_format = "%d/%m/%Y"
        a = datetime.strptime(fromdate, date_format)
        b = datetime.strptime(todate, date_format)
        e = datetime.strptime(fromdate, date_format)
        delta = b - a
        count = 0
        l = []
        for x in d:
            temp = d[x]['Date']
            c = datetime.strptime(temp, date_format)
            delta1 = c - a
            delta2 = b - c
            delta3 = e - a
            if delta1.days >= delta3.days and delta2.days >= delta3.days:
                totalsales += (d[x]['Total amount of sales'] * 102 / 100)
                totalquantity += sum(d[x]['Quantity'])
                billno.append(x)
                if d[x]['Total amount of sales'] * 102 / 100 > count:
                    temp = []
                    l = []
                    temp.append(d[x]['Customer Information']['Name'])
                    temp.append(d[x]['Total amount of sales'] * 102 / 100)
                    temp.append(x)
                    l.append(temp)
                elif d[x]['Total amount of sales'] * 102 / 100 == count:
                    temp = []
                    temp.append(d[x]['Customer Information']['Name'])
                    temp.append(d[x]['Total amount of sales'] * 102 / 100)
                    temp.append(x)
                    l.append(temp)
        print 'Total Quantity Sold   :',totalquantity,'piece[s]'
        print 'Total Amount of sales :','Rs.',totalsales
        print 'Average sales per day :','Rs.',totalsales / delta.days
        print 'Bill numbers          :',billno[0] , '-' , billno[-1]
        print
        if len(l) >= 1:
            print 'Highest Purchase[s] :-'
            for x in l:
                print '    Bill Number   :',x[2]
                print '    Customer Name :',x[0]
                print '    Total Amount  : Rs.',x[1]
                print

    #######################################################################################################################################

    #######################################################################################################################################


    def salescheck(self):
        print '___________________________________ Sales ____________________________________'
        print
        d1 = pickle.load(open("Databases/companymanagement.db", "rb"))
        chr1 = 'y'
        date = ''
        while chr1 == 'y':
                date = raw_input('Enter date in the format : DD/MM/YYYY : ')
                if date[0:2].isdigit() and date[2] == '/' and date[3:5].isdigit() and date[5] == '/' and date[6:10].isdigit():
                    if date[0:2] <= '31' and date[3:5] <= '12' and date[6:-1] <= '2016':
                        chr1 = 'n'
                    else:
                        chr1 = 'y'
                        print 'Invalid date'
                        print
                else:
                    chr1 = 'y'
                    print 'Invalid Date'
                    print
        d = d1['sales']
        totalquantity = 0
        totalsales = 0
        billno = []
        count = 0
        l = []
        for x in d:
            if d[x]['Date'] == date:
                totalsales += (d[x]['Total amount of sales'] * 102 / 100)
                totalquantity += sum(d[x]['Quantity'])
                billno.append(x)
                if d[x]['Total amount of sales'] * 102 / 100 > count:
                    temp = []
                    l = []
                    temp.append(d[x]['Customer Information']['Name'])
                    temp.append(d[x]['Total amount of sales'] * 102 / 100)
                    temp.append(x)
                    l.append(temp)
                elif d[x]['Total amount of sales'] * 102 / 100 == count:
                    temp = []
                    temp.append(d[x]['Customer Information']['Name'])
                    temp.append(d[x]['Total amount of sales'] * 102 / 100)
                    temp.append(x)
                    l.append(temp)
        print 'Total Quantity Sold   :',totalquantity,'piece[s]'
        print 'Total Amount of sales :','Rs.',totalsales
        if len(billno) > 1:
            print 'Bill numbers          :',billno[0] , '-' , billno[-1]
        elif len(billno) == 1:
            print 'Bill number           :',billno[0]
        else:
            print 'Bill numbers          : None'
        print
        if len(l) >= 1:
            print 'Highest Purchase[s] :-'
            for x in l:
                print '    Bill Number   :',x[2]
                print '    Customer Name :',x[0]
                print '    Total Amount  : Rs.',x[1]
                print

    #######################################################################################################################################

    #######################################################################################################################################

    def savecustomerinformation(self):
        print '________________________________ New Customer _________________________________'
        print
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        del globalcompanydatabase['Customers']['Vishrut Jaipuria']
        customername = raw_input('Customer Name :')
        customeradd1 = raw_input('Customer Address(Line 1) :')
        customeradd2 = raw_input('Customer Address(Line 2) :')
        customercity = raw_input('Customer City :')
        customerno = raw_input('Customer Phone Number :')
        customeremail = raw_input('Customer Email :')
        tempdict = {}
        tempdict['address1'] = customeradd1
        tempdict['address2'] = customeradd2
        tempdict['City'] = customercity
        tempdict['Phone Number'] = customerno
        tempdict['email'] = customeremail
        tempdict['Salesrecord'] = {}
        globalcompanydatabase['Customers'][customername] = tempdict
        print
        print 'Successfully added new customer'
        pickle.dump(globalcompanydatabase, open("Databases/companymanagement.db", "wb"))
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def wow(self):
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        globalcompanydatabase['Customers']['Vishrut']['Salesrecord']['Bills'] = []
        globalcompanydatabase['Customers']['Vishrut']['Salesrecord']['Total sales'] = 0
        pickle.dump(globalcompanydatabase, open("Databases/companymanagement.db", "wb"))
        print 'done wow'

    #######################################################################################################################################

    #######################################################################################################################################

    def viewcustomerinformation(self):
        print '______________________________ Customer Information_______________________________'
        print
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        name = raw_input('Enter customer name: ')
        tempdict = globalcompanydatabase['Customers'][name]
        print 'Name         :',name
        print 'Address      :',tempdict['address1'] + tempdict['address2']
        print 'City         :',tempdict['City']
        print 'Phone Number :',tempdict['Phone Number']
        print 'Email Id     :',tempdict['email']
        print
        print 'Sales Record :-'
        print '    Bill Numbers   :',
        for x in tempdict['Salesrecord']['Bills']:
            print x + ',',
        print
        print '    Total Purchase :',tempdict['Salesrecord']['Total sales']