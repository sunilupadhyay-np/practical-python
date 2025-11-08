# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 10:18:29 2025

@author: sunil
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_pay = 1000.0
month_index = 1
extra_pay_months = 12


while month_index <= extra_pay_months:
    principal = principal + (rate/12)*principal - payment - extra_pay
    total_paid = total_paid + payment + extra_pay
    print(month_index, principal)
    month_index = month_index + 1
    

while principal > 0:
    principal = principal + (rate/12)*principal - payment
    total_paid = total_paid + payment
    print(month_index, principal)
    month_index = month_index + 1
    
# Note that the there is one extra month upadate in the 2nd while loop at the very end.
# We manually account for this below. Not elegant. A better approach?
month_index = month_index - 1

    
print('Number of months required', month_index)  
print('Total paid', total_paid)