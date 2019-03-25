#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 01:20:27 2019

@author: zeski
"""

class Ticket():
    def __init__(self, ticket_id = 0, customer_name = None, customer_email = None, submitted_date = None, employee = 0, solution = 0, status = 0, issue = None ):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.submitted_date = submitted_date
        self.employee = employee
        self.solution = solution
        self.status = status
        self.issue = issue
        
        
class Employee():
    def __init__(self, emp_id, emp_name, emp_email, emp_role): 
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.emp_role  = emp_role



