
# coding: utf-8

# In[5]:


from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("richard_curtis.jpg")
nose_pic = Image.open('sniffer.png', mode='r')
nose_pic.thumbnail((30,40), resample=0)

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks['nose_tip'])
for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

print(face_landmarks['nose_tip'][2])
print(face_landmarks['nose_bridge'][1])

pil_image.paste(nose_pic, box=face_landmarks['left_eye'][3] ,mask=nose_pic )

pil_image.show()


