from PIL import Image,ImageOps
image=Image.open("Library/Opencv/1.png")
image=ImageOps.mirror(image)
image.show()