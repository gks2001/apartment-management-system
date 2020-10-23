class User: 
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype

    def printuserdetails(self):
        print("\nUsername: " + self.username + "\nUsertype: " + self.usertype)

name = input("Enter your name: ")
type1 = input("Enter your user type: ")
u1 = User(name, type1)
u1.printuserdetails()