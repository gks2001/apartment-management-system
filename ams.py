import sys
import os
import shutil
import sqlite3

conn = sqlite3.connect('apt.db')
c = conn.cursor()
# c.execute("CREATE TABLE apt_tran (months integer, dates integer, years integer, details text, amt real, c_d text)")
# c.execute("CREATE TABLE apt_def (aptno integer, months integer, years integer,details text, paid text)")
conn.commit()

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
        # google drive api ???
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

class Vendor(User):
    def __init__(self, username, ven_id = -1):
        User.__init__(self, username, "vendor")
        self.vendorid = ven_id
        self.privilege = 1

    def printdetails(self):
        print("\nVendor Name: " + self.username + "\nVendor ID: " + self.vendorid + "\nUsertype: " + self.usertype)

    def perform_service(self):
        service_name = input("Enter the service name: ")
        service_cost = float(input("Enter the payment amount: "))
        date = input("Enter date: ")
        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]
        self.get_payment(service_name, service_cost, mon, dat, yea)

    def get_payment(self, service_name, service_cost, mon, dat, yea):
        Treasurer.pay_vendor(self.username, self.vendorid, service_name, service_cost, mon, dat, yea)

class Employee(User):
    def __init__(self, username, emp_id = -1):
        User.__init__(self, username, "employee")
        self.employeeid = emp_id
        self.privilege = 1

    def printdetails(self):
        print("\nEmployee Name: " + self.username + "\nEmployee ID: " + self.employeeid + "\nUsertype: " + self.usertype)

    def fill_timecard(self):
        date = input("Enter date: ")
        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]
        days = int(input("How many days have the employee worked this month: "))
        emp_sal = 300 * days
        self.get_salary(emp_sal, mon, dat, yea)

    def get_salary(self, emp_sal, mon, dat, yea):
        Treasurer.pay_emp(self.username, self.employeeid, emp_sal, mon, dat, yea)

class Owner(User):
    def __init__(self, username, apt = -1):
        User.__init__(self, username, "owner")
        self.aptno = apt
        self.privilege = 2
        all_apt.append(apt)

    def printdetails(self):
        print("\nOwner Name: " + self.username + "\nApartment Number: " + self.aptno + "\nUsertype: " + self.usertype)

    def paydues(self):
        adv_time = 0
        months = 0
        cur_mon = 0
        aptno = int(input("Enter the apartment number: "))
        date = input("Enter date: ")
        size = input("Enter apartment size(small, medium, large): ")
        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]
        selection = int(input("1.Pay for current month\n2.Pay in advance\nEnter your choice: "))
        if size == "small":
            cost = 1500
        if size == "medium":
            cost = 2500
        if size == "large":
            cost = 3500

        if selection == 1:
            months = 1
            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount, mon, dat, yea)
        else:
            adv_time = int(input("1.Quarterly\n2.Semi-Annually\n3.Annually\nEnter your choice: "))
            if adv_time == 1:
                months = 3
            if adv_time == 2:
                months = 6
            if adv_time == 3:
                months = 12
            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount, mon, dat, yea)

class Resident(User):
    def __init__(self, username, apt = -1):
        User.__init__(self, username, "resident")
        self.aptno = apt
        self.privilege = 2
        all_apt.append(apt)

    def printdetails(self):
        print("\nResident Name: " + self.username + "\nApartment Number: " + str(self.aptno) + "\nUsertype: " + self.usertype)

    def paydues(self):
        adv_time = 0
        months = 0
        cur_mon = 0
        aptno = int(input("Enter the apartment number: "))
        date = input("Enter date: ")
        size = input("Enter apartment size(small, medium, large): ")
        da = date.split("/", -1)
        mon = da[0]
        dat = da[1]
        yea = da[2]
        selection = int(input("1.Pay for current month\n2.Pay in advance\nEnter your choice: "))
        if size == "small":
            cost = 1500
        if size == "medium":
            cost = 2500
        if size == "large":
            cost = 3500

        if selection == 1:
            months = 1
            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount, mon, dat, yea)
        else:
            adv_time = int(input("1.Quarterly\n2.Semi-Annually\n3.Annually\nEnter your choice: "))
            if adv_time == 1:
                months = 3
            if adv_time == 2:
                months = 6
            if adv_time == 3:
                months = 12
            amount = cost * months
            Treasurer.collect_dues(self.aptno, months, amount, mon, dat, yea)

class Treasurer(User):
    def __init__(self, username):
        User.__init__(self, username, "treasurer")
        self.privilege = 3

    def printdetails(self):
        print("\nTreasurer Name: " + self.username + "\nUsertype: " + self.usertype)
    
    def generate_incomereport(self):
        mon = input("Enter month to generate report for: ");
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("SELECT * FROM apt_tran WHERE months = ? AND c_d = ?", (mon, 'c'))
        records = c.fetchall()
        
        printrec = ''
        for record in records:
            date = str(record[1]) + "/" + str(record[0]) + "/" + str(record[2])
            print("Date: " + date + "\tDeatails: " + str(record[3]) + "\tAmount: " + str(record[4]))
            print("\n")
        
        if records == []:
            print("No transactions!")
        
        conn.commit()
        conn.close()

    def generate_expensereport(self):
        mon = input("Enter month to generate report for: ");
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("SELECT * FROM apt_tran WHERE months = ? AND c_d = ?", (mon, 'd'))
        records = c.fetchall()
        
        printrec = ''
        for record in records:
            date = str(record[1]) + "/" + str(record[0]) + "/" + str(record[2])
            print("Date: " + date + "\tDeatails: " + str(record[3]) + "\t\tAmount: " + str(record[4]))
            print("\n")
        
        if records == []:
            print("No transactions!")

        conn.commit()
        conn.close()

    def generate_defaulterlist(self):
        paid_list = []
        d_list = []
        count = 0
        mon = input("Enter month to generate report for: ")
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        sql = "SELECT * FROM apt_def WHERE months = " + mon
        c.execute(sql)
        records = c.fetchall()
        
        printrec = ''
        print("Paid List")
        for record in records:
            date = str(record[1]) + "/" + str(record[2])
            tem = str(record[0]) + str(record[3])
            print("Month: " + date + "\tDetails: " + tem + "\t\tPaid: " + str(record[4]))
            paid_list.append(record[0])
        
        print("\nDefaulter List")
        d_list = set(all_apt).difference(paid_list)
        for i in d_list:
            count += 1
            print(str(count) + ". Apartment " + str(i))
        print("There are total " + str(count) + " defaulters for this month")


    @staticmethod
    def pay_emp(name, empid, sal, mon, dat, yea):
        tem = name + " - " + "monthly salary"
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("INSERT INTO apt_tran (dates, months, years, details, amt, c_d) VALUES (?,?,?,?,?,?)",(mon, dat, yea, tem, sal, 'd'))
        print("Transaction successful!")
        conn.commit()
        c.close()

    @staticmethod
    def pay_vendor(name, ven_id, service_name, service_cost, mon, dat, yea):
        tem = name + " - " + service_name
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("INSERT INTO apt_tran (dates, months, years, details, amt, c_d) VALUES (?,?,?,?,?,?)",(mon, dat, yea, tem, service_cost, 'd'))
        print("Transaction successful!")
        conn.commit()
        c.close()
    
    @staticmethod
    def collect_dues(aptno, time, amt, mon, dat, yea):
        tem = "Monthly dues ("+ str(time) + ") - Aptno: " + str(aptno)
        conn = sqlite3.connect('apt.db')
        c = conn.cursor()
        c.execute("INSERT INTO apt_tran (dates, months, years, details, amt, c_d) VALUES (?,?,?,?,?,?)",(mon, dat, yea, tem, amt, 'c'))
        m = dat
        t = int(m) + time
        for i in range(int(m), t):
            c.execute("INSERT INTO apt_def (aptno, months, years, details, paid) VALUES (?,?,?,?,?)",(aptno, i, yea, tem, 'Y'))
        print("Transaction successful!")
        conn.commit()
        c.close()

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

conn.commit()
conn.close()

# Testing purposes ....

global all_apt
all_apt = []

res1 = Resident("res1", 123)
res2 = Resident("res2", 234)
res3 = Resident("res3", 345)

userlist = []
selection = -1
while(selection != 0):
    print("1.Add user\n2.Display users\n3.Backup\n4.Admin moduser\n5.Pay vendor\n6.Expenese Report\n7.Pay Employee\n8.Income Report\n9.Owner dues\n10.Defaulter\n11.Resdient\n0.Exit")
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
    if selection == 5:
        v1 = Vendor("ven1")
        v1.perform_service()
    if selection == 6:
        t1 = Treasurer("t1")
        t1.generate_expensereport()
    if selection == 7:
        e1 = Employee("e1")
        e1.fill_timecard()
    if selection == 8:
        t1 = Treasurer("t1")
        t1.generate_incomereport()
    if selection == 9:
        o1 = Owner("o1")
        o1.paydues()
    if selection == 10:
        t1 = Treasurer("t1")
        t1.generate_defaulterlist()
    if selection == 11:
        r1 = Resident("r1", 123)
        r1.paydues()