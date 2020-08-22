import cmath as mth
import numpy as np
import scipy as sc
import time
np.seterr(all='print')

# Angle functions in degrees
nptypes = np.float64

angle_a = lambda _b, _c: 180 - _c - _b
angle_b = lambda _a,_c: 180 - _a - _c
angle_c = lambda _a,_b: 180 - _a - _b

# degrees from segment + opposite angles
angle_a_deg = lambda _C, _alpha_rad, _gamma_rad: _C * np.sin(_alpha_rad) / np.sin(_gamma_rad)
angle_b_deg = lambda _C, _beta_rad, _gamma_rad: _C * np.sin(_beta_rad) / np.sin(_gamma_rad)
angle_c_deg = lambda _A, _alpha_rad, _gamma_rad: _A * np.sin(_gamma_rad) / np.sin(_alpha_rad)

# radian from angles ABC
angle_alpha_rad = lambda _A,_B,_C: np.arccos( (_B**2 + _C**2 - _A**2) / (2*_B*_C), dtype=nptypes)  # calcular angula A from B and C
angle_beta_rad = lambda _A,_B,_C: np.arccos( (_A**2 + _C**2 - _B**2) / (2*_A*_C), dtype=nptypes)   # calcular angula B from A and C
angle_gamma_rad = lambda _A,_B,_C: np.arccos( (_A**2 + _B**2 - _C**2) / (2*_A*_B), dtype=nptypes)  # calcular gamma = np.pi - alpha - beta

#Normal
A_angle = lambda B,C: angle_a(B,C)
B_angle = lambda A,C: angle_b(A,C)
C_angle = lambda A,B: angle_c(A,B)
A_rad = lambda A,B,C: angle_alpha_rad(A,B,C)
B_rad = lambda A,B,C: angle_beta_rad(A,B,C)
C_rad = lambda A,B,C: angle_gamma_rad(A,B,C)
A_deg = lambda _C, _alpha, _gamma: angle_a_deg(_C,_alpha,_gamma)
B_deg = lambda _C, _beta, _gamma: angle_b_deg(_C,_beta,_gamma)
C_deg = lambda _A, _alpha, _gamma: angle_c_deg(_A,_alpha, _gamma)

def compute_angles(alist):
	for a in alist:
		A = np.float64(a)
		B = np.float64(90)
		C = np.float64(angle_c(A,B))
		print(A,B,C, A+B+C==180)
		arad = np.radians(A)
		brad = np.radians(B)
		crad = np.radians(C)
		print(arad,brad,crad)
		print(arad+brad+crad==np.pi)
		adeg = np.degrees(arad)
		bdeg = np.degrees(brad)
		cdeg = np.degrees(crad)
		print(adeg+bdeg+cdeg==180)
		print()

def compute_sides(x,y):
	hyp = np.hypot(x,y)
	A = y
	B = x
	C = hyp
	# np.sin(A)/a == np.sin(B)/b == np.sin(C)/c  <-- Ley de los senos
	arad = angle_alpha_rad(A,B,C)
	brad = np.radians(90) #angle_beta_rad(A,B,C)
	crad = angle_gamma_rad(A,B,C)
	adeg = angle_a_deg(C,arad, crad)
	bdeg = angle_b_deg(C,brad, crad)
	cdeg = angle_c_deg(A,arad, crad)
	print(adeg,bdeg,cdeg)
	print(adeg**2+bdeg**2==cdeg**2)

LP = np.random.randint(1,89,4)
compute_angles(LP)
compute_sides(5,5)
compute_sides(75,35)