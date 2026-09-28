import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')
f_expr = x**3+x-1

f = sp.lambdify(x,f_expr,'numpy')



a = 0
b = 1
tol = 0.0000001
old_root = 0
roots = []

print("iteration\tRoot\tError")

for i in range(1,100):
    root = (a*f(b)-b*f(a))/(f(b)-f(a))
    error = abs(old_root-root)
    roots.append(root)
    print(i,"\t\t",round(root,6),"\t",round(error,6))

    if error < tol:
        break

    if f(a)*f(root)<0:
        b = root
    else:
        a = root
    old_root = root

print("\nFinal root = ",round(root,6))

x_values = np.linspace(0,1,200)
plt.plot(x_values,f(x_values))
plt.axhline(0)
plt.scatter(roots,f(np.array(roots)),label="ROOTS")
plt.scatter(root,0,marker="*")
plt.grid()
plt.show()