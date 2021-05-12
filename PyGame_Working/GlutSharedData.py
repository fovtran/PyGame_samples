from System import UInt32, IntPtr
from ctypes import *
from math import cos,sin,pi
from NP2Interface.NP import *
from GlutControls import *

class window():
	screenX = 0
	screenY = 0

win = window()

class controls():
	specialKey=-1
	kbdKey=-1
	mouseButon=-1
	mouseButtonState=-1
	currentCursorX=0
	currentCursorY=0
	currentCursorZ=0
	lastCursorX=0
	lastCursorY=0
	lastCursorZ=0

ctrl = controls()

class gimbal():
	centerX = win.screenX/2
	centerY = win.screenY/2
	offsetX = 1.0-(centerX/(ctrl.currentCursorX+1))
	offsetY = 1.25

class camera():
	g = gimbal()
	eyeX = 0
	eyeY = g.offsetY
	eyeZ = -5
	centerX = 0
	centerY = 0
	centerZ = 0
