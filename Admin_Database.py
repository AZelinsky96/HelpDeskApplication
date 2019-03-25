#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:55:48 2019

@author: zeski
"""

import mysql.connector
from contextlib import closing
from employeefile import Employee

## Connection function
def connect(user = "Anthony", password = "8terss7a",host = "localhost",database = "vc_helpdesk"): 
    """Function takes in the parameters above to connect to a MySQL database. It returns a connection object"""
    
    conn = mysql.connector.connect(user = user,
                                   password = password, 
                                   host = host, 
                                   database = database)
    print("Connected to the Database: {}".format(database))
    return conn 




#with closing(conn.cursor()) as cur: 
#    cur.execute("Show Tables;")
#    tables_tup= cur.fetchall()

#    tables = [k[0] for k in tables_tup]    



#    for i in tables: 
#        print("Table: {}\n".format(i))
#        cur.execute("SELECT * FROM {}".format(i))
#        query = cur.fetchall()
#        for k in query: 
#            print(k)
#        print('\n')


## get_employees functions: 
def login(username, password, roleid, conn) : 
    query = "SELECT COUNT(*) FROM employees WHERE username = %s AND password = %s AND role_id = %s"
    with closing(conn.cursor()) as cur: 
        cur.execute(query, (username, password, roleid))
        result = cur.fetchall()
    if result[0][0] > 0 :
        query = "SELECT name FROM employees WHERE username = %s"
        with closing(conn.cursor()) as cur:
            cur.execute(query, (username,))
            result = cur.fetchone()
        print("\nWELCOME {}".format(result[0]))
        return True
    else: 
        return False


def make_employee(row):
    return Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    
def display_roles(conn):
    query = "SELECT * FROM roles;"
    with closing(conn.cursor()) as cur: 
        cur.execute(query)
        result = cur.fetchall()
    roles = []
    [roles.append(role) for role in result]
    for role in roles:
        print("ID:", role[0], "  ----  Role:", role[1])
    
    
    
def get_employees(conn): 
    query = "SELECT employees.*, roles.role FROM employees INNER JOIN roles ON (employees.role_id = roles.roleid)"
    with closing(conn.cursor()) as cur: 
        cur.execute(query)
        result = cur.fetchall()
    employees = []
    [employees.append(make_employee(row)) for row in result]
    
    return employees

#conn = connect()
#employees =get_employees(conn)
#for emp in employees: 
#    print(emp.role)
def get_employee(employeeid,conn): 
    query = "SELECT employees.*, roles.role FROM employees INNER JOIN roles ON (employees.role_id = roles.roleid) WHERE employees.employeeid = %s"
    with closing(conn.cursor()) as cur: 
        cur.execute(query, (employeeid, ))
        result = cur.fetchone()
    employee = make_employee(result)
    return employee



def add_employee(employee, conn): 
    sql = "INSERT INTO employees(name, username, password, email, role_id) VALUES(%s, %s, %s, %s, %s )"
    with closing(conn.cursor()) as cur: 
        cur.execute(sql, (employee.name, employee.username, employee.password, employee.email, employee.role_id))
        conn.commit()
    


def delete_employee(employeeid, conn): 
    sql = "DELETE FROM employees WHERE employeeid = %s"
    with closing(conn.cursor()) as cur: 
        cur.execute(sql, (employeeid, ))
        conn.commit()

## Closing function 
def close(conn): 
    if conn: 
        conn.close()
    return print("\nConnection Closed")

