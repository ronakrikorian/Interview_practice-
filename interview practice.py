# -*- coding: utf-8 -*-
"""
@author: ronak
"""
base_time = 30
customer_first_name = input ("What is your first name?\n")
customer_last_name = input ("What is your last name?\n")

customer = str((customer_last_name, customer_first_name))
#made into a string since could not concat tuple
dine_in = input ("Welcome, Select 'Y' if you would like to dine-in or 'N' if you would"
                 " like to order take out. \n")
if dine_in.upper() == 'Y':
    party_size = int(input("How many people are in your party?\n" ))

    if  party_size in range(1,5):
        print("Your table will be ready in approximately" + str(base_time) + " minutes.\n" )
        
    else:
        print("Your table will be ready in approximately" + str(base_time+15) + " minutes.\n" )

bid_yn = input ("Would you like to make a bid " + customer +" to decrease your wait time?\n"
                "Enter '0' if you do not want to place a bid.\n" )

while bid_yn != "0":
    bid = int(input ("How much would would you like to bid for this reservation\n"))
    if bid >=party_size*100:
        print("Your wait time is now " + str(base_time-15) + " minutes.\n")
        break
    elif bid < party_size*100:
        print ("We appologize but a larger bid is needed to decrease your wait time.\n"
               "Would you like to place another bid?")
        
        
        
    
    


    
    


    
    
    



    
            


    

    
    
