"""
Image Processing Example

"""

from PIL import Image, ImageFilter

img = Image.open("d:/develope/ocvtest/f2_new.JPG")

img.show()

blured_img = img.filter(ImageFilter.BLUR)
edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
contour_img = img.filter(ImageFilter.CONTOUR)
median_img = img.filter(ImageFilter.MedianFilter)

blured_img.show()
edge_img.show()
contour_img.show()
median_img.show()

blured_img.save("d:/develope/ocvtest/f2_new_blur.JPG")
edge_img.save("d:/develope/ocvtest/f2_new_edge.JPG")
contour_img.save("d:/develope/ocvtest/f2_new_contour.JPG")