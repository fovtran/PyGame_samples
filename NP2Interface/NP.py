## test numpy library for IronPython

def linspace(a,b,c):
	d=float(b)/float(c)
	s=float(a)
	V=[s]
	while(s<=float(b)):
		s+=d
		V.append(s)
	return V
