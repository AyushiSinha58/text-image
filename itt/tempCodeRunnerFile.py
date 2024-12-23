import torch
from PIL import Image
import pytesseract


image_path = r"C:\Users\Ayushi\Desktop\GitStuff\TEXT TO IMAGE\text-image\itt\practice image.jpg"

img = Image.open(image_path)
print(pytesseract.image_to_string(img))
img.show()
