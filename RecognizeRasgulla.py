from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
im = Image.open('D:\Projects\OCRUsingTesseract\diarymilk\OreoIngredients.jpg')
text = pytesseract.image_to_string(im,lang="eng").replace('\n','')
f = open("D:\Projects\OCRUsingTesseract\OreoIngredients.txt","w+")
f.write(text)
f.close()
print(text)