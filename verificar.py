'''
Created on 08/04/2014

@author: jeanmachuca
'''
#Here also you should used verified.py not verificar.py
import FPS, sys
from test_raw import *

if __name__ == '__main__':
    fps = FPS.FPS_GT511C3()
    fps.UseSerialDebug = True
    print Verify(fps,sys.argv[1])
    fps.Close()
    pass
    

