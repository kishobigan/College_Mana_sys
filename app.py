from cupshelpers import Printer
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="admin", password="KISHO@bigan5176", database="College")
command_handler = db.cursor(buffered = True)

def Admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("----------")
        print("1. Add A New Student")
        print("2. Add A New Teacher")
        print("3. Delete Exisiting Student")
        print("4. Delete Exisiting Teacher")
        print("5. Logout")
        print("")

        admin_option = input(str("Option : "))
        print("")
        if admin_option == "1":
            print("Register New Student")
            print("--------------------")
            username = input(str("Enter Student user Name     : "))
            password = input(str("Enter Student user Password : "))
            query_val = (username,password)
            command_handler.execute("INSERT INTO Users (userName,Password,Privilege) VALUES (%s,%s,'Student')",query_val)
            db.commit()
            print(username+" is Registered As A Student")
            print("")
        elif admin_option == "2":
            print("Register New Teacher")
            print("--------------------")
            username = input(str("Enter Teacher user Name     : "))
            password = input(str("Enter Teacher user Password : "))
            query_val = (username,password)
            command_handler.execute("INSERT INTO Users (userName,Password,Privilege) VALUES (%s,%s,'Teacher')",query_val)
            db.commit()
            print(username+" is Registered as a Teacher")
            print("")
        elif admin_option == "3":
            print("Delete a student")
            print("----------------")
            username = input(str("Enter user name for delete : "))
            query_val = (username,"Student")
            command_handler.execute("DELETE FROM Users WHERE userName = %s AND Privilege = %s", query_val)
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not found")
                print("")
            else:
                print(username+" has Deleted")
                print(" ")
        elif admin_option == "4":
            print("Delete a teacher")
            print("----------------")
            username = input(str("Enter user name for delete : "))
            query_val = (username,"Teacher")
            command_handler.execute("DELETE FROM Users WHERE userName = %s AND Privilege = %s", query_val)
            db.commit()
            if command_handler.rowcount < 1:
                print("User Not found")
                print("")
            else:
                print(username+" has Deleted")
                print(" ")
        elif admin_option == "5":
            break
        else:
            print("No Valid Selection")
            print(" ")

def auth_admin():
    print("Admin Login")
    print("-----------")
    print("")
    userName = input(str("User Name : "))
    password = input(str("Password  : "))

    if userName == "username":
        if password == "password":
            Admin_session()
        else:
            print("Password is Incorrect")
            print("")
    else:
        print("Admin Login Failed")
        print("")


def main():
   while 1:
        print("Welcome To The College Management System")
        print("----------------------------------------")
        print("")
        print("1. Login As A Student")
        print("2. Login As A Teacher")
        print("3. Login As A Admin")
        print("   Press any other option for exit ")
        print("")

        user_option = input(str("Option : "))
        print("")
        if user_option == "1":
            print("Student Login")
        elif user_option == "2":
            print("Teacher Login")
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option selected. Try again thank you.")
            print("")
            break


main()