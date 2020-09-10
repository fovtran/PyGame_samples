import scipy
import scipy.special
import scipy.integrate
from numpy import exp,cos,sin

# A basic 1D integral:
scipy.integrate.quad(exp, 0, 1)
# (1.7182818284590453, 1.9076760487502457e-14)
scipy.integrate.quad(sin, -0.5, 0.5)
# (0.0, 2.707864644566304e-15)
scipy.integrate.quad(cos, -0.5, 0.5)
# (0.9588510772084061, 1.0645385431034061e-14)

f = lambda x : exp(-x**2)
scipy.integrate.quad(f, 0, 1)
# (0.7468241328124271, 8.291413475940725e-15)

scipy.integrate.quad(lambda x : exp(-x**2), 0, 1)
# (0.7468241328124271, 8.291413475940725e-15)

scipy.integrate.quad(lambda x : exp(-x**2), 0, inf)
# (0.8862269254527579, 7.101318390472462e-09)

scipy.integrate.quad(lambda x : exp(-x**2), -inf, 1)
# (1.6330510582651852, 3.669607414547701e-11)

scipy.integrate.quad(lambda x: scipy.special.jn(1,x),0,5)
# (1.177596771314338, 1.8083362065765924e-14)

#### Integrating Polynomials

p = np.poly1d([2, 5, 1])
p(1), p(2), p(3.5)

P = polyint(p)
q=P(5)-P(1)


#### Basic computations in linear algebra
import scipy.linalg

a = array([[-2, 3], [4, 5]])
scipy.linalg.det(a)

b = scipy.linalg.inv(a)
dot(a,b)

#### Solving systems of linear equations¶
import scipy.linalg

A = array([[2, 4, 6], [1, -3, -9], [8, 5, -7]])
b = array([4, -11, 2])

sol1 = scipy.linalg.solve(A,b)

Ainv = scipy.linalg.inv(A)
sol2 = dot(Ainv, b)
sol1==sol2
