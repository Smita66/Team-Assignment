# main.py

# Name: Rhodas Yemaneab and Smita Magar
# email: yemanert@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/24
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: 
# Brief Description of what this module does. Do not copy/paste from a previous assignment. 
# Citations: 
# Anything else that's relevant: 

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                        'Database=GroceryStoreSimulator;'
                        'uid=IS4010Login;'
                        'pwd=P@ssword2;')
cursor = conn.cursor()
cursor.execute( )
