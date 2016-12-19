# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""






#SIP Profit/Loss Calculator

import numpy as np

def to_int(arg1):
    if arg1.isdigit():
        return int(arg1)
    else:
        return("invalid entry")
        
months=input("Enter the number of months = ")

no_of_months = to_int(months)

no_of_months
#print("no of months is "+no_of_months)

#SIP Plan
#Here investor buys shares everymonth by paying equal monthly amount for the same stock irrespective of its price.

monthly_installment=input("enter the monthly installment =" )
EMI = to_int(monthly_installment)


def shareprice(no_of_months):
    list=[]
    while (len(list)<no_of_months):
        i=0
        sprice=input("Enter the share price of month",i=i+1)
        list.append(sprice)
    
    return list

sp=shareprice(no_of_months)
print("share price list monthwise :",*sp)

sp_array = np.array(sp,dtype=float)
#to convert list to array with type float

#NOTE: TypeError: ufunc 'multiply' did not contain a loop with signature matching types dtype('<U32') dtype('<U32') dtype('<U32'
#is a type conversion error where the data type dosnt match and hence are is denoted by Unicode-32.
 
no_of_shares_per_month = EMI*(1.0/sp_array)

no_of_shares_total = sum(no_of_shares_per_month)

Saleprice_SIP = sp_array[-1]*no_of_shares_total 

#Simgle Investment
#here investor buys one time at first month price and sells at last month price.

no_of_shares_bought = (no_of_months*EMI)/sp_array[1]

Saleprice_SI=sp_array[-1]*no_of_shares_bought

Profit_loss = Saleprice_SIP - Saleprice_SI

print("Saleprice_SIP :",Saleprice_SIP,"Saleprice_SI :",Saleprice_SI,"Profit/loss",Profit_loss)





    
        
        

        


    
    