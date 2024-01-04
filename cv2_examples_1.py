import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('dog_backpack.jpg')

print(f"How does a jpg look like when read by cv2's imread function? Something like this:\n\n", im)

print("\nLet's show the image via matplotlib's pyplot's imshow and then show:\n")

print("\nWait, that's not quite right. We got the image with... Inverted colors? Let's use cv2's cvtColor to fix the colors.\nimg_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)\n")
plt.imshow(im)
plt.show()

print("\nLooking good, just like the original. Can we show the image in grayscale?\nimg_grayscale = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)\n")

img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.show()


print("\nWait, what? That's not gray at all!\nHuh, apparently imshow treated the gray image as if it was a colorful image, and tried mapping it as if it were colorful.\nLet's try the imshow command with a specific parameter for a gray image:\nplt.imshow(img_grayscale, cmap='gray')\n")

img_grayscale = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

plt.imshow(img_grayscale)
plt.show()



print("\nNow that's more like it!")

plt.imshow(img_grayscale, cmap='gray')
plt.show()
