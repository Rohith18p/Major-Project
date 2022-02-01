import numpy as np
import math

#link lengths
l1 = 120
l2 = 250
l3 = 212.5

Xmax = l2 + l3 
Ymax = l2 + l3
Zmax = l1 + l2 + l3

l = np.array([l1, l2, l3])
c = np.array([100, 100, 120])

def req_angles(l, c):
    
    #inverse kinematic equation for position:
    r3 = np.sqrt(c[0]**2 + c[1]**2)
    r2 = c[2] - l[0]
    r1 = np.sqrt(r3**2 - r2**2)
    
    phi1 = math.degrees(np.arctan2(r2, r3))
    phi2 = math.degrees(math.acos((r3**2 + l[1]**2 - l[2]**2)/(2*l[1]*r3)))
    phi3 = math.degrees(math.acos((l[1]**2 + l[2]**2 - r3**2)/(2*l[1]*l[2])))
    
    theta1 = math.degrees(np.arctan2(c[1], c[2]))
    theta2 = phi2 - phi1
    theta3 = 180 - phi3
    
    return theta1, theta2, theta3



t = req_angles(l, c)
print('theta_1: ', t[0])
print('theta_2: ', t[1])
print('theta_3: ', t[2])