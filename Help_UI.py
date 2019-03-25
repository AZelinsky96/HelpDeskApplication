#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 01:20:27 2019

@author: zeski
"""

import datetime
import mysql.connector
from contextlib import closing
from help_object import Ticket
import Help_database




def display_menu():
    print("")
    print("WELCOME TO VECTA CORP HELP DESK APPLICATION (USER)")
    print("")
    print("COMMAND MENU")
    print("-" * 100)
    print("view    -  View all open Tickets")
    print("issue   -  View issue for ticket")
    print("add     -  Add a ticket")
    print("update  -  Update a ticket's status")
    print("exit    -  Exit the program")
    print("-" * 110)
    
def view_tickets():
    print("")
    print("VECTA CORP HELP DESK (CURRENT OPEN TICKETS) " )
    print("-" * 110)
    line_format = "{:5s}| {:15s}| {:15s}| {:15s}|      {:15s}| {:15s}| {:15s}"
    print(line_format.format("ID", "NAME", "EMAIL", "DATE", "EMPLOYEE", "SOLUTION", "STATUS"))
    tickets = Help_database.get_open_ticket()
    for ticket in tickets:
        print(line_format.format(
                        str(ticket.ticket_id),
                        str(ticket.customer_name),
                        str(ticket.customer_email), 
                        str(ticket.submitted_date),
                        str(ticket.employee),
                        str(ticket.solution),
                        str(ticket.status)
                ))
def view_ticket_issue():
    ticketid = input("Please enter Ticket Id: ")
    print("")
    print("VECTA CORP HELP DESK(CURRENT OPEN TICKETS)")
    print("-" * 110)
    issue = Help_database.get_ticket_issue(ticketid)
    print(issue)
    
    
def add_ticket():
    cust_name  = input("Input Customer Name: ")
    cust_email = input("Input Customer Email: ")
    sub_date   = datetime.date.today()
    Help_database.employee_lookup()
    employee   = int(input("Input Employee ID: "))
    solution   = int(input("Solution Id (1 = Open, 2 = In Progress, 3 = Closed):"))  
    status     = 1
    issue      = input("Input issue: ")
    ticket = Ticket(customer_name=cust_name, customer_email=cust_email, submitted_date=sub_date, employee=employee, solution = solution, status = status, issue=issue)
    Help_database.add_ticket(ticket)
    print("")
    print("The new ticket was added successfully!")

    
def update_ticket():
    ticketid = input("Please enter Ticket Id: ")
    choice = input("Do you want to update this ticket? (y/n):").lower()
    if choice == "y": 
        statusid = int(input("Enter new Status-(1 = Open, 2 = In Progress, 3 = Closed):"))
        Help_database.update_ticket(status_id=statusid, ticketid=ticketid)
        print("Ticket Successfully Updated")
    else: 
        print("\nThe Ticket was not updated.\n")
def main():
    Help_database.connect()
    
    while True: 
        print("VECTA CORP HELP DESK USER LOG IN")
        print("-" * 110)
        username = input("Username: ").lower()
        password = input("Password: ").lower()
        if Help_database.login(username, password): 
            print("\nWELCOME {}!".format(username))
            break
        
        else: 
            print("Your Credentials are invalid. Please Try Again.")
        
    display_menu()
    
    
    while True: 
       command = input("Please enter a command to continue: ").lower()
       if command == "view":
           view_tickets()
       elif command == "issue": 
           view_ticket_issue()
       elif command == "add": 
           add_ticket()
       elif command == "update": 
           update_ticket()
       elif command == "exit": 
           
           print("\nThank you, program terminated.")
           break
       else: 
           print("\n\nINVALID ENTRY, PLEASE TRY AGAIN!")
           display_menu()
    Help_database.close()
if  __name__ == "__main__":
    main()
