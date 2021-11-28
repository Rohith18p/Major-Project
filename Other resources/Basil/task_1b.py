'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			NB-270
# Author List:		SAFA PARY
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					left_right, top_bottom
# Global variables:	
# 					-


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
def left_right(img,x,y):
	"""Function to find the values of left and right sides of a cell
		The function is executed as follows:
		Consider a point (x,y). We have to find whether there is a wall on the left side of that particular cell. Three points are considered for this purpose: 
		(x-8,y), (x,y) and (x+8,y). This is because the point (x,y) might not always lie on the wall, and the actual wall might be somewhere near the point (x,y). 
		That's why, a range of +-8 is used. If any of these points are 'red' in colour, the value is updated to 1.(The maze has been painted to red colour for 
		easy identification of walls). Same procedure is followed for detecting the wall on the right side. Exception handling is used in case 'Index is Out of 
		Bounds for Axis With Size Error' arises when points of different range are considered.
	"""
	try:
		if (img[y,x-8,2]==[255]):
			return 1
		elif (img[y,x,2]==[255]):
			return 1
		elif (img[y,x+8,2]==[255]):
			return 1
		else:
			return 0
	except:
		return 1

def top_bottom(img,x,y):
	"""Function to find the values of left and right sides of a cell
		The function is executed as follows:
		Consider a point (x,y). We have to find whether there is a wall on the top side of that particular cell. Three points are considered for this purpose:
		(x,y-8), (x,y) and (x,y+8). This is because the point (x,y) might not always lie on the wall, and the actual wall might be somewhere near the point (x,y).
		That's why, a range of +-8 is used. If any of these points are 'red' in colour, the value is updated to 1.(The maze has been painted to red colour for
		easy identification of walls). Same procedure is followed for detecting the wall on the bottom side. Exception handling is used in case 'Index is Out of
		Bounds for Axis With Size Error' arises when points of different range are considered.
	"""


	try:
		if (img[y,x,2]==[255]):
			return 1
		elif (img[y-8,x,2]==[255]):
			return 1
		elif (img[y+8,x,2]==[255]):
			return 1
		else:
			return 0
	except:
		return 1



##############################################################


def applyPerspectiveTransform(input_img):

	"""
	Purpose:
	---
	takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

	Input Arguments:
	---
	`input_img` :   [ numpy array ]
		maze image in the form of a numpy array
	
	Returns:
	---
	`warped_img` :  [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Example call:
	---
	warped_img = applyPerspectiveTransform(input_img)
	"""

	warped_img = None

	##############	ADD YOUR CODE HERE	##############
	gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (7,7), 0)
	ret,thresh = cv2.threshold(blur,230,255,cv2.THRESH_BINARY)

	#Finding the contour with maximum area
	cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0]
	c = max(cnts, key=cv2.contourArea)

	#Finding the top_left(tl), top_right(tr), bottom_left(bl) and bottom_right(br) points of the maze
	s = np.sum(c, axis=1)
	b = np.squeeze(c,axis=1)
	d = np.diff(b, axis = 1)
	tl = c[np.argmin(np.sum(s,axis=1))]
	br = c[np.argmax(np.sum(s,axis=1))]
	tr = c[np.argmin(d)]
	bl = c[np.argmax(d)]

	points = np.zeros((4, 2), dtype = "float32")
	points[0],points[1],points[2],points[3] = tl, tr, br, bl
	#Specifying the destination array(dest) as 1280x1280, and then applying Perspective Transform
	dest = np.array([[0, 0],[1279, 0],[1279, 1279],[0, 1279]], dtype = "float32")
	M = cv2.getPerspectiveTransform(points, dest)
	warped_img = cv2.warpPerspective(gray, M, (1280, 1280))
	
	##################################################

	return warped_img


def detectMaze(warped_img):

	"""
	Purpose:
	---
	takes the warped maze image as input and returns the maze encoded in form of a 2D array

	Input Arguments:
	---
	`warped_img` :    [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Returns:
	---
	`maze_array` :    [ nested list of lists ]
		encoded maze in the form of a 2D array

	Example call:
	---
	maze_array = detectMaze(warped_img)
	"""

	maze_array = []

	##############	ADD YOUR CODE HERE	##############
	#Changing the colourspace of warped_img to HSV and thresholding black colour. 
	warped = warped_img.copy()
	img_HSV = cv2.cvtColor(warped, cv2.COLOR_BGR2HSV)
	thresh = cv2.inRange(img_HSV, (0,0,0), (180,255,120))

	#Changing all black points to red colour.
	for x in range(0,img_HSV.shape[0]):
		for y in range(0,img_HSV.shape[1]):
			if thresh[x,y]>150:
				cv2.circle(warped,(y,x),1,(0,0,255),1)

	#Finding the height and width of each cell on the maze
	h = int(np.ceil(warped.shape[1]/10))
	w = int(np.ceil(warped.shape[0]/10))
	#Weight of each side of the cell
	wt = np.array([1,2,4,8])
	x,y = 0,0

	for i in range(0,10):
		m = []
		for j in range(0,10):
			value = np.zeros([4],dtype='int64')

			#Assigning values to the array 'value'
			value[0] = left_right(warped,x,int(y+(h/2)))
			value[1] = top_bottom(warped,int(x+(w/2)),y)
			value[2] = left_right(warped,x+w,int(y+(h/2)))
			value[3] = top_bottom(warped,int(x+(w/2)),y+h)
        	
			#Finding the cell number of each cell
			cell = int(np.dot(wt,value))
			m.append(cell)

			x = x+w
		y = y+h
		x = 0
		maze_array.append(m)
	
	
	##################################################

	return maze_array


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv2.imshow('warped_img_0' + str(file_num), warped_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv2.imshow('warped_img_0' + str(file_num), warped_img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

