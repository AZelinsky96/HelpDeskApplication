#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:23:47 2019

@author: zeski
"""
import DatabaseProject
from employeefile import Employee
import time


def display_menu():
    print("\nThe Vecta Corp Help Desk Application  (Admin)")
    print('\n')
    print("COMMAND MENU")
    print("_" * 65)
    print("view   - View all employees")
    print("add    - Add an Employee")
    print("delete - Remove and employee")
    print("exit   - Exit the Program")
    print("_" * 65)

def view_employees(conn):
    print("")
    print("VECTA CORP HELP DESK EMPLOYEES")
    print("_" * 65)
    line_format = "{:5s} {:8s} {:15s} {:15s} {:25s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Username", "Password", "Email", "RoleID", "Role"))
    print("_" * 65)
    employees = DatabaseProject.get_employees(conn)
    #print(employees)
    for employee in employees: 
        try: 
            print(line_format.format(str(employee.employeeid).strip(), str(employee.name).strip(), str(employee.username).strip(), str(employee.password).strip(), str(employee.email).strip(), str(employee.role_id).strip(), str(employee.role).strip()))
        except: 
            pass
        #print("Name",employee.name)
        #print("email", employee.email)
        #print("ID", str(employee.employeeid))
        #print("Pass", employee.password)
        #print("Role", str(employee.role_id))
        #print("username", employee.username)
        #print("\n")


def add_employee(conn): 
    print("Please Input: ")
    name     = input("Name: ")
    username = input("Username: ")
    password = input("Password: ")
    email    = input("Email:  ")
    print("\nBelow is a list of Role Id's and their corresponding roles. Please enter correct Id.")
    
    DatabaseProject.display_roles(conn)
    roleid   = int(input("Role ID: "))
    
    employee = Employee(name = name, username=username, password=password, email=email, role_id=roleid)
    
   
    DatabaseProject.add_employee(employee, conn)
    print("USER: " + name + " was added to the Database successfully!\n")


def delete_employee(conn): 
    print("Please input Employee ID to delete. ")
    employeeid = int(input("Employee ID: "))
    employee   = DatabaseProject.get_employee(employeeid, conn)
    
    choice = input("CONFIRM TO  DELETE \n\nUSER: {}, \nID: {}\nROLE: {}\n\nfrom the database? [Y/N]\n".format(employee.name, employee.employeeid, employee.role))
    
    
    if choice == "Y": 
         DatabaseProject.delete_employee(employeeid, conn)
         print("USER:{} was deleted from the Database. ".format(employee.name))
    elif choice != "Y": 
         print("USER: "+ employee.name + " was not deleted from the Database!\n")

    
    
    
    
def main(): 
    conn = DatabaseProject.connect()
    while True: 
        print("\nVECTACORP HELP DESK LOG IN")
        print("_" * 65)
        username_login = input("Username: ").lower().strip()
        password_login = input("Password: ").lower().strip()
        if DatabaseProject.login(username_login, password_login, 4 , conn): 
            time.sleep(1.5)
            break
        else: 
            print("\nCredentials Invalid. Please Try Again\n")
            
    display_menu()
    while True: 
        command = input("Enter Command: ").lower()
        if command == "view": 
            view_employees(conn)
        elif command == "add": 
            add_employee(conn)
        elif command =="delete":
            delete_employee(conn)
        elif command == "exit": 
            break
        else: 
            print("Not a Valid Command.... Please try again.\n")
            display_menu()
    DatabaseProject.close(conn)
    print("Program has been terminated.")
    
    
    
if __name__ == "__main__":     
    main()
    
    
    
    