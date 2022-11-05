#!/usr/bin/env python3
"""
Guidelines for program submission: 
    
A) To ensure readability by the grader, 
    please make sure the following submission format:

    1-- Please change the file name to python_program_one.py and python_program_two.py 
        ---(The file name is case sensitive, make sure it's identical)---
       
               
    2-- The *.py file should be compressed to the root of the *.zip file
        e.g., when you submit your homework.zip, 
                Please compress the python files directly 
        ---(Do Not compress the directory!)---
                    aka, if you unzip your *.zip, *.py files should appear
                        in the directory of *.zip file. 

B) Your homework should follow the similar structure as this template

C) Keep in mind some minor points:
    
    0-- Your code should not have any debug error before submission!!!

    1-- make sure the function name is identical to that in the problem set (HW)
            ---(function names are case sensitive! )---
    
    2-- The order of the function arguments should be the same as that in HW 

    2a-- The data type of the argument should be the same as that in HW
                      
    3-- make sure your function return the value which the HW requested
    
    4-- make sure the order of the output arguments the same as those in HW
    
    5-- Do not round up your output values
    
    6-- Do not use input function in your function
        
    7-- if you need uncommon modules, contact TA before submission
    


If you had any question about the guideline, 
    contact TAs or post questions on piazza for response.
        
@author: Dan Li (lidan@ucsd.edu) at UCSD
@date: Jan 2021
"""



"""
The template starts from here
"""

# A432432 #PID

# import all modules here if you need any

# import numpy as np

# your file should always start from definition of functions 

def My_first_function(p1, p2):
    """ Add illustrations here, if needed """
    
    # define variables you need
    a = 0
    b = 0
    c = 0
    
    #####
    # enter logic here
    #####
    
    #make sure you return your function
    return a, b, c


def My_Second_Function(q, p1, p2):
    distance = 0
    # enter logic here
    return distance


if __name__ == '__main__':
    """ 
    This is the place where you test your function. 
    You could define variables, feed them into your function and check the output   
    """
    
    p1 = [1, 1]
    p2 = [2, 2]
    q = [3, 4]
    a, b, c = My_first_function(p1, p2)
    print(a)
    print('my value c')
    print(c)
    distance = My_Second_Function(q, p1, p2)

