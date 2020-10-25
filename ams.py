import sys
import os
import shutil

class User: 
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype

    def printdetails(self):
        print("\nUsername: " + self.username + "\nUsertype: " + self.usertype)

class Admin(User):
    def __init__(self, username):
        User.__init__(self, username, "admin")
        self.privilege = 3
    
    def printdetails(self):
        print("\nAdmin Name: " + self.username + "\nUsertype: " + self.usertype)

    def backup(self):
        bkp_fileloc = "D:\\AMS\\1.txt"
        bkp_choice = int(input("cloud or physical (0/1): "))
        if bkp_choice == 0:
            a1.cloud_backup(bkp_fileloc)
        if bkp_choice == 1: 
            a1.physical_backup(bkp_fileloc)
            
    def cloud_backup(self, bkp_fileloc):
        pass
    
    def physical_backup(self, bkp_fileloc):
        bkp_location = input("Enter path for storing the backup: ")
        shutil.copy(bkp_fileloc, bkp_location)
        print("Back up (physical) was successfull!")
    
    def mod_user(self, user):
        def add_user(self):
            addusers()

        def del_user(self, user):
            pass

        def upd_user(self, user):
            pass

class Vendor(User):
    def __init__(self, username, ven_id = -1):
        User.__init__(self, username, "vendor")
        self.vendorid = ven_id
        self.privilege = 1

    def printdetails(self):
        print("\nVendor Name: " + self.username + "\nVendor ID: " + self.vendorid + "\nUsertype: " + self.usertype)

    def perform_service(self):
        pass

    def get_payment(self):
        pass

class Employee(User):
    def __init__(self, username, emp_id = -1):
        User.__init__(self, username, "employee")
        self.employeeid = emp_id
        self.privilege = 1

    def printdetails(self):
        print("\nEmployee Name: " + self.username + "\nEmployee ID: " + self.employeeid + "\nUsertype: " + self.usertype)

    def fill_timecard(self):
        pass

    def get_salary(self):
        pass

class Owner(User):
    def __init__(self, username, apt = -1):
        User.__init__(self, username, "owner")
        self.aptno = apt
        self.privilege = 2

    def printdetails(self):
        print("\nOwner Name: " + self.username + "\nApartment Number: " + self.aptno + "\nUsertype: " + self.usertype)

    def paydues(self):
        def paynow(amt):
            pass

        def payadv(amt):
            def pay_quaterly(amt):
                pass

            def pay_semiannual(amt):
                pass

            def pay_annual(amt):
                pass

class Resident(User):
    def __init__(self, username, apt = -1):
        User.__init__(self, username, "resident")
        self.aptno = apt
        self.privilege = 2

    def printdetails(self):
        print("\nResident Name: " + self.username + "\nApartment Number: " + str(self.aptno) + "\nUsertype: " + self.usertype)

    def paydues(self):
        def paynow(amt):
            pass

        def payadv(amt):
            def pay_quaterly(amt):
                pass

            def pay_semiannual(amt):
                pass

            def pay_annual(amt):
                pass

class Treasurer(User):
    def __init__(self, username):
        User.__init__(self, username, "treasurer")
        self.privilege = 3

    def printdetails(self):
        print("\nTreasurer Name: " + self.username + "\nUsertype: " + self.usertype)
    
    def generate_incomereport(self):
        pass

    def generate_expensereport(self):
        pass

    def generate_defualterlist(self):
        pass

    def pay(self):
        def pay_emp(self, emp):
            pass

        def pay_vendor(self, vendor):
            pass
    
    def collect(self):
        def collect_dues(self, res_own):
            pass

def addusers():
    for x in range(0,n):
        name = input("Enter user name: ")
        type1 = input("Enter your user type: ")
        
        if type1 == "admin":
            userlist.append(Admin(name))
        if type1 == "resident":
            apt = int(input("Enter apartment number: "))
            userlist.append(Resident(name,apt))
        if type1 == "owner":
            apt = input("Enter apartment number: ")
            userlist.append(Owner(name,apt))
        if type1 == "vendor":
            vid = input("Enter vendor id: ")
            userlist.append(Vendor(name,vid))
        if type1 == "employee":
            eid = input("Enter employee id: ")
            userlist.append(Employee(name,eid))
        if type1 == "treasurer":
            userlist.append(Treasurer(name))

def displayallusers():
    for x in userlist:
        x.printdetails()

# Testing purpoese ....

userlist = []
selection = -1
while(selection != 0):
    print("1.Add user\n2.Display users\n3.Backup\n0.Exit")
    selection = int(input("Enter your choice: "))
    if selection == 0:
        sys.exit
    if selection == 1:
        n = int(input("Enter number of users: "))
        addusers()
    if selection == 2:
        displayallusers()
    if selection == 3:
        a1 = Admin("admin1")
        a1.backup()
