import sys
sys.stdout.reconfigure(encoding='utf-8')

import sympy as sp

x, y = sp.symbols('x y')
f = x * 3 * y + 4 * x * y * 2 + sp.exp(x)
partial_x = sp.diff(f, x)
partial_y = sp.diff(f, y)

print("∂f/∂x:", partial_x)
print("∂f/∂y:", partial_y)
