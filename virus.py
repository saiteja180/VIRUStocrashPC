import glob
import platform
import os
if(platform.system()=='Windows'):
    if(os.path.exists(r"C:\Program Files (x86)")):
        path=r"C:\Program Files (x86)"
    else:
        path=r"C:\Program Files (x64)"
    for i in glob.glob(path+'/*/*/*/*/*.exe'):
        os.startfile(i)
elif(platform.system()=='Linux'):
    if(os.path.exists('/root')):
        for i in glob.glob(path+'/*/*/*.deb'):
            os.startfile(i)
    