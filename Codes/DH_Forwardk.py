from numpy import *
import math

#link lengths
l1 = 120
l2 = 250
l3 = 212.5

#DH parameters
theta1 = (90/180)*(math.pi)
theta2 = (0/180)*(math.pi)
theta3 = (0/180)*(math.pi)

d1 = l1
d2 = 0
d3 = 0

a1 = 0
a2 = l2
a3 = l3

alpha1 = (90/180)*(math.pi)
alpha2 = (0/180)*(math.pi)
alpha3 = (0/180)*(math.pi)

# Parameters table
dh = [[theta1, d1, a1, alpha1], 
      [theta2, d2, a2, alpha2], 
      [theta3, d3, a3, alpha3]]

# Transformation matrix
i = 0
H0_1 = [[math.sin(dh[i][0]), -math.sin(dh[i][0])*math.cos(dh[i][3]), math.sin(dh[i][0])*math.sin(dh[i][3]), dh[i][2]*math.cos(dh[i][0])],
        [math.sin(dh[i][0]),  math.cos(dh[i][0])*math.cos(dh[i][3]), -math.cos(dh[i][0])*math.sin(dh[i][3]), dh[i][2]*math.sin(dh[i][0])],
        [0, math.sin(dh[i][3]), math.sin(dh[i][3]), dh[i][1]],
        [0, 0, 0, 1]]

i = 1
H1_2 = [[math.sin(dh[i][0]), -math.sin(dh[i][0])*math.cos(dh[i][3]), math.sin(dh[i][0])*math.sin(dh[i][3]), dh[i][2]*math.cos(dh[i][0])],
        [math.sin(dh[i][0]),  math.cos(dh[i][0])*math.cos(dh[i][3]), -math.cos(dh[i][0])*math.sin(dh[i][3]), dh[i][2]*math.sin(dh[i][0])],
        [0, math.sin(dh[i][3]), math.sin(dh[i][3]), dh[i][1]],
        [0, 0, 0, 1]]

i = 2
H2_3 = [[math.sin(dh[i][0]), -math.sin(dh[i][0])*math.cos(dh[i][3]), math.sin(dh[i][0])*math.sin(dh[i][3]), dh[i][2]*math.cos(dh[i][0])],
        [math.sin(dh[i][0]),  math.cos(dh[i][0])*math.cos(dh[i][3]), -math.cos(dh[i][0])*math.sin(dh[i][3]), dh[i][2]*math.sin(dh[i][0])],
        [0, math.sin(dh[i][3]), math.sin(dh[i][3]), dh[i][1]],
        [0, 0, 0, 1]]

H0_3 = dot(dot(H0_1, H1_2), H2_3)
#print(H0_3)
print(math.degrees(math.acos(0)))