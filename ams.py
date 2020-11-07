import sys
import os
import shutil
import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from os import system, name
from time import sleep
import keyboard

# Inital creation of the database (Only run the first time)
# conn = sqlite3.connect('apt.db')
# c = conn.cursor()
# c.execute("CREATE TABLE apt_tran (months integer, dates integer, years integer, details text, amt real, c_d text)")
# c.execute("CREATE TABLE apt_def (aptno integer, months integer, years integer,details text, paid text)")
# c.execute("CREATE TABLE apt_det (size text, cost real)")                      # Inserting monthly due cost based on size of apt
# c.execute("INSERT INTO apt_det VALUES ('small', '1500')")
# c.execute("INSERT INTO apt_det VALUES ('medium', '2500')")
# c.execute("INSERT INTO apt_det VALUES ('large', '3500')")
# conn.commit()

# User super class
class User: 
    # Constructor
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype

    # Function to print User details
    def printdetails(self):
        print("\nUsername: " + self.username + "\nUsertype: " + self.usertype)

# Admin class
class Admin(User):
    # Constructor
    def __init__(self, username):
        User.__init__(self, username, "admin")      # Calling the super constructor
        self.privilege = 3
    
    # Function to print Admin details
    def printdetails(self):
        print("\nAdmin Name: " + self.username + "\nUsertype: " + self.usertype)

    # Function to get backup choice
    def backup(self):
        clear()
        bkp_fileloc = "D:\\AMS\\apt.db"
        bkp_choice = int(input("cloud or physical (0/1): "))

        if bkp_choice == 0:
            self.cloud_backup(bkp_fileloc)
        if bkp_choice == 1: 
            self.physical_backup(bkp_fileloc)
            
    # Cloud Backup function        
    def cloud_backup(self, bkp_fileloc):
        # google drive api ???
        pass
    
    # Physical Backup
    def physical_backup(self, bkp_fileloc):
        bkp_location = input("Enter path for storing the backup: ")
        shutil.copy(bkp_fileloc, bkp_location)
        print("Back up (physical) was successfull!")
    
    # Modify users
    def mod_user(self):
        clear()
        print("1.add user\n2.del user\n3.update user")
        mu_choice = int(input("Enter your choice: "))

        if mu_choice == 1:
            n = int(input("Enter number of users: "))
            addusers(n)
        if mu_choice == 2:
            self.del_user()
        if mu_choice == 3:
            self.upd_user()

    # Delete users
    def del_user(self):
        if len(userlist) == 1:
                print("There are no other users!")
                return

        del_username = input("Enter username of user to be deleted: ")
        for i in userlist:
            if i.username == del_username:
                userlist.remove(i)
                print("The user has been deleted!")
                break
    
    # Update users
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
                if i.usertype == "resident":
                    i.username = input("Enter name: ")
                    i.aptno = input("Enter apartment number: ")
                if i.usertype == "vendor":
                    i.username = input("Enter name: ")
                    i.vendorid = input("Enter vendor id: ")
                if i.usertype == "employee":
                    i.username = input("Enter name: ")
                    i.employeeid = input("Enter employee id: ")

        print("The user has been updated!")

    # Function to display all users
    def displayallusers(self):
        for x in userlist:
            x.printdetails()  

# Vendor Class
class Vendor(User):
    # Constructor
    def __init__(self, username, ven_id = -1):          # Calling the super constructor
        User.__init__(self, username, "vendor")
        self.vendorid = ven_id
        self.privilege = 1

    # Function to print Vendor details
    def printdetails(self):
        print("\nVendor Name: " + self.username + "\nVendor ID: " + self.vendorid + "\nUsertype: " + self.usertype)

    # Function to collect payment for vendor services
    def perform_service(self):
        clear()
        service_name = input("Enter the service name: ")
        service_cost = float(input("Enter the payment amount: "))
        date = input("Enter date: ")

        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]
        self.get_payment(service_name, service_cost, mon, dat, yea)

    # Function to link to treasurer payment method
    def get_payment(self, service_name, service_cost, mon, dat, yea):
        Treasurer.pay_vendor(self.username, self.vendorid, service_name, service_cost, mon, dat, yea)   #static method call

# Employee Class
class Employee(User):
    # Constructor
    def __init__(self, username, emp_id = -1):
        User.__init__(self, username, "employee")           # Calling the super constructor
        self.employeeid = emp_id
        self.privilege = 1

    # Function to print Employee details
    def printdetails(self):
        print("\nEmployee Name: " + self.username + "\nEmployee ID: " + self.employeeid + "\nUsertype: " + self.usertype)

    # Function to collect employee salary
    def fill_timecard(self):
        clear()
        date = input("Enter date: ")

        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]
        days = int(input("How many days have the employee worked this month: "))

        emp_sal = 300 * days
        self.get_salary(emp_sal, mon, dat, yea)

    # Function to link to treasurer payment method
    def get_salary(self, emp_sal, mon, dat, yea):
        Treasurer.pay_emp(self.username, self.employeeid, emp_sal, mon, dat, yea)       #static method call

# Owner Class
class Owner(User):
    # Constructor
    def __init__(self, username, apt = -1, a_size = None):
        User.__init__(self, username, "owner")          # Calling the super constructor
        self.aptno = apt
        self.privilege = 2
        self.apt_size = a_size
        all_apt.append(apt)

    # Function to print Owner Details
    def printdetails(self):
        print("\nOwner Name: " + self.username + "\nApartment Number: " + self.aptno + "\nUsertype: " + self.usertype)

    # Function to pay monthly dues for apt
    def paydues(self):
        clear()
        adv_time = 0
        months = 0
        cur_mon = 0

        # aptno = int(input("Enter the apartment number: "))
        date = input("Enter date: ")
        # size = input("Enter apartment size(small, medium, large): ")

        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()

        selection = int(input("1.Pay for current month\n2.Pay in advance\nEnter your choice: "))
        if a_size == "small":
            c.execute("SELECT cost FROM apt_det WHERE size = 'small'")
            cost = c.fetchone()
        if a_size == "medium":
            c.execute("SELECT cost FROM apt_det WHERE size = 'medium'")
            cost = c.fetchone()
        if a_size == "large":
            c.execute("SELECT cost FROM apt_det WHERE size = 'large'")
            cost = c.fetchone()

        conn.commit()
        c.close()

        if selection == 1:
            months = 1
            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount[0], mon, dat, yea)
        else:
            adv_time = int(input("1.Quarterly\n2.Semi-Annually\n3.Annually\nEnter your choice: "))
            if adv_time == 1:
                months = 3
            if adv_time == 2:
                months = 6
            if adv_time == 3:
                months = 12

            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount[0], mon, dat, yea)           #static method call

# Resident Class
class Resident(User):
    # Constructor
    def __init__(self, username, apt = -1, a_size = None):
        User.__init__(self, username, "resident")           # Calling the super constructor
        self.aptno = apt
        self.privilege = 2
        self.apt_size = a_size
        all_apt.append(apt)

    # Function to print Resident Details
    def printdetails(self):
        print("\nResident Name: " + self.username + "\nApartment Number: " + str(self.aptno) + "\nUsertype: " + self.usertype)

    # Function to pay monthly for apt
    def paydues(self):
        clear()
        adv_time = 0
        months = 0
        cur_mon = 0

        # aptno = int(input("Enter the apartment number: "))
        date = input("Enter date: ")
        # size = input("Enter apartment size(small, medium, large): ")

        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()

        selection = int(input("1.Pay for current month\n2.Pay in advance\nEnter your choice: "))
        if a_size == "small":
            c.execute("SELECT cost FROM apt_det WHERE size = 'small'")
            cost = c.fetchone()
        if a_size == "medium":
            c.execute("SELECT cost FROM apt_det WHERE size = 'medium'")
            cost = c.fetchone()
        if a_size == "large":
            c.execute("SELECT cost FROM apt_det WHERE size = 'large'")
            cost = c.fetchone()

        conn.commit()
        c.close()

        if selection == 1:
            months = 1
            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount[0], mon, dat, yea)
        else:
            adv_time = int(input("1.Quarterly\n2.Semi-Annually\n3.Annually\nEnter your choice: "))
            if adv_time == 1:
                months = 3
            if adv_time == 2:
                months = 6
            if adv_time == 3:
                months = 12

            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount[0], mon, dat, yea)           #static method call

# Treasurer Class
class Treasurer(User):
    # Constructor
    def __init__(self, username):
        User.__init__(self, username, "treasurer")              # Calling the super constructor
        self.privilege = 3

    # Function to print Treasurer details
    def printdetails(self):
        print("\nTreasurer Name: " + self.username + "\nUsertype: " + self.usertype)
    
    # Function to generate income report
    def generate_incomereport(self):
        clear()
        mon = input("Enter month to generate report for: ")

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("SELECT * FROM apt_tran WHERE months = ? AND c_d = ?", (mon, 'c'))
        records = c.fetchall()
        
        # printrec = ''
        for record in records:
            date = str(record[1]) + "/" + str(record[0]) + "/" + str(record[2])
            print("Date: " + date + "\t\tDeatails: " + str(record[3]) + "\t\tAmount: " + str(record[4]))
            print("\n")
        
        if records == []:
            print("No transactions!")
        
        conn.commit()
        conn.close()

    # Function to generate expense repirt
    def generate_expensereport(self):
        clear()
        mon = input("Enter month to generate report for: ")
        
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("SELECT * FROM apt_tran WHERE months = ? AND c_d = ?", (mon, 'd'))
        records = c.fetchall()
        
        # printrec = ''
        for record in records:
            date = str(record[1]) + "/" + str(record[0]) + "/" + str(record[2])
            print("Date: " + date + "\tDeatails: " + str(record[3]) + "\t\tAmount: " + str(record[4]))
            print("\n")
        
        if records == []:
            print("No transactions!")

        conn.commit()
        conn.close()

    # Function to genertate defaulters list
    def generate_defaulterlist(self):
        clear()
        paid_list = []
        d_list = []
        count = 0

        mon = input("Enter month to generate report for: ")

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        sql = "SELECT * FROM apt_def WHERE months = " + mon
        c.execute(sql)
        records = c.fetchall()
        
        # printrec = ''
        print("Paid List")
        for record in records:
            date = str(record[1]) + "/" + str(record[2])
            # tem = str(record[0]) + str(record[3])
            print("Month: " + date + "\tDetails: " + str(record[3]) + "\t\tPaid: " + str(record[4]))
            paid_list.append(record[0])
        
        print("\nDefaulter List")
        d_list = set(all_apt).difference(paid_list)
        for i in d_list:
            count += 1
            print(str(count) + ". Apartment " + str(i))

        print("There are total " + str(count) + " defaulters for this month")

    # Function to pay employee salary
    @staticmethod
    def pay_emp(name, empid, sal, mon, dat, yea):
        tem = name + " - " + "monthly salary"

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("INSERT INTO apt_tran (dates, months, years, details, amt, c_d) VALUES (?,?,?,?,?,?)",(mon, dat, yea, tem, sal, 'd'))
        
        print("Transaction successful!")

        conn.commit()
        c.close()

    # Function to pay vendor for service performed
    @staticmethod
    def pay_vendor(name, ven_id, service_name, service_cost, mon, dat, yea):
        tem = name + " - " + service_name

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("INSERT INTO apt_tran (dates, months, years, details, amt, c_d) VALUES (?,?,?,?,?,?)",(mon, dat, yea, tem, service_cost, 'd'))
        
        print("Transaction successful!")
        
        conn.commit()
        c.close()
    
    # Function to collect monthly dues form residents and owners for apts
    @staticmethod
    def collect_dues(aptno, time, amt, mon, dat, yea):
        tem = "Monthly dues ("+ str(time) + ") - Aptno: " + str(aptno)

        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("INSERT INTO apt_tran (dates, months, years, details, amt, c_d) VALUES (?,?,?,?,?,?)",(mon, dat, yea, tem, str(amt), 'c'))
        
        m = dat
        t = int(m) + time
        for i in range(int(m), t):
            c.execute("INSERT INTO apt_def (aptno, months, years, details, paid) VALUES (?,?,?,?,?)",(aptno, i, yea, tem, 'Y'))
        
        print("Transaction successful!")
        
        conn.commit()
        c.close()

# Function add users
def addusers(n):
    clear()
    for x in range(0,n):
        name = input("Enter user name: ")
        type1 = input("Enter your user type: ")
        
        if type1 == "admin":
            userlist.append(Admin(name))
        if type1 == "resident":
            apt = int(input("Enter apartment number: "))
            a_size = input("Enter apartment size(small, medium, large): ")
            userlist.append(Resident(name, apt, a_size))
        if type1 == "owner":
            apt = input("Enter apartment number: ")
            a_size = input("Enter apartment size(small, medium, large): ")
            userlist.append(Owner(name, apt, a_size))
        if type1 == "vendor":
            vid = input("Enter vendor id: ")
            userlist.append(Vendor(name,vid))
        if type1 == "employee":
            eid = input("Enter employee id: ")
            userlist.append(Employee(name,eid))
        if type1 == "treasurer":
            userlist.append(Treasurer(name))

# Function to clear screen using os commands
def clear():
    if os.name == 'nt':                # NT for Windows
        _ = system('cls')
    elif os.name == 'posix':           # POSIX for MacOS and Linux
        _ = system('clear')
    else:
        return
    sleep(0)
    # clear()

# conn.commit()
# conn.close()

#global declarations
global all_apt
all_apt = []
userlist = []

# main
print("Intial Setup")
while(True):
    name = input("Enter user name: ")
    type1 = input("Enter your user type: ")
    
    if type1 == "admin":
        userlist.append(Admin(name))
    if type1 == "resident":
        apt = int(input("Enter apartment number: "))
        a_size = input("Enter apartment size(small, medium, large): ")
        userlist.append(Resident(name,apt, a_size))
    if type1 == "owner":
        apt = input("Enter apartment number: ")
        a_size = input("Enter apartment size(small, medium, large): ")
        userlist.append(Owner(name,apt, a_size))
    if type1 == "vendor":
        vid = input("Enter vendor id: ")
        userlist.append(Vendor(name,vid))
    if type1 == "employee":
        eid = input("Enter employee id: ")
        userlist.append(Employee(name,eid))
    if type1 == "treasurer":
        userlist.append(Treasurer(name))
    
    exit = input("Would you like to end the inital setup: ")
    if exit == "yes":
        break

print("Intial setup finished")
clear()

while (True):
    print("1.Admin\n2.Resident\n3.Owner\n4.Vendor\n5.Employee\n6.Treasurer\n0.Exit")
    selection = int(input("Enter your choice: "))

    if selection == 1:
        admin_list = []
        admin_names = []

        for i in userlist:
            clear()
            if i.usertype == "admin":
                admin_list.append(i)
                admin_names.append(i.username)
        count = 0

        if admin_names == []:
                clear()
                print("There are no admins yet!")
                break

        for admin in admin_names:
            count += 1
            print(str(count) + ". " + admin)

        admin_ind = int(input("Select an admin: "))
        admin_ind -= 1

        print("Admin functions: ")
        while(True):
            clear()
            print("1.Print user details\n2.Take Backup\n3.Modify user\n4.Display all users\n0.Exit admin functions")
            selection1 = int(input("Enter your choice: "))

            if selection1 == 1:
                admin_list[admin_ind].printdetails()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 2:
                admin_list[admin_ind].backup()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 3:
                admin_list[admin_ind].mod_user()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 4:
                admin_list[admin_ind].displayallusers()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 0:
                clear()
                break
            
    
    if selection == 2:
        clear()
        resident_list = []
        resident_names = []

        for i in userlist:
            clear()
            if i.usertype == "resident":
                resident_list.append(i)
                resident_names.append(i.username)
        count = 0

        if resident_names == []:
                clear()
                print("There are no residents yet!")
                break

        for resident in resident_names:
            count += 1
            print(str(count) + ". " + resident)

        resident_ind = int(input("Select an resident: "))
        resident_ind -= 1

        print("Resident functions: ")
        while(True):
            clear()
            print("1.Print user details\n2.Pay dues\n0.Exit resident functions")
            selection1 = int(input("Enter your choice: "))

            if selection1 == 1:
                resident_list[resident_ind].printdetails()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 2:
                resident_list[resident_ind].paydues()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 0:
                clear()
                break

    if selection == 3:
        clear()
        owner_list = []
        owner_names = []

        for i in userlist:
            clear()
            if i.usertype == "owner":
                owner_list.append(i)
                owner_names.append(i.username)
        count = 0

        if owner_names == []:
                clear()
                print("There are no owners yet!")
                break

        for owner in owner_names:
            count += 1
            print(str(count) + ". " + owner)

        owner_ind = int(input("Select an owner: "))
        owner_ind -= 1

        print("Owner functions: ")
        while(True):
            clear()
            print("1.Print user details\n2.Pay dues\n0.Exit owner functions")
            selection1 = int(input("Enter your choice: "))

            if selection1 == 1:
                owner_list[owner_ind].printdetails()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 2:
                owner_list[owner_ind].paydues()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 0:
                clear()
                break

    if selection == 4:
        clear()
        vendor_list = []
        vendor_names = []

        for i in userlist:
            clear()
            if i.usertype == "vendor":
                vendor_list.append(i)
                vendor_names.append(i.username)
        count = 0

        if vendor_names == []:
                clear()
                print("There are no vendors yet!")
                break

        for vendor in vendor_names:
            count += 1
            print(str(count) + ". " + vendor)

        vendor_ind = int(input("Select an vendor: "))
        vendor_ind -= 1

        print("Vendor functions: ")
        while(True):
            clear()
            print("1.Print user details\n2.Vendor service\n0.Exit vendor functions")
            selection1 = int(input("Enter your choice: "))

            if selection1 == 1:
                vendor_list[vendor_ind].printdetails()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 2:
                vendor_list[vendor_ind].perform_service()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 0:
                clear()
                break

    if selection == 5:
        clear()
        employee_list = []
        employee_names = []

        for i in userlist:
            clear()
            if i.usertype == "employee":
                employee_list.append(i)
                employee_names.append(i.username)
        count = 0

        if employee_names == []:
                clear()
                print("There are no employees yet!")
                break

        for employee in employee_names:
            count += 1
            print(str(count) + ". " + employee)

        employee_ind = int(input("Select an employee: "))
        employee_ind -= 1

        print("employee functions: ")
        while(True):
            clear()
            print("1.Print user details\n2.Employee payment\n0.Exit employee functions")
            selection1 = int(input("Enter your choice: "))

            if selection1 == 1:
                employee_list[employee_ind].printdetails()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 2:
                employee_list[employee_ind].fill_timecard()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 0:
                clear()
                break
    
    if selection == 6:
        clear()
        treasurer_list = []
        treasurer_names = []

        for i in userlist:
            clear()
            if i.usertype == "treasurer":
                treasurer_list.append(i)
                treasurer_names.append(i.username)
        count = 0

        if treasurer_names == []:
                clear()
                print("There are no treasurers yet!")
                break

        for treasurer in treasurer_names:
            count += 1
            print(str(count) + ". " + treasurer)

        treasurer_ind = int(input("Select an treasurer: "))
        treasurer_ind -= 1

        print("Treasurer functions: ")
        while(True):
            clear()
            print("1.Print user details\n2.Generate income report\n3.Generate expense report\n4.Generate defaulters list\n0.Exit treasurer functions")
            selection1 = int(input("Enter your choice: "))

            if selection1 == 1:
                treasurer_list[treasurer_ind].printdetails()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 2:
                treasurer_list[treasurer_ind].generate_incomereport()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 3:
                treasurer_list[treasurer_ind].generate_expensereport()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 4:
                treasurer_list[treasurer_ind].generate_defaulterlist()
                print("Press space bar to continue ...")
                keyboard.wait(" ")
            if selection1 == 0:
                clear()
                break
            
    if selection == 0:
        sys.exit()
