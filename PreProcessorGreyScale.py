#!/usr/bin/env python
# coding: utf-8

# In[90]:


from PIL import Image
column = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\Rasgulla.jpg')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 30 else 255, '1')
blackwhite.save("D:\Projects\OCRUsingTesseract\diarymilk\Rasgulla_BW.jpg")


# In[92]:


from tesserocr import PyTessBaseAPI

f = open("D:\Projects\OCRUsingTesseract\Rasgulla.txt","w+")
with PyTessBaseAPI(path='D:/Projects/OCRUsingTesseract/tessdata-master/',lang='eng') as api:
    api.SetImageFile('D:\Projects\OCRUsingTesseract\diarymilk\Rasgulla_BW.jpg')
    f.write(api.GetUTF8Text())
f.close()


# 

# In[67]:


with open('D:\Projects\OCRUsingTesseract\Rasgulla.txt', 'r') as file:
    data = file.read().replace('\n', '')
print(data)


# In[97]:


from PIL import Image
import pytesseract
im = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\Rasgulla.jpg')
text = pytesseract.image_to_string(im,lang="eng")
print(text)


# In[ ]:




