import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('assets/logo1.jpg')
while True:
# Converting the image to hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
    lower_red = np.array([160, 50, 50])
    upper_red = np.array([180, 255, 255])

# Threshold the HSV image using inRange function to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    plt.figure(figsize=[13, 13])
    plt.subplot(121);
    plt.imshow(image[:, :, ::-1]);
    plt.title("Original Image", fontdict={'fontsize': 25});
    plt.axis('off');
    plt.subplot(122);
    plt.imshow(mask, cmap='gray');
    plt.title("Mask of red Color", fontdict={'fontsize': 25});
    plt.axis('off');

    if cv2.waitKey(1) == ord('q'):
        break

image.release()
cv2.destroyAllWindows()
