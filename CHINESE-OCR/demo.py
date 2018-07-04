
import time
from glob import glob

import numpy as np
from PIL import Image
import sys
import model
# ces
#reload(sys)
#sys.setdefaultencoding('utf8')
paths = glob('./test/*.*')
#imgPath = sys.argv[1]
if __name__ == '__main__':
    #print imgPath
    #im = Image.open(imgPath)
    im = Image.open("./test/005.jpg")
    img = np.array(im.convert('RGB'))
    t = time.time()


    result, img, angle = model.model(
        img, model='keras11', adjust=True, detectAngle=True)
    #result, img, angle = model.model(
    #    img, model='keras', adjust=True, detectAngle=True)
    print("It takes time:{}s".format(time.time() - t))
    print("---------------------------------------")
    for key in result:
        print(result[key][1])
