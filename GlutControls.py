from System import UInt32, IntPtr
from ctypes import *

from math import cos,sin,pi
from NP import *
from GlutSharedData import *

def on_up(key,x,y):
	ctrl.kbdKey = key
	ctrl.lastCursorX = ctrl.currentCursorX
	ctrl.lastCursorY = ctrl.currentCursorY
	ctrl.currentCursorX = x
	ctrl.currentCursorY = y

def mouse_up(but,state,x,y):
	ctrl.mouseButtonState=state
	ctrl.mouseButton=but
	ctrl.lastCursorX = ctrl.currentCursorX
	ctrl.lastCursorY = ctrl.currentCursorY
	ctrl.currentCursorX = x
	ctrl.currentCursorY = y
	print(x,y)

def special_up(key,x,y):
	ctrl.specialKey=key
	ctrl.lastCursorX = ctrl.currentCursorX
	ctrl.lastCursorY = ctrl.currentCursorY
	ctrl.currentCursorX = x
	ctrl.currentCursorY = y
