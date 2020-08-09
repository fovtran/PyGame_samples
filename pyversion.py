import sys

a = sys.version.split()

if a[0].startswith('3'):
	print('Python Interpreter detected')
if a[0].startswith('2'):
	print('IronPython Interpreter detected')
