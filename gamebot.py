import cv2
import pyautogui
import time
from PIL import Image
import numpy as np
from numpy import asarray
from PIL import ImageChops

pyautogui.FAILSAFE = False;


def imagecomparison():
    img = Image.open("E:\pic\\original.png")

    img2 = Image.open("E:\pic\\cropped.png")
    # difference = cv2.subtract(img, img2)
    # result = not np.any(difference)

    diff = ImageChops.difference(img, img2)

    print(diff.getbbox())

    if diff.getbbox():
        print("pic is different ")
        jump()

        #  diff.show();
    else:
        print("pic is same")


def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    # cropped_image.show()


def jump():
    # this will keep on pressing until we write function of taking it up
    pyautogui.keyDown('space')
    time.sleep(0.5)
    pyautogui.keyUp('space')
    print('Jump')


def takescreenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'E:\pic\\screenshot1.png')

    img = cv2.imread('E:\pic\\screenshot1.png')


def printscreenshot():
    img = cv2.imread('E:\pic\\screenshot1.png')
    cv2.imshow('imag  e', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
time.sleep(0.5)
# takescreenshot()
# image = "E:\pic\\screenshot1.png"
# crop(image, (450, 380, 607, 420), 'E:\pic\\cropped.png')
generations=1;
x=607
while True:
    takescreenshot()
    image = "E:\pic\\screenshot1.png"
    #    # 1st paratemr is left widht. decreasing it will increase left porting
    #     # 2nd paramer is height
    #     # 3rd parameter is length
    crop(image, (450, 380, x, 420), 'E:\pic\\cropped.png')
    imagecomparison()
    x=x+0.20;

