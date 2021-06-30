# Importing Image and ImageGrab module from PIL package
from PIL import Image, ImageGrab

img = Image.new('RGB', (60, 30), color = 'red')
img.save('./Images/pil_red.png')

# using the grab method
im2 = ImageGrab.grab(bbox=None)
im2.save('./Images/Screenshot.png')

print(type(im2))

im2.show()