#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
#print sys.getdefaultencoding()
import time
from glob import glob

import numpy as np
from PIL import Image

import model

import argparse
from argparse import RawTextHelpFormatter

#paths = glob('./test/*.*')
#imgPath = sys.argv[1]
if __name__ == '__main__':
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    description = '''
            A ID Card Chinese and Other Characters recognition program
        '''
    parser = argparse.ArgumentParser(
        description=description, formatter_class=RawTextHelpFormatter)
    parser.add_argument('image',help='image to recognize' )
    options = parser.parse_args()
    if options.image:
        print("! image to reco:", options.image)
    path_image = options.image
    im = Image.open(path_image)
    #im = Image.open("./test/005.jpg")
    img = np.array(im.convert('RGB'))
    t = time.time()


    result, img, angle = model.model(
        img, model='keras11', adjust=True, detectAngle=True)
    #result, img, angle = model.model(
    #    img, model='keras', adjust=True, detectAngle=True)
    print("It takes time:{}s".format(time.time() - t))
    print("---------------------------------------")
    print result
    for key in result:
        print(result[key][1])
        #print(result[key][1])

