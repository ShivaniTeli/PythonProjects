import cv2

#Configuring parameters
source = "data.jpg"
destination = "Resize.jpeg"

image = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)

#percent by whic the image is resized
scale_percent = 50
#Calculate by which 50 percent of original dimensions
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (width, height))
cv2.imshow("Resize", output)
cv2.imwrite(destination, output)
cv2.waitKey(0)
