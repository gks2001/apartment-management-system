class User: 
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype

    def printdetails(self):
        print("\nUsername: " + self.username + "\nUsertype: " + self.usertype)

class Admin(User):
    def __init__(self, username):
        self.adminname = username
        self.usertype = "admin"
        self.privilege = 3
    
    def printdetails(self):
        print("\nAdmin Name: " + self.adminname + "\nUsertype: " + self.usertype)

class Vendor(User):
    def __init__(self, username, ven_id = -1):
        self.vendorname = username
        self.vendorid = ven_id
        self.usertype = "vendor"
        self.privilege = 1

    def printdetails(self):
        print("\nVendor Name: " + self.vendorname + "\nVendor ID: " + self.vendorid + "\nUsertype: " + self.usertype)

class Employee(User):
    def __init__(self, username, emp_id = -1):
        self.employeename = username
        self.employeeid = emp_id
        self.usertype = "employee"
        self.privilege = 1

    def printdetails(self):
        print("\nEmployee Name: " + self.employeename + "\nEmployee ID: " + self.employeeid + "\nUsertype: " + self.usertype)

class Owner(User):
    def __init__(self, username, apt = -1):
        self.ownername = username
        self.aptno = apt
        self.usertype = "owner"
        self.privilege = 2

    def printdetails(self):
        print("\nOwner Name: " + self.ownername + "\nApartment Number: " + self.aptno + "\nUsertype: " + self.usertype)

class Resident(User):
    def __init__(self, username, apt = -1):
        self.residentname = username
        self.aptno = apt
        self.usertype = "resident"
        self.privilege = 2

    def printdetails(self):
        print("\nResident Name: " + self.residentname + "\nApartment Number: " + str(self.aptno) + "\nUsertype: " + self.usertype)

n = int(input("Enter number of users: "))
userlist = []
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

for x in userlist:
    x.printdetails()