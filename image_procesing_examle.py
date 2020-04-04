"""
Image Processing Example

"""

from PIL import Image

img = Image.open("d:/develope/ocvtest/f2_new.JPG")

grey_img = img.convert("L")
hsv_img = img.convert("HSV")

h, s, v = hsv_img.split()
hh = hsv_img.getchannel("H")

hh.show()
s.show()
v.show()

grey_img.save("d:/develope/ocvtest/grey_img.JPG")
h.save("d:/develope/ocvtest/h_img.JPG")
s.save("d:/develope/ocvtest/s_img.JPG")
v.save("d:/develope/ocvtest/v_img.JPG")