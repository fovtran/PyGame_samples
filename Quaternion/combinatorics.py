# These commands were executed:
from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

from sympy.combinatorics.permutations import Permutation
from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.combinatorics.tensor_can import double_coset_can_rep, get_transversals
gens = [Permutation(x) for x in [[2,1,0,3,4,5,7,6], [4,1,2,3,0,5,7,6]]]
base = [0, 2]
g = Permutation([4,2,0,1,3,5,6,7])
transversals = get_transversals(base, gens)
double_coset_can_rep([list(range(6))], [0], base, gens, transversals, g)
# [0,1,2,3,4,5,7,6]
