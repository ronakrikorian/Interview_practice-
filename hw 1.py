# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:09:22 2022

@author: ronak
"""

# A14160302 #PID
# import all modules here if you need any
import math
import sys
import copy
import matplotlib.path as mpltPath


# your file should always start from definition of functions 
def dist(p1, p2):
        
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def compute_line_through_two_pts(p1,p2):
   
    distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    if distance < 1e-5:
        sys.stderr.write("Cannot compute line: the two points are too close\n")
        sys.exit(1)
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0]*p2[1] - p2[0]*p1[1]
    
    return a/distance, b/distance, c/distance

def compute_distance_pt_to_line (q, p1, p2):
    
    (a,b,c) = compute_line_through_two_pts(p1, p2)
    
    return abs(a*q[0] + b*q[1] + c)/math.sqrt(a**2 + b**2)

def compute_distance_pt_to_segment (q, p1, p2):
    segment_length = dist(p1,p2)
    u = (((q[0] - p1[0])*(p2[0] - p1[0]) + (q[1] - p1[1])*(p2[1]-p1[1]))/(segment_length**2))
    w = 0
    
    if 0.0 <= u <= 1.0:
        return compute_distance_pt_to_line(q, p1, p2),w
    elif u < 0.0:
        w = 1
        return dist(p1, p2),w
    else:
        w=2
        return dist(q,p2),w
def compute_dist_pt_to_polygon(q,P):
    outvar = math.inf
    PDV = copy.deepcopy(P)
    PDV.append(P[0])
    
    for i in range(len(PDV) - 1):
        p1 = PDV[i]
        p2 = PDV[i+1]
        D = compute_distance_pt_to_segment(q, p1, p2)
        if D < outvar:
            outvar = D
            
    path = mpltPath.Path(P)
    inside = path.containts_point(q)
    if inside:
        return -outvar
    else:
        return outvar

if __name__ == '__main__':
    """ 
    This is the place where you test your function. 
    You could define variables, feed them into your function and check the output  
    """
    
    p1 = [1, 1]
    p2 = [2, 2]
    q = [3, 4]
    a, b, c = compute_line_through_two_pts(p1, p2)
    print(round(a,2))
    print('my value c')
    print(c)
    distance = compute_distance_pt_to_line(q, p1, p2)