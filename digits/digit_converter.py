# This script convert binary images in a folder to data arrays suitable for
# frame buffers for LCDs such as SSD1306 using Micropytho's framebuf.MONO_HLSB
# How to use:
#   1. Place this scrit in a folder
#   2. Using a drawing app of your choice (e.g. Windows Paint),
#      draw digits in an grayscale images of pixel size (height, width) = (32,24).
#      Name the image for digit 0 as "0.png", 1 for "1.png" etc.
#   3. Save the digit images in a folder "rawdigits", and place this folder at the same level as this script
#   4. Change current directory to the folder containing this script and run this script
#      It requiers numpy and cv2, which can be installed by pip, conda etc
#   5. The script creates "digits.py" in the "rawdigits" folder with custom digit hex arrays.
#      Copy "digits.py" to your Pico to display costom digits
# Notes:
#     If the input image is grayscale, it wll be thresholded.

import os
import numpy as np
import cv2

# Parameters =================================================
inputimgdirname = r"rawdigits" # folder path to the binary image files to be converted to data arrays
savefilename = inputimgdirname+r"/digits.py" # folder path to which the output data array will be saved
threshold = np.uint8(255/2) # image threshold for binarizing input images
blackison = True # True if black pixels (0) in the input image correspond to on (1) in the output data array.

endian = 1 # 0=little, 1=big, little endian means the first pixel in a series of 8 pixels to be converted to a hex will be the lowest binary digit (i.e. it will get 2^0 multiplied)

imgfmts = [".png",".PNG",".jpg",".JPG",".jpeg",".JPEG"] #  accepted input image formats
comments = "# hex arrays of digits to be converted to framebuffer via framebuf.FrameBuffer(_,24,32,framebuf.MONO_HLSB) \n# (height,width) = (32,24) for digits d0 to d9, = (32,8) for colon, = (16,24) for cake \n# Font: \n"
# Parameters (end) ===========================================

if __name__ == "__main__":

    if not os.path.exists(inputimgdirname):
        raise ValueError("inputimgdirname = "+str(inputimgdirname)+" does not exist.")
    else:
        imgfilenames = [f for f in os.listdir(inputimgdirname) if os.path.isfile(os.path.join(inputimgdirname,f)) and (os.path.splitext(f)[1] in imgfmts)]

        file = open(savefilename,"a")
        file.write(comments)
        file.close()
        for imgfilename in imgfilenames:
            digitarray = cv2.imread(os.path.join(inputimgdirname,imgfilename),0)
            imgsize = digitarray.shape[:2]
            if imgsize[0]%8 != 0 or imgsize[1]%8 != 0:
                raise ValueError("imgsize[0] or imgsize[1] of "+str(imgfilename)+" is not divisible by 8. Check the input image size again.")

            else:
                digitarray = cv2.threshold(digitarray,threshold,255,cv2.THRESH_BINARY_INV if blackison else cv2.THRESH_BINARY)[1].astype(bool)

#                digitarray2 = np.zeros((int(imgsize[0]*imgsize[1]),),dtype=np.int32)
#                for row in range(0,int(imgsize[0]/8)):
#                    for col in range(0,imgsize[1]):
#                        digitarray2[row*8*imgsize[1]+col*8:row*8*imgsize[1]+col*8+8] = digitarray[row*8:(row+1)*8,col]
#                digitarray = digitarray2
                digitarray = digitarray.flatten("C")

                outputarraystr = ""
                bool2hex = np.array([2**x for x in range(0,8)],dtype=np.int32)
                if endian == 1:
                    bool2hex = bool2hex[::-1]
                for i in range(0,int(imgsize[0]*imgsize[1]/8)):
                    outputarraystr += "{0:#0{1}x}".format(np.sum(digitarray[8*i:8*(i+1)]*bool2hex),4)
                    if i != int(imgsize[0]*imgsize[1]/8)-1:
                        outputarraystr += ", "

                outputstr = ("d" if os.path.splitext(imgfilename)[0].isnumeric() else "")+os.path.splitext(imgfilename)[0]+" = ["+outputarraystr+"]\r\n"
                file = open(savefilename,"a")
                file.write(outputstr)
                file.close()
