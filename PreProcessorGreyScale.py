#!/usr/bin/env python
# coding: utf-8

# In[56]:


from PIL import Image
column = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\KetchupIngredient.jpg')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 150 else 255, '1')
blackwhite.save("D:\Projects\OCRUsingTesseract\diarymilk\KetchupIngredient_BW.jpg")


# In[67]:


from PIL import Image
column = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\KetchupIngredient_BW.jpg')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 255 if x < 150 else 0, '1')
blackwhite.save("D:\Projects\OCRUsingTesseract\diarymilk\KetchupIngredient_BW1.jpg")


# In[75]:


from tesserocr import PyTessBaseAPI

f = open("D:\Projects\OCRUsingTesseract\KetchupIngredient_BW1.txt","w+")
with PyTessBaseAPI(path='D:/Projects/OCRUsingTesseract/tessdata-master/',lang='eng') as api:
    api.SetImageFile('D:\Projects\OCRUsingTesseract\diarymilk\Jalpeno_nachos_Nutrition_BW.jpg')
    f.write(api.GetUTF8Text())
f.close()


# 

# In[67]:


with open('D:\Projects\OCRUsingTesseract\Rasgulla.txt', 'r') as file:
    data = file.read().replace('\n', '')
print(data)


# In[76]:


from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
im = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\Jalpeno_nachos_Nutrition_BW.jpg')
text = pytesseract.image_to_string(im,lang="eng")
f = open("D:\Projects\OCRUsingTesseract\WingreensMexicanSalsa","w+")
f.write(text)
f.close()
print(text)


# In[94]:


import cv2
import os
import glob
from PIL import Image
import pytesseract
img_dir = "D:\Projects\OCRUsingTesseract\diarymilk" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
print(files)
for f in files:
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    im = Image.open(f)
    text = pytesseract.image_to_string(im,lang="eng")
    imageName = f.split('\\')
    fileNameTxt= imageName[len(y) -1].split('.')[0]+'.txt'
    directory = 'D:\\Projects\\OCRUsingTesseract\\diarymilk\\extracts\\'
    textFile = directory + fileNameTxt 
    f = open(textFile,"w+")
    f.write(text)


# In[90]:


import re
x = "D:\\Projects\\OCRUsingTesseract\\diarymilk\\DairyMilk_nutrition.jpg"
y = x.split('\\')
z = y[len(y) -1].split('.')[0]+'.txt'
directory = "D:\\Projects\\OCRUsingTesseract\\diarymilk\\"
textFile = directory + z
print(textFile)


# In[80]:


from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
im = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\Jalpeno_nachos_Nutrition_BW.jpg')
text = pytesseract.image_to_string(im,lang="eng")
f = open("D:\Projects\OCRUsingTesseract\WingreensMexicanSalsa","w+")
f.write(text)
f.close()
print(text)


# In[ ]:




