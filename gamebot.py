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

    #print(diff.getbbox())

    if diff.getbbox():
        #print("pic is different ")
        jump()

        #  diff.show();
    else:
        pass;
        #print("pic is same")


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
    time.sleep(0.1)
    pyautogui.keyUp('space')
    #print('Jump')


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
#x=607

takescreenshot()
image = "E:\pic\\screenshot1.png"
    #    # 1st paratemr is left widht. decreasing it will increase left porting
    #     # 2nd paramer is height
    #     # 3rd parameter is length

croppedpicvalues=pyautogui.locateOnScreen(r'E:\pic\\trex.png')  # If the file is not a png file it will not wor


# width and height are of image that we searched  . we can also see the in the details of trex image it will show the width 42 and height 39
# this will give cropped image of trex(x,y,width+x,height+y)
# we can increase width independenly of any value but must be greater than x
# we can increase height independently of any value but must be greater than y
#crop(image, (croppedpicvalues[0], croppedpicvalues[1], croppedpicvalues[0]+croppedpicvalues[2],croppedpicvalues[1]+croppedpicvalues[3]), 'E:\pic\\cropped.png')


while(croppedpicvalues==None):
    croppedpicvalues = pyautogui.locateOnScreen(r'E:\pic\\trex.png')

croppedpicvaluesend=pyautogui.locateOnScreen(r'E:\pic\\end.png')

while(croppedpicvaluesend==None):
    croppedpicvaluesend = pyautogui.locateOnScreen(r'E:\pic\\end.png')


#byincreasing 3rd paraemter onlt  the length increases from starting coord x

x=(croppedpicvalues[0]+croppedpicvaluesend[0])/2;
w=x+croppedpicvalues[2]-37;# to increase width. another approach will be to give trex of image of having greater widh
x=x-211;

y=croppedpicvalues[1];

h=croppedpicvalues[1]+croppedpicvalues[3];



originalx=x;
originalw=w;
originalw2=w;
  # is staring x point
# w is width of p ic
# y is starting y index vertically. by increasing y the crop pic go down
# h is height

pyautogui.moveTo(croppedpicvaluesend)
jump();

counter=0;
max=0;
bestx=x;
besty=y;
while True:
    counter=counter+1;
    takescreenshot()
    image = "E:\pic\\screenshot1.png"
    crop(image, (x, y, w, h), 'E:\pic\\cropped.png')
    imagecomparison()
    x=x+0.10
    w=w+0.10
    if(pyautogui.locateOnScreen(r'E:\pic\\gameover.png')!=None or pyautogui.locateOnScreen(r'E:\pic\\gameover2.png')!=None ):
         jump();
         if(counter>=max):
             bestx=originalx;
             besty=originalw
             max=counter;
             print("BEST X, Y are ", bestx, besty)
             originalw=w-3;

         originalw = originalw +3;
         if(originalw==950):
             originalw=originalw2;
             originalx=originalx-5;


         x=originalx;
         w=originalw;
         counter=0;






