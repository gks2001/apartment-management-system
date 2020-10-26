import sys
import os
import shutil
import sqlite3

conn = sqlite3.connect('apt.db')
c = conn.cursor()

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
        bkp_fileloc = "D:\\AMS\\apt.db"
        bkp_choice = int(input("cloud or physical (0/1): "))
        if bkp_choice == 0:
            a1.cloud_backup(bkp_fileloc)
        if bkp_choice == 1: 
            self.physical_backup(bkp_fileloc)
            
    def cloud_backup(self, bkp_fileloc):
        pass
    
    def physical_backup(self, bkp_fileloc):
        bkp_location = input("Enter path for storing the backup: ")
        shutil.copy(bkp_fileloc, bkp_location)
        print("Back up (physical) was successfull!")
    
    def mod_user(self):
        print("1.add user\n2.del user\n3.update user")
        mu_choice = int(input("Enter your choice: "))
        if mu_choice == 1:
            n = int(input("Enter number of users: "))
            addusers(n)
        if mu_choice == 2:
            self.del_user()
        if mu_choice == 3:
            self.upd_user()

    def del_user(self):
        del_username = input("Enter username of user to be deleted: ")
        for i in userlist:
            if i.username == del_username:
                userlist.remove(i)
                print("The user has been deleted!")
                break

    def upd_user(self):
        upd_username = input("Enter username of user to be updated: ")
        for i in userlist:
            if i.username == upd_username:
                if i.usertype == "admin":
                    i.username = input("Enter name: ")
                if i.usertype == "treasurer":
                    i.username = input("Enter name: ")
                if i.usertype == "owner":
                    i.username = input("Enter name: ")
                    i.aptno = input("Enter apartment number: ")
                if i.username == "resident":
                    i.username = input("Enter name: ")
                    i.aptno = input("Enter apartment number: ")
                if i.usertype == "vendor":
                    i.username = input("Enter name: ")
                    i.vendorid = input("Enter vendor id: ")
                if i.usertype == "employee":
                    i.username = input("Enter name: ")
                    i.employeeid = input("Enter employee id: ")

class Vendor(User):
    def __init__(self, username, ven_id = -1):
        User.__init__(self, username, "vendor")
        self.vendorid = ven_id
        self.privilege = 1

    def printdetails(self):
        print("\nVendor Name: " + self.username + "\nVendor ID: " + self.vendorid + "\nUsertype: " + self.usertype)

    def perform_service(self):
        service_name = ("Enter the service name: ")
        service_cost = ("Enter the payment amount: ")
        get_payment(service_name, service_cost)

    def get_payment(self, service_name, service_cost):
        pass

class Employee(User):
    def __init__(self, username, emp_id = -1):
        User.__init__(self, username, "employee")
        self.employeeid = emp_id
        self.privilege = 1

    def printdetails(self):
        print("\nEmployee Name: " + self.username + "\nEmployee ID: " + self.employeeid + "\nUsertype: " + self.usertype)

    def fill_timecard(self):
        days = input("How many days have the employee worked this month: ")
        emp_sal = 300 * days
        get_salary(self, emp_sal)

    def get_salary(self, emp_sal):
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

def addusers(n):
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

# Testing purpose ....

userlist = []
selection = -1
while(selection != 0):
    print("1.Add user\n2.Display users\n3.Backup\n4.Admin moduser\n0.Exit")
    selection = int(input("Enter your choice: "))
    if selection == 0:
        sys.exit
    if selection == 1:
        n = int(input("Enter number of users: "))
        addusers(n)
    if selection == 2:
        displayallusers()
    if selection == 3:
        a1 = Admin("admin1")
        a1.backup()
    if selection == 4:
        a1 = Admin("admin1")
        a1.mod_user()
