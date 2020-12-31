import cv2
import sys
import os, os.path

try:
    image_path = sys.argv[1]
    output_path = sys.argv[2]

    if os.path.exists(f'{image_path}/{output_path}'):
    	pass
    else:
    	os.makedirs(f'{image_path}/{output_path}')
except:
    print('Enter the Command like following : \n python3 face_scrapper.py {Image_Path} {New_Folder_Name} \n . \n . \n . \n Attention! Enter the path without {}, {} are only for user understanding :)')



for img in os.listdir(f'{image_path}/'):
    if img.endswith('.jpg') or img.endswith('.png') or img.endswith('.webp') or img.endswith('.jpeg'):
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

        print(f"Found {len(faces)} Faces!")

        i = 0
        for (x, y, w, h) in faces:
            crop_img = image[y:y+h, x:x+w]

            if os.path.exists(f'{image_path}/{output_path}/{img}'):
                pass
            else:
                os.makedirs(f'{image_path}/{output_path}/{img}')

            status = cv2.imwrite(f'{image_path}/{output_path}/{img}/{str(i)}.png', crop_img)

            i = i+1
            print('done!')
            continue
    else:
    	print('No images to process in the given directory!')
    continue

