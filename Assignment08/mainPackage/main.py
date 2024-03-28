# main.py

# Name: Rhodas Yemaneab and Smita Magar
# email: yemanert@mail.uc.edu ,diswamsa@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/24
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment demonstrates how to collaborate with team members to 
# contrive a select query from SSMS and eclipse to sort and analyze the data. This assignment also demonstrated 
# how to push and commit, and pull from Git hub when collaborating.   
# Brief Description of what this module does: This module call the SQL function which has SQL syntax . it also
# print the interesting fact about coupon discount which is analyzed after executing the SQL statements.
# Citations:https://www.freecodecamp.org/news/print-newline-in-python/
# https://www.geeksforgeeks.org/how-to-connect-python-with-sql-database/
# Anything else that's relevant: 

import pyodbc
from SqlsyntaxPackage.Sqlsyntax import sql_select
conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                        'Database=GroceryStoreSimulator;'
                        'uid=IS4010Login;'
                        'pwd=P@ssword2;')
cursor = conn.cursor()
# Execute the SQL query from sqlsyntax.py
sql_query = sql_select()
cursor.execute(sql_query)

totalAmountOff = list();
couponsSource = list();
# Fetch and print the results if needed
for row in cursor.fetchall():
    print("-------------")
    print(row[0] ,"|", row[1])
    totalAmountOff.append(row[0]);
    couponsSource.append(row[1]);
#printing the output of code in one sentence.
print("\n")  
print("The highest coupon discount is %s with CouponSource: %s and the lowest coupon discount is %s with CouponSource: %s " 
      %(totalAmountOff.pop(0), couponsSource.pop(0), totalAmountOff.pop(len(totalAmountOff)-1), couponsSource.pop(len(couponsSource)-1)));
