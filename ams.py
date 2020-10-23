class User: 
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype

    def printuserdetails(self):
        print("\nUsername: " + self.username + "\nUsertype: " + self.usertype)

class Admin(User):
    def __init__(self, username, usertype = "admin"):
        self.adminname = username
        self.usertype = "admin"
        self.privilege = 3
    
    def printadmindetails(self):
        print("\nAdmin Name: " + self.adminname + "\nUsertype: " + self.usertype)

class Vendor(User):
    def __init__(self, username, usertype = "vendor", id = -1):
        self.vendorname = username
        self.vendorid = id
        self.usertype = usertype
        self.privilege = 1

    def printvendordetails(self):
        print("\nVendor Name: " + self.vendorname + "\nVendor ID: " + self.vendorid + "\nUsertype: " + self.usertype)

class Employee(User):
    def __init__(self, username, usertype = "employee", id = -1):
        self.employeename = username
        self.employeeid = id
        self.usertype = usertype
        self.privilege = 1

    def printemployeedetails(self):
        print("\nEmployee Name: " + self.employeename + "\nEmployee ID: " + self.employeeid + "\nUsertype: " + self.usertype)

class Owner(User):
    def __init__(self, username, usertype = "owner", aptno = -1):
        self.ownername = username
        self.aptno = aptno
        self.usertype = usertype
        self.privilege = 2

    def printownerdetails(self):
        print("\nOwner Name: " + self.ownername + "\nApartment Number: " + self.aptno + "\nUsertype: " + self.usertype)

class Resident(User):
    def __init__(self, username, usertype = "resident", apt = -1):
        self.residentname = username
        self.aptno = aptno
        self.usertype = usertype
        self.privilege = 2

    def printvendordetails(self):
        print("\nResident Name: " + self.residentname + "\nApartment Number: " + self.aptno + "\nUsertype: " + self.usertype)

n = int(input("Enter number of users: "))
for x in range(0,n):
    name = input("Enter user name: ")
    type1 = input("Enter your user type: ")
    
u1 = Admin(name, type1)
u1.printuserdetails()