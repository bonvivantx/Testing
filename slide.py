#!/usr/bin/env python2

import math, operator
from PIL import Image
import sys
import os
import glob
import subprocess
import shutil

def compare(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,
                           map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

if __name__=='__main__':
    if len(sys.argv) < 3:
        sys.exit("Need video file and output dir as parameter")
    if not os.path.exists("decomp"):
        os.mkdir("decomp")
    else:
        sys.exit("decomp already exists, exit")
    if not os.path.exists(sys.argv[2]):
        os.mkdir(sys.argv[2])

    cmd = ["ffmpeg", "-i", sys.argv[1], "-vf", "select='eq(pict_type,I)'", "-vsync", "0", "-f", "image2", "decomp/%09d.png"]

    print "Running ffmpeg: " + " ".join(cmd)

    subprocess.call(cmd)

    print "Done, now eliminating duplicate images and moving unique ones to output folder..."

    filelist = glob.glob(os.path.join("decomp", '*.png'))
    filelist.sort()
    for ii in range(0, len(filelist)):
        if ii < len(filelist)-1:
            if compare(filelist[ii], filelist[ii+1]) == 0:
                print 'Found similar images: ' + filelist[ii] + " and " + filelist[ii+1]
            else:
                print 'Found unique image: ' + filelist[ii]
                head, tail = os.path.split(filelist[ii])
                shutil.copyfile(filelist[ii], sys.argv[2] + os.path.sep + tail)
        else:
            shutil.copyfile(filelist[ii], sys.argv[2] + os.path.sep + tail)
    shutil.rmtree("decomp")
