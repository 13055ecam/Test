import cv2, numpy as np
import time
import sys

rangelower = np.array([0, 100, 100], dtype=np.uint8)
rangeupper = np.array([255, 255, 255], dtype=np.uint8)
hue = 128
wid = 256

# Set color range
# BGR lower and upper ranges for each color

blue = [([35, 0, 0], [255,255,85])]
yellow = [([100, 200, 90], [130,255,255])]
green = [([120, 210, 120],[190,230,140])]
orange = [([150, 180, 90], [170, 200,255])]
black = [([0, 0, 0], [150, 100, 75])]


filename = "opencv.png" 
frame_image = cv2.imread(filename)
image = frame_image

# Set frame position of each cube

# We select a window on the picture for each cube so we need x and y positions


#   [cube1, cube2, cube3]

# Minimum x value for each of the three cubes
xmin = [124, 250, 379]
# Maximum x value for each of the three cubes
xmax = [210, 349, 476]
# Minimum y value for each of the three cubes
ymin = [230, 230, 230]
# Maximum y value for each of the three cubes
ymax = [324, 324, 324]



# Observation window selection for each cube
cube1 = image[ymin[0]:ymax[0], xmin[0]:xmax[0]]
cube2 = image[ymin[1]:ymax[1], xmin[1]:xmax[1]]
cube3 = image[ymin[2]:ymax[2], xmin[2]:xmax[2]]

cubes = [cube1, cube2, cube3]

# Color detection for each of the three cubes
for i in range(3):

# Blue color detection

	for(lower,upper) in blue:
	    # print("test1 : " + str(lower))
	    # Lowest BGR values for blue
	    lower = np.array(lower,dtype="uint8")
	    # Highest BGR values for blue
	    upper = np.array(upper,dtype="uint8")
	mask = cv2.inRange(cubes[i],lower,upper)
	# print("test2 : " + str(mask))
	b = sum(sum(mask))
	print ("blue for cube nbr" + str(i+1) + " : "  + str(b))

	    
	# Green color detection

	for(lower,upper) in green:
	    # Lowest BGR values for green
	    lower = np.array(lower,dtype="uint8")
	    # Highest BGR values for green
	    upper = np.array(upper,dtype="uint8")
	mask = cv2.inRange(cubes[i],lower,upper)
	g = sum(sum(mask))
	print ("green for cube nbr" + str(i+1) + " : " + str(g))


	# Yellow color detection

	for(lower,upper) in yellow:
	    # Lowest BGR values for yellow
	    lower = np.array(lower,dtype="uint8")
	    # Highest BGR values for yellow
	    upper = np.array(upper,dtype="uint8")
	mask = cv2.inRange(cubes[i],lower,upper)
	y = sum(sum(mask))
	print ("yellow for cube nbr" + str(i+1) + " : " + str(y))


	# Orange color detection

	for(lower,upper) in orange:
	    # print("test1 : " + str(lower))
	    # Lowest BGR values for orange
	    lower = np.array(lower,dtype="uint8")
	    # Highest BGR values for orange
	    upper = np.array(upper,dtype="uint8")
	# print("test cubes : " + str(cubes[i]))
	mask = cv2.inRange(cubes[i],lower,upper)
	# print("testtest " + str(mask))
	o = sum(sum(mask))
	print ("orange for cube nbr" + str(i+1) + " : " + str(o))


	# Black color detection

	for(lower,upper) in black:
	    # Lowest BGR values for black
	    lower = np.array(lower,dtype="uint8")
	    # Highest BGR values for black
	    upper = np.array(upper,dtype="uint8")
	mask = cv2.inRange(cubes[i],lower,upper)
	bl = sum(sum(mask))
	print ("black for cube nbr" + str(i+1) + " : " + str(bl))


	if (b < 1000 and y < 1000 and g < 1000 and o < 1000 and bl < 1000):
	    print ("no block for cube nbr" + str(i+1) + "\n")
	elif (g > b and g > y and g > o):
	    print ("block green for cube nbr" + str(i+1) + "\n")
	    if (o > b and o > y and o > g):
	        print ("block orange for cube nbr" + str(i+2) + "\n")
	        print("cube n3 is yellow")
	else:
	    print ("problema")

	# time.sleep(1)
	cv2.imshow("cube",cube1)
	cv2.imshow("cube2", cube2)

	cv2.imshow("cube3", cube3)

	# Draw rectangles on the picture to see which part is selected

	cv2.rectangle(image,(xmin[0],ymin[0]),(xmax[0],ymax[0]),(0,0,255),2)
	#cv2.rectangle(image, (250, 200), (350, 300), (0, 255, 255), 2)
	cv2.rectangle(image, (xmin[1], ymin[1]), (xmax[1], ymax[1]), (0, 255, 255), 2)
	#cv2.rectangle(image, (425, 200), (525, 300), (255, 255, 255), 2)
	cv2.rectangle(image, (xmin[2], ymin[2]), (xmax[2], ymax[2]), (255, 255, 255), 2)

cv2.namedWindow("original",cv2.WINDOW_NORMAL);
cv2.imshow("original",image)
key = cv2.waitKey(0) & 0xFF

combinaison = []
#orange|noir|vert
if (colorsCubes[0][3] > colorsCubes[0][0] and colorsCubes[0][3] > colorsCubes[0][1]  and colorsCubes[0][2] > colorsCubes[0][2] and colorsCubes[0][3]> colorsCubes[0][4] and colorsCubes[1][4] > colorsCubes[1][0]
	and colorsCubes[1][4] > colorsCubes[1][1]  and colorsCubes[1][4] > colorsCubes[1][2]and  colorsCubes[1][4] > colorsCubes[1][3]):
	        combinaison.extend(("orange","noir","vert"))
	        
#jaune|noir|bleu
elif (colorsCubes[0][2] > colorsCubes[0][0] and colorsCubes[0][2] > colorsCubes[0][1] and colorsCubes[0][2] > colorsCubes[0][3] and colorsCubes[0][2] > colorsCubes[0][4] and colorsCubes[1][4] > colorsCubes[1][0] 
	and colorsCubes[1][4] > colorsCubes[1][1] and colorsCubes[1][4] > colorsCubes[1][2] and colorsCubes[1][4] > colorsCubes[1][3]):
	      	combinaison.extend(("jaune","noir","bleu"))


#bleu|vert|orange
elif (colorsCubes[0][0] > colorsCubes[0][1] and colorsCubes[0][0] > colorsCubes[0][2] and colorsCubes[0][0] > colorsCubes[0][3] and colorsCubes[0][0] > colorsCubes[0][4] and colorsCubes[1][1] > colorsCubes[1][0]
	and colorsCubes[1][1] > colorsCubes[1][2] and colorsCubes[1][1] > colorsCubes[1][3] and colorsCubes[1][1] > colorsCubes[1][4]):
	        combinaison.extend(("bleu","vert","orange"))            
#jaune|vert|noir
elif (colorsCubes[0][2] > colorsCubes[0][0]and colorsCubes[0][2] > colorsCubes[0][1] and colorsCubes[0][2] > colorsCubes[0][3] and colorsCubes[0][2] > colorsCubes[0][4] and colorsCubes[1][1] > colorsCubes[1][0] 
	and colorsCubes[1][1] > colorsCubes[1][2] and colorsCubes[1][1] > colorsCubes[1][3] and colorsCubes[1][1] > colorsCubes[1][4]):
	        combinaison.extend(("jaune","vert","noir"))
#noir|jaune|orange
elif (colorsCubes[0][4] > colorsCubes[0][0] and colorsCubes[0][4] > colorsCubes[0][1] and colorsCubes[0][4] > colorsCubes[0][2] and colorsCubes[0][4] > colorsCubes[0][3]
	and colorsCubes[1][2] > colorsCubes[1][0] and colorsCubes[1][2] > colorsCubes[1][1] and colorsCubes[1][2] > colorsCubes[1][3] and colorsCubes[1][3] > colorsCubes[1][4]):
	        combinaison.extend(("noir","jaune","orange"))
#vert|jaune|bleu
elif (colorsCubes[0][1] > colorsCubes[0][0] and colorsCubes[0][1] > colorsCubes[0][2] and colorsCubes[0][1] > colorsCubes[0][3] and colorsCubes[0][1] > colorsCubes[0][4]
	and colorsCubes[1][2] > colorsCubes[1][0] and colorsCubes[1][2] > colorsCubes[1][1] and colorsCubes[1][2] > colorsCubes[1][3] and colorsCubes[1][2] > colorsCubes[1][4]):
	        combinaison.extend(("vert","orange","bleu"))

#bleu|orange|noir
elif (colorsCubes[0][0] > colorsCubes[0][1] and colorsCubes[0][0] > colorsCubes[0][2] and colorsCubes[0][0] > colorsCubes[0][3] and colorsCubes[0][0] > colorsCubes[0][4]
	and colorsCubes[1][3] > colorsCubes[1][0] and colorsCubes[1][3] > colorsCubes[1][1] and colorsCubes[1][3] > colorsCubes[1][2] and colorsCubes[1][3] > colorsCubes[1][4]):
	        combinaison.extend(("bleu","orange","noir"))

#vert|orange|jaune
elif (colorsCubes[0][1] > colorsCubes[0][0]and colorsCubes[0][1] > colorsCubes[0][2]and colorsCubes[0][1] > colorsCubes[0][3] and colorsCubes[0][1] > colorsCubes[0][4]
	and colorsCubes[1][3] > colorsCubes[1][0] and colorsCubes[1][3] > colorsCubes[1][1] and colorsCubes[1][3] > colorsCubes[1][2] and colorsCubes[1][3] > colorsCubes[1][4]):
	        combinaison.extend(("vert","orange","jaune"))

#noir|bleu|vert
elif (colorsCubes[0][4] > colorsCubes[0][0] and colorsCubes[0][4] > colorsCubes[0][1] and colorsCubes[0][4] > colorsCubes[0][2] and colorsCubes[0][4] > colorsCubes[0][3]
	and colorsCubes[1][0] > colorsCubes[1][1] and colorsCubes[1][0] > colorsCubes[1][2] and colorsCubes[1][0] > colorsCubes[1][3] and colorsCubes[1][0] > colorsCubes[1][4]):
	        combinaison.extend(("noir","bleu","vert"))

#orange|bleu|jaune
elif (colorsCubes[0][3] > colorsCubes[0][0] and colorsCubes[0][3] > colorsCubes[0][1] and colorsCubes[0][3] > colorsCubes[0][2] and colorsCubes[0][3] > colorsCubes[0][4]
	and colorsCubes[1][0] > colorsCubes[1][1] and colorsCubes[1][0] > colorsCubes[1][2] and colorsCubes[1][0] > colorsCubes[1][3] and colorsCubes[1][0] > colorsCubes[1][4]):
	        combinaison.extend(("orange","bleu","jaune"))
else:
	print("no combinaison")
print(combinaison)

