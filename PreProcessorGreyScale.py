#!/usr/bin/env python
# coding: utf-8

# In[90]:


from PIL import Image
column = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\Rasgulla.jpg')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 30 else 255, '1')
blackwhite.save("D:\Projects\OCRUsingTesseract\diarymilk\Rasgulla_BW.jpg")


# In[92]:


from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
im = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\OreoIngredients.jpg')
text = pytesseract.image_to_string(im,lang="eng").replace('\n','')
f = open("D:\Projects\OCRUsingTesseract\OreoIngredients.txt","w+")
f.write(text)
f.close()
print(text)


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




