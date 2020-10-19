import cv2

catface_cascade=cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
humanface_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img1=cv2.imread('ready3.jpg')
img2=cv2.imread('ready4.jpg')

#detect face in image
human_faces = humanface_cascade.detectMultiScale(img1,scaleFactor=1.3, minNeighbors=5, minSize=(75, 75))
cat_faces = catface_cascade.detectMultiScale(img2, scaleFactor=1.3,minNeighbors=5, minSize=(75, 75))

#draw rectangle
for (i, (x, y, w, h)) in enumerate(human_faces):
   cv2.rectangle(img1, (x, y), (x+w, y+h), (220, 90, 230), 3)
   cv2.putText(img1, "Human Face - #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 90, 230), 2)

for (i, (x, y, w, h)) in enumerate(cat_faces):
   cv2.rectangle(img2, (x, y), (x+w, y+h), (0,255, 0), 3)
   cv2.putText(img2, "Cat Faces - #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

cv2.imwrite('face_human_rectangl.jpg',img1)
cv2.imwrite('face_cat_rectangle.jpg',img2)
