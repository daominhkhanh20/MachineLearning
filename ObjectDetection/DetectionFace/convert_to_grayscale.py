import cv2
from PIL import Image #lib for processing image

catface_cascade=cv2.CascadeClassifier('catface_detector.xml')
humanface_cascade=cv2.CascadeClassifier('humnafcae_detector.xml')

newsize=(600,600)
image1=Image.open('3.jpg')
image_new1=image1.resize(newsize)

image2=Image.open('4.jpg')
image_new2=image2.resize(newsize)

#convert to grayscale
image_new1.convert('L').save('ready3.jpg')
image_new2.convert('L').save('ready4.jpg')

