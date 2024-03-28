#sqlsyntax.py
# Name: Rhodas Yemaneab and Smita Magar
# email: yemanert@mail.uc.edu , diswamsa@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/28/24
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment demonstrates how to collaborate with team members to 
# contrive a select query from SSMS and eclipse to sort and analyze the data. This assignment also demonstrated 
# how to push and commit, and pull from Git hub when collaborating.   
# Brief Description of what this module does.On this module, we create a function of SQL syntax using
# group by, order by, and sum operations.
# Citations: https://www.w3schools.com/sql/sql_groupby.asp
# Anything else that's relevant: 


def sql_select():
    sql_select= "SELECT SUM(td.AmountOff) as totalAmtOff, ts.CouponSource FROM tCoupon as tc \
                 INNER JOIN tCouponDetail as td ON tc.CouponID = td.CouponID    INNER JOIN \
                 tCouponSource as ts ON tc.CouponSourceID = ts.CouponSourceID \
                 WHERE td.PercentageDiscount >= 50 \
                 GROUP BY ts.CouponSource \
                 ORDER BY totalAmtOff DESC"
    return sql_select;             

