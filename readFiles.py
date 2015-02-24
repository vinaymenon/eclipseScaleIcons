import sys
import os
from PIL import Image

# Workaround solution for eclipse on QHD monitors. Resize the icons
# Usage : readFiles.py <eclipseRootDir>

if len(sys.argv) < 2:
    print "Argument : Root eclipse path required"
    sys.exit(-1)
image_files = []
for root, dirs, files in os.walk(sys.argv[1]):
    # print "Current Dir : " + root
    for curFile in files:
        try:
            with Image.open(os.path.join(root, curFile)) as im:
                image_files.append(curFile)
                print(curFile, im.format, "%dx%d" % im.size, im.mode)
                newSize = [x*2 for x in im.size]
                im = im.resize(newSize, Image.ANTIALIAS)
                im.save(os.path.join(root, curFile))
                print(curFile, im.format, "%dx%d" % im.size, im.mode)
        except IOError:
            pass
print image_files
with open(os.path.join(sys.argv[1], "listFiles.txt"), 'w') as theFile:
    for fileName in image_files:
        print>>theFile, fileName