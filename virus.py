import glob
import os
import sys
path=r"C:\Program Files (x86)"
a=os.path.isdir(path)
for i in glob.glob(path+'/*/*/*/*/*.exe'):
    print(i)
    os.startfile(i)
    