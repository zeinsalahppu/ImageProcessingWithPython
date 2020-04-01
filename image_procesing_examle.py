"""
Image Processing Example

"""

from PIL import Image
img = Image.open("d:/develope/ocvtest/f1.JPG")

print(img.format)
print(img.size)
print(img.mode)

img.show()

small_img = img.crop((0, 0, 300, 200))

small_img.show()

small_img.save("d:/develope/ocvtest/f1_new.JPG")