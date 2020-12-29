import cv2
import sys
import os, os.path

image_path = sys.argv[1]
output_path = sys.argv[2]

if os.path.exists(f'{image_path}/{output_path}'):
    pass
else:
    os.makedirs(f'{image_path}/{output_path}')

try:
	for img in os.listdir(f'{image_path}/'):
		image = cv2.imread(f'{image_path}/{img}')
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faceCascade = cv2.CascadeClassifier(
		    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.3,
		    minNeighbors=3,
		    minSize=(30, 30)
		)

		print("Found {0} Faces!".format(len(faces)))

		i = 0
		for (x, y, w, h) in faces:
		    crop_img = image[y:y+h, x:x+w]
		    i = i+1
		    if os.path.exists(f'{image_path}/{output_path}/{img}'):
		    	pass
		    else:
		    	os.makedirs(f'{image_path}/{output_path}/{img}')
		    	
		    status = cv2.imwrite(f'{image_path}/{output_path}/{img}/{str(i)}.jpg', crop_img)
		    print('done!')

except:
	print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
