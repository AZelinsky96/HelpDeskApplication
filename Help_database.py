#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 01:20:27 2019

@author: zeski
"""
import mysql.connector
from contextlib import closing
from help_object import Ticket, Employee



def connect(user = "Anthony", password = "8terss7a",host = "localhost",database = "vc_helpdesk"): 
    """Function takes in the parameters above to connect to a MySQL database. It returns a connection object"""
    
    global conn 
    conn = mysql.connector.connect(user = user,
                                   password = password, 
                                   host = host, 
                                   database = database)
    print("Connected to the Database: {}".format(database))
    #return conn 
    
def close():
    if conn: 
        conn.close()
        
def make_ticket(row):
    return Ticket(row[0],
                  row[1],
                  row[2], 
                  row[3], 
                  row[4], 
                  row[5], 
                  row[6],
                  row[7]
                  )
    
    
    
def get_open_ticket():
    query = ("""
        SELECT tickets.ticket_id, tickets.customer_name, tickets.customer_email, tickets.submitted_date,  employees.name AS employee, solutions.solution, status.status, tickets.issue
        FROM employees INNER JOIN tickets ON (employees.employeeid = tickets.employee_id) INNER JOIN
        solutions ON (tickets.solution_id = solutions.solutionid) INNER JOIN
        status ON (tickets.status_id = status.statusid)
        WHERE tickets.status_id  = 1 OR tickets.status_id = 2
        """)
    with closing(conn.cursor()) as cur:
        cur.execute(query)
        results = cur.fetchall()
    tickets = []
    for row in results: 
        tickets.append(make_ticket(row))
    return tickets

    
def get_ticket_issue(ticketid):
    query = "SELECT ticket.issue FROM tickets WHERE ticket_id = %s"
    with closing(conn.cursor()) as cur: 
        cur.execute(query, (ticketid,))
        results = cur.fetchone()
    return results[0]
    
def add_ticket(ticket):
    insert = "INSERT INTO tickets (customer_name, customer_email, submitted_date, employee_id, solution_id, status_id, issue) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    with closing(conn.cursor()) as cur: 
        cur.execute(insert, (ticket.customer_name, ticket.customer_email, ticket.submitted_date, ticket.employee, ticket.solution, ticket.status, ticket.issue))
        conn.commit()
        
        
        
def update_ticket(status_id, ticketid):
    update = "UPDATE tickets SET status_id = %s WHERE ticket_id = %s"
    with closing(conn.cursor()) as cur:
        cur.execute(update, (status_id, ticketid))
    
    
def login(username, password): 
    query = "SELECT COUNT(*) FROM employees WHERE username = %s AND password = %s"

    
    with closing(conn.cursor()) as cur: 
        cur.execute(query, (username, password))
        results = cur.fetchone()
        
    if results[0] > 0:
        return True
    else: 
        print("Invalid Credentials, please try again.")
        return False
    
def lookup_emp_obj(row): 
    return Employee(
                row[0],
                row[1], 
                row[2],
                row[3]
            )
    
def employee_lookup(): 
    query = "SELECT employees.employeeid, employees.name, employees.email, roles.role FROM employees INNER JOIN roles ON employees.role_id = roles.roleid"
    with closing(conn.cursor()) as cur: 
        cur.execute(query)
        results = cur.fetchall()
    print("Here is a list of employees for id reference: ")
    print("-" * 110)
    line_format = "{:15s}     |{:15s}  |{:25s}      |{:15s}"
    print(line_format.format("Employee ID", "Name", "Email", "Role"))
    for row in results:
        print(line_format.format(str(row[0]), row[1], row[2], row[3]))    
    


