from PIL import Image
# converting jpg to png
im1 = Image.open(r"C:\Users\User\Desktop\SIT-LOGO.jpg")
im1.save(r"C:\Users\User\Desktop\SIT-LOGO.png")

# converting png to jpg
im2 = Image.open(r"C:\Users\User\Desktop\SIT-LOGO.png")
im2.save(r"C:\Users\User\Desktop\SIT-LOGO.jpg")