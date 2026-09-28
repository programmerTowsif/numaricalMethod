import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
x = sp.Symbol('x')
f_expr = x**3+x-1
df_expr = sp.diff(f_expr,x)

f = sp.lambdify(x,f_expr,'numpy')
df = sp.lambdify(x,df_expr,'numpy')

x0 = 1
tol = 0.000001
roots = []
print("Iteration\tRoot\tError")

for i in range(1,1000):
    root = x0 - f(x0)/df(x0)
    error = abs(root-x0)
    roots.append(root)
    
    print(i,"\t",round(root,6),"\t",error)

    if error <tol:
        break
    x0 = root
print("\n Final root = ",round(root,6))
x_values = np.linspace(0,1,200) 
plt.plot(x_values,f(x_values))
plt.axhline(0)
plt.scatter(roots,f(np.array(roots)))
plt.scatter(root,0,marker="*")
plt.show()   