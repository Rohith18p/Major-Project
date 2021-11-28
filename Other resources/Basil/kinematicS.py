import numpy as np
import cv2
import os, sys
import traceback
import time
import simpy

import task_1b
import task_1a_part1
import task_2a

def get_angles(pos_orientation,present_dh_params,link_lengths):
    """""""""""""""""""""""""""""""""""""""
    input : pos_orientation - desired position and orientation of end effector, numpy array of size [3,4], as per DH convention.
            present_dh_params - current dh parameters, list of the form [theta1p,theta2,theta3,theta4,theta5]
    output : angles of rotation of joint
    link_lengths : list of link lengths of the form [l1,l2,l3,l4,l5]

    """""""""""""""""""""""""""""""""""""""

    theta1p = np.arctan2(pos_orientation[1][3],pos_orientation[0][3])
    theta234 = np.arctan2(- (pos_orientation[0][2]*np.cos(theta1p) + pos_orientation[1][2]*np.sin(theta1p) ), pos_orientation[2][2] )
    #print(- (pos_orientation[0][2]*np.cos(theta1p) + pos_orientation[1][2]*np.sin(theta1p) ), -pos_orientation[2][2])
    #print(theta234)
    A = link_lengths[3]
    B = link_lengths[2]
    C = (pos_orientation[0][3]/np.cos(theta1p)) + link_lengths[4]*np.sin(theta234) - link_lengths[1]
    D = pos_orientation[2][3] - link_lengths[0] - link_lengths[4]*np.cos(theta234)

    #print(A,B,C,D)
    cosTheta3 = (np.square(C) + np.square(D) - np.square(A) - np.square(B))/ (2*A*B)
    print(cosTheta3)
    cosTheta3 = np.clip(cosTheta3,-1,1)
    sinTheta3 = np.sqrt(1- np.square(cosTheta3))

    theta3 = np.arctan2(sinTheta3,cosTheta3)
    r = A*np.cos(theta3) + B
    s= A*np.sin(theta3)

    theta2 = np.arctan2( (r*D - s*C),(r*C + s*D))

    theta4 = theta234 - theta2 - theta3

    theta5 = np.arctan2( -(pos_orientation[0][0]*np.sin(theta1p) - pos_orientation[1][0]*np.cos(theta1p)),-(pos_orientation[0][1]*np.sin(theta1p) - pos_orientation[1][1]*np.cos(theta1p)) )

    return theta1p,theta2,theta3,theta4,theta5

client_id = task_2a.init_remote_api_server()
vision_sensor_handle = 0
return_code = task_2a.start_simulation()

link_lengths = [0.1,0.1,0.4,0.2,0.25]
pos = np.array([[0,-1,0,-0.5],[1,0,0,0.3],[0,0,1,0.55]])
print(pos)
prev_thetas = [0,np.pi/2,0,-np.pi/2,np.pi/2]
current_thetas = get_angles(pos,prev_thetas,link_lengths)


print(current_thetas)


a1 = current_thetas[0]
a2 = current_thetas[1] - np.pi/2
a3 = -current_thetas[2]
a4 = -(-np.pi/2 - current_thetas[3])
a5  = -(np.pi/2 - current_thetas[4])

print(a1,a2,a3,a4,a5)

_, mot1 = sim.simxGetObjectHandle(client_id , 'r1',sim.simx_opmode_blocking)
_, mot2 = sim.simxGetObjectHandle(client_id , 'r2',sim.simx_opmode_blocking)
_, mot3 = sim.simxGetObjectHandle(client_id , 'r3',sim.simx_opmode_blocking)
_, mot4 = sim.simxGetObjectHandle(client_id , 'r4',sim.simx_opmode_blocking)
_, mot5 = sim.simxGetObjectHandle(client_id , 'r5',sim.simx_opmode_blocking)


rc = sim.simxSetJointTargetPosition(client_id,mot5,a5,sim.simx_opmode_oneshot)
sim.simxSetJointTargetPosition(client_id,mot1,a1,sim.simx_opmode_oneshot)
#time.sleep(1)
sim.simxSetJointTargetPosition(client_id,mot2,a2,sim.simx_opmode_oneshot)
#time.sleep(1)
sim.simxSetJointTargetPosition(client_id,mot3,a3,sim.simx_opmode_oneshot)
#time.sleep(1)
rc = sim.simxSetJointTargetPosition(client_id,mot4,a4,sim.simx_opmode_oneshot)
#time.sleep(2)

