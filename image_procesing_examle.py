"""
Image Processing Example

"""

from PIL import Image

img = Image.open("d:/develope/ocvtest/f2_new.JPG")

size = img.size
print(size)

neg_img1 = Image.new('RGB', size)

for i in range(size[0]):
    for j in range(size[1]):
        in_pixel = img.getpixel((i, j))
        out_pixel = (255 - in_pixel[0], 255 - in_pixel[1], 255 - in_pixel[2])
        neg_img1.putpixel((i, j), out_pixel)

neg_img2 = img.point(lambda i: 255-i)

neg_img1.show()
neg_img2.show()

neg_img1.save("d:/develope/ocvtest/f1_new_neg1.JPG")
neg_img2.save("d:/develope/ocvtest/f1_new_neg2.JPG")