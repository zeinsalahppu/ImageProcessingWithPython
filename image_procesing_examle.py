"""
Image Processing Example

"""

from PIL import Image

img = Image.open("d:/develope/ocvtest/f2_new.JPG")

resized_img = img.resize((200, 300))
rotated_img = img.rotate(45)
flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)

resized_img.show()
rotated_img.show()
flipped_img.show()

resized_img.save("d:/develope/ocvtest/f1_new_resized.JPG")
rotated_img.save("d:/develope/ocvtest/f1_new_rotated.JPG")
flipped_img.save("d:/develope/ocvtest/f1_new_flipped.JPG")
