
# coding: utf-8

# In[117]:


from PIL import Image, ImageDraw
import face_recognition
import math, cv2, numpy as np

# Load the jpg file into a numpy array
# Choose a picture 'richard_curtis.jpg' 'rihanna.jpg' 'ryan_gosling.jpg' 'arnie.jpg' 'drake.jpg' 'kim_kardashian'
image = face_recognition.load_image_file("richard_curtis.jpg")
# Choose a noise 'sniffer.png' 'sourcerer.png' 'teeth.png' 'viking.png' 'cook.png' 'djboogy.png' 'drnose.png' 'owl.png'
nose_pic = Image.open('teeth.png', mode='r')

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

print('nose_tip coordinates',face_landmarks['nose_tip'])
print('nose_bridge coordinates',face_landmarks['nose_bridge'])

# left part of the nose tip, adding -5 as the picture of the nose is smaller than picture size
left = face_landmarks['nose_tip'][0][0] -5
# right part of the nose tip, adding +5 as the picture of the nose is smaller than picture size
right = face_landmarks['nose_tip'][4][0] +5
# lower part of the nose bridge
lower = face_landmarks['nose_tip'][2][1] +2
# upper part of the nose bridge, based on lower ground as nose picture is a square
upper = lower - (right-left)


region = (left,upper,right,lower)
print('region(left,upper,right,lower)', region)

#resizing nose_pic to fit region size

new_w = right-left
new_h = new_w
#new_h = lower-upper
print("pic_size",(new_w,new_h))

print('original nose pic size', nose_pic.size)

nose_pic = nose_pic.resize((new_w, new_h), Image.ANTIALIAS)
test = nose_pic.size
print('nose',test)

# Paste nose to picture
pil_image.paste(nose_pic, box=region,mask=nose_pic )

pil_image.show()


