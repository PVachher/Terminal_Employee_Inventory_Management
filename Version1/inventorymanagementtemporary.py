#### IMPORT CALLS
import pickle
import os

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

    #######################################################################################################################################

    #######################################################################################################################################

    def addnewproduct(self):

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
                self.tempdict['Company']=self.product_company
                self.tempdict['Quantity']=self.product_quantity
                self.tempdict['SP']=self.product_SP
                self.tempdict['VAT']=self.product_VAT
                self.globalinventorydatabase1[self.product_name]=self.tempdict
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
        print 'hi'
        mainmenu = ['1. Add Stocks','2. Remove Stocks','3. Add New Product','4. Remove Product','5. Make Sales','6. Edit ','7. Search Inventory','8. View Inventory','9. Search Sales Records','10. Go Back',]
        print
        print '______________________________ Inventory Menu _______________________________'
        print ""
        for choice in mainmenu:
            print choice
        print
        self.usermainmenuinput_inventory = input('Choice(1/2/3/4/5/6/7/8/9/10): ')
        print

        if self.usermainmenuinput_inventory == 1:
            self.addstocks()
        elif self.usermainmenuinput_inventory == 2:
            self.removestocks()
        elif self.usermainmenuinput_inventory == 3:
            self.addnewproduct()
        elif self.usermainmenuinput_inventory == 4:
            self.removeproduct()
        elif self.usermainmenuinput_inventory == 5:
            self.entersales()
        elif self.usermainmenuinput_inventory == 6:
            self.editinformation()
        elif self.usermainmenuinput_inventory == 7:
            self.inventorysearch()
        elif self.usermainmenuinput_inventory == 8:
            self.inventorylistout()
        elif self.usermainmenuinput_inventory == 9:
            self.billsearch()
        elif self.usermainmenuinput_inventory == 10:
            pass
        else:
            usermainmenuinput_inventory = input('Main menu choice')
            self.transfer(usermainmenuinput_inventory)

    #######################################################################################################################################

    #######################################################################################################################################

    def entersales(self):
        globalemployeedatabase = pickle.load(open("Databases/employeedatabase.db", "rb"))
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        d = globalcompanydatabase['sales']
        self.count = 1
        for x in d:
            self.count = x+1
        print "Bill Number: ", self.count
        print 'hey'
        customername = raw_input('Customer Name :')
        customeradd1 = raw_input('Customer Address(Line 1) :')
        customeradd2 = raw_input('Customer Address(Line 2) :')
        customercity = raw_input('Customer City :')
        customerno = raw_input('Customer Phone Number :')
        customeremail = raw_input('Customer Email :')
        tdict = {}
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
        self.salespersonid = input("Employee ID: ")
        if self.salespersonid in globalemployeedatabase:
            tempdict['Salesperson id'] = self.salespersonid
        while self.salespersonid not in globalemployeedatabase:
            print 'Employee id does not exist'
            self.salespersonid = input("Renter Employee ID: ")
        tempdict['Salesperson id'] = self.salespersonid
        while chr == 'Y':
            prcode = raw_input('Product Code: ')
            d1 = self.existancecheckercode(prcode)
            #print "Price: ", globalinventorydatabase[d1[1]]['SP']
            if d1[0] == True:
                print "Name: ",d1[1]
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
                self.reedit()
                if self.reedit() == 2:
                    self.entersales()

            chr = raw_input('Enter more sales? (Y/N): ')
            print
        tempdict['Customer Information'] = tdict
        tempdict['Product Code'] = l1
        tempdict['Product Name'] = l5
        tempdict['Description'] = l6
        tempdict['Quantity'] = l2
        tempdict['Price'] = l3
        totalprice = 0
        for x in range(len(l1)):
            totalprice += l3[x] * l2[x]
        tempdict['Total amount of sales'] = totalprice
        d[self.count] = tempdict
        count1 = 0
        for i in l4:
            globalinventorydatabase[i]['Quantity'] -= l2[count1]
            count1 += 1
        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        pickle.dump(globalcompanydatabase, open("Databases/companymanagement.db", "wb"))
        print 'hello'
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
        #print "Global Inventory Database"
        #print globalcompanydatabase
        d = globalcompanydatabase['sales'][self.count]
        ifile = open("InvoiceTemplate.txt","r")

        '''try:
            ifile = open("InvoiceTemplate.txt","r")
            while True:
                s = ifile.readline()
                print s
        except IOError:
            print 'hey'
            ifile.close()'''
        str1 = ifile.readlines()
        ifile.close()
        print
        print
        print
        print
        print 'str1'
        #print str1

        string = ''

        for x in range(3):
            string += str(str1[x])

        string += d['Customer Information']['Name']
        for x in range(57 - len(globalcompanydatabase['sales'][self.count]['Customer Information']['Name'])):
            string += ' '
        string += str1[3][57:len(str1[3])+1]
        ##########################################################################################################
        string += d['Customer Information']['Address']
        for x in range(57 - len(d['Customer Information']['Address'])):
            string += ' '
        string += str1[4][57:len(str1[4])+1]
        ##########################################################################################################
        string += d['Customer Information']['City']
        for x in range(57 - len(globalcompanydatabase['sales'][self.count]['Customer Information']['City'])):
            string += ' '
        string += str1[5][57:len(str1[5])+1]
        ##########################################################################################################
        string += d['Customer Information']['Phone Number']
        for x in range(57 - len(globalcompanydatabase['sales'][self.count]['Customer Information']['Phone Number'])):
            string += ' '
        string += str1[6][57:len(str1[6])+1]
        ##########################################################################################################
        string += d['Customer Information']['Email']
        for x in range(57 - len(d['Customer Information']['Email'])):
            string += ' '
        string += str1[7][57:len(str1[7])+1]
        ##########################################################################################################
        string += str1[8]
        string += str1[9]
        string += 'Invoice Number : ' + str(self.count) + '\n'
        string += str1[11]
        for x in range(12,16):
            string += str1[x]
        ##########################################################################################################
        l = []
        l.append(string)
        totalamount = 0
        for x in range(len(d['Price'])):
            tempstr2 = ''
            flag = 0
            tempstr1 = ''
            string = ''
            tempstr = []
            count2 = 0
            tempstr1 = ''
            string += '   '
            string += str(x+1)
            for y in range(3):
                string += ' '
            for z in range(6):
                string += ' '
            string += str(d['Product Code'][x])
            for c in range(10 - len(str(d['Product Code'][x])) ):
                string += ' '
            if len(d['Description'][x]) <= 32:

                string += str(d['Description'][x])
                for abcd in range(32 - len(str(d['Description'][x])) + 10):
                    string += ' '
            else:
                tempstr = d['Description'][x].split()

                count2 = 0
                for i in range(len(tempstr)):
                    tempstr1 += tempstr[i]
                    if len(tempstr1) > 32:
                        count2 = i
                        break
                    else:
                        string += tempstr[i] + ' '
                        tempstr1 += tempstr[i] + ' '
                flag = 1
            string += ' ' * (42 - len(tempstr1))





            string += str(d['Quantity'][x])
            for ab in range(3 - len(str(d['Quantity'][x])) + 6):
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
                tempstr3 = tempstr[count2 + 1:len(tempstr) + 1]
                tempstr4 = tempstr3[:]
                tempstr5 = ''
                while len(tempstr4) != 0:

                    for x in tempstr3:

                        if len(tempstr5) <= 32:
                            tempstr5 += x + ' '
                            tempstr4.remove(x)
                        else:
                            string += tempstr5
                            string += '\n'
                            l.append(string)
                            string = ''
                            tempstr5 = ''
                            string += ' ' * 16
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
        l.append(str1[19])
        string = ''
        string += str(str1[20][0:94])
        string += str(totalamount + (totalamount * 2/100))
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
        globalcompanydatabase = pickle.load(open("Databases/companymanagement.db", "rb"))
        billnumber = input('Enter Bill Number : ')
        d = globalcompanydatabase['sales']
        if billnumber in d:

            print 'Salesperson id',d[billnumber]['Salesperson id']
            print 'Customer Information :-'
            #for x in d[billnumber]['Customer Information']:
            print 'Name :',d[billnumber]['Customer Information']['Name']
            print 'Address :',d[billnumber]['Customer Information']['Address']
            print 'City-Pincode :',d[billnumber]['Customer Information']['City']
            print 'Phone Number :',d[billnumber]['Customer Information']['Phone Number']
            print 'Email Address :',d[billnumber]['Customer Information']['Email']
            print
            print 'Products Sold :-'
            for x in range(len(d[billnumber]['Price'])):
                print 'Product Code :',d[billnumber]['Product Code'][x]
                print 'Product Name :',d[billnumber]['Product Name'][x]
                print 'Product Description :',d[billnumber]['Description'][x]
                print 'Quantity Sold :',d[billnumber]['Quantity'][x]
                print 'Selling Price :',d[billnumber]['Price'][x]
                print 'Total price :',d[billnumber]['Price'][x] * d[billnumber]['Quantity'][x]
                print
            print 'Total amount of sales :',d[billnumber]['Total amount of sales']


        self.menu()
    #######################################################################################################################################

    #######################################################################################################################################

    def removeproduct(self):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        submenu3 = ['1. to remove with product name','2. to remove with product code','3. to remove a company']
        for x in submenu3:
            print x
        print
        choice6 = input('Submenu choice')
        if choice6 == 1:
            name1 = raw_input('Enter product name')
            name2 = raw_input('Reenter product name')
            if name1 == name2:

                print 'SUBMENU :-'
                menu = ['1. To confirm deletion','2. To reenter product information','3. to go to main menu']
                for hi in menu:
                    print hi
                choice = input('Submenu choice')
                if choice == 1:
                    del globalinventorydatabase[name1]
                    pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                    print 'Product with name',name1,'successfully deleted'
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

        elif choice6 == 2:
            code1 = raw_input('Enter product code')
            code2 = raw_input('Reenter product code')
            if code1 == code2:

                d = self.existancecheckercode(code1)
                if d[0] == True:
                    print 'SUBMENU :-'
                    menu = ['1. To confirm deletion','2. To reenter product information','3. to go to main menu']
                    for hi in menu:
                        print hi
                    choice = input('Submenu choice')
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
                        print 'SUBMENU :-'
                        menu = ['1. To confirm deletion','2. To reenter product information','3. to go to main menu']
                        for hi in menu:
                            print hi
                        choice = input('Submenu choice')
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
        print "______________________________ Remove Stocks _______________________________"
        print ""
        self.submenu1 = ['1. Product Code','2. Product Name','0. Previous Menu']
        for wow in self.submenu1:
            print wow
        print
        self.choice1 = input('Choice(1/2/0): ')
        print ""
        if self.choice1 == 1:
            while True:
                self.code = raw_input('Product Code: ')
                d = self.existancecheckercode(self.code)
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


        elif self.choice1 == 2:
            while True:
                self.name = raw_input('Product Name: ')
                self.flag=0
                if self.name in globalinventorydatabase:
                    print 'Current Stock :', globalinventorydatabase[self.name]['Quantity']
                    self.adstock = input('Stock to be Removed: ')
                    self.adstock1 = input('Re-Enter Stock to be Removed: ')
                    if self.adstock == self.adstock1:
                        globalinventorydatabase[self.name]['Quantity'] -= self.adstock
                        print 'Inventory has Succesfully been Updated'
                        print 'New stocks :',globalinventorydatabase[self.name]['Quantity']
                        break
                else:
                    print 'Incorrect Product Name'
                    print ""

        elif self.choice1 == 0:
            self.menu()

        else:
            print 'Incorrect Option'

        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def addstocks(self):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        print "________________________________ Add Stocks ________________________________"
        response = 'y'
        print
        while response == 'y':
            self.code = raw_input('Product Code: ')
            d = self.existancecheckercode(self.code)
            d1 = d[1]
            if d[0] == True:
                print "Product Name :",d[1]
                print 'Current Stock :', globalinventorydatabase[d1]['Quantity']
                tempstock = input('Enter Stock Added: ')
                tempstock1 = input('Re-Enter Stock Added: ')
                if tempstock == tempstock1:
                    globalinventorydatabase[d1]['Quantity'] += tempstock
                    print 'Stock Successfully Synced'
                    print 'New stocks :',globalinventorydatabase[d1]['Quantity']
                    break
                else:
                    print 'Please Re-Enter'
            else:
                print 'Incorrect Product Code'
                print

        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
        self.menu()

    #######################################################################################################################################

    #######################################################################################################################################

    def inventorysearch(self):
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        print
        submenu2 = ['1. to search with product name','2. to search with product code','3. to search with company name']
        for x in submenu2:
            print x

        choice2 = input('Menu Choice: ')
        if choice2 == 1:
            choice3 = raw_input('Enter name of product')
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
            choice7 = raw_input('Enter name of the company')
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
        globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
        submenu4 = ['1. to edit code','2. to edit product name','3. to edit selling price','4. to edit VAT','5. to edit minimum order quantity','6. to edit product description']
        for x in submenu4:
            print x
        print
        choice8 = input('Sub menu choice')
        if choice8 == 1:
            tempcode = raw_input('Enter original product code')
            d = self.existancecheckercode(tempcode)
            if d[0] == True:
                newtempcode = raw_input('Enter the new code')
                newtempcode1 = raw_input('Enter the new code')
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
            tempname = raw_input('Enter original product name')
            d = self.existancecheckername(tempname)
            if d[0] == True:
                newtempname = raw_input('Enter new name')
                newtempname1 = raw_input('Reenter new name')
                if newtempname1 == newtempname:
                    i = d[1]
                    tempdict={}
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
            submenu6 = ['1. to edit using code','2. to edit using product name']
            for x in submenu6:
                print x
            print
            choice9 = input('Submenu choice')
            if choice9 == 1:
                tempcode = raw_input('Enter original product code')
                d = self.existancecheckercode(tempcode)
                if d[0] == True:
                    tempsp = input('Enter new selling price')
                    tempsp1 = input('Reenter new selling price')
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
                tempname = raw_input('Enter product name')
                if tempname in globalinventorydatabase:
                    print 'Current selling price :',globalinventorydatabase[tempname]['SP']
                    tempsp = input('Enter new selling price')
                    tempsp1 = input('Reenter new selling price')
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
            submenu6 = ['1. to edit using code','2. to edit using product name']
            for x in submenu6:
                print x
            print
            choice9 = input('Submenu choice')
            if choice9 == 1:
                tempcode = raw_input('Enter original product code')
                d = self.existancecheckercode(tempcode)
                if d[0] == True:
                    print 'Current VAT :',globalinventorydatabase[d[1]]['VAT']
                    tempvat = input('Enter new VAT')
                    tempvat1 = input('Reenter new VAT')
                    print
                    if tempvat == tempvat1:
                        globalinventorydatabase[d[1]]['VAT'] = tempvat
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'VAT successfully changed'
                        print "New VAT",tempvat
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
                tempname = raw_input('Enter product name')
                if tempname in globalinventorydatabase:
                    print 'VAT :',globalinventorydatabase[tempname]['VAT']
                    tempvat = input('Enter new VAT')
                    tempvat1 = input('Reenter new VAT')
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


        elif choice8 == 6:
            globalinventorydatabase = pickle.load(open("Databases/inventorydatabase.db", "rb"))
            submenu6 = ['1. to edit using code','2. to edit using product name']
            for x in submenu6:
                print x
            print
            choice9 = input('Submenu choice')
            if choice9 == 1:
                tempcode = raw_input('Enter original product code')
                d = self.existancecheckercode(tempcode)
                if d[0] == True:
                    print 'Current Description :',globalinventorydatabase[d[1]]['Description']
                    tempdes = raw_input('Enter new description')
                    tempdes1 = raw_input('Reenter new descriptione')
                    print
                    if tempdes == tempdes1:
                        globalinventorydatabase[d[1]]['Description'] = tempdes
                        pickle.dump(globalinventorydatabase, open("Databases/inventorydatabase.db", "wb"))
                        print 'Descriptione successfully changed'
                        print "New Selling Price",tempdes
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
                tempname = raw_input('Enter product name')
                if tempname in globalinventorydatabase:
                    print 'Current Description :',globalinventorydatabase[tempname]['Description']
                    tempdes = raw_input('Enter new Description')
                    tempdes1 = raw_input('Reenter new Description')
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

