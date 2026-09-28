# import numpy as np
# import sympy as sp
# import matplotlib.pyplot as plt

# x = sp.symbols('x')
# f_ex = x**3+x-1
# f = sp.lambdify(x,f_ex,'numpy')
# a=0
# b=1
# roots=[]
# old_root =0
# tol=0.0000000001
# print("it\troot\error")
# for i in range(1,100):
#     root = (a+b)/2
#     error = abs(old_root-root)
#     roots.append(root)
#     print(i,"\t",root,"\t",error)

#     if error<tol:
#         break
#     if f(a)*f(root)<0:
#         b = root
#     else:
#         a = root
#     old_root = root

# print(old_root)
# x_value = np.linspace(0,1,200)
# plt.plot(x_value,f(x_value))
# plt.axhline(0)
# plt.scatter(roots,f(np.array(roots)))
# plt.scatter(root,0,marker="*")
# plt.show()
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
x = sp.Symbol('x')
f_ex = x**3+x-5
f =sp.lambdify(x,f_ex,'numpy')
df_ex = sp.diff(f_ex,x)
df = sp.lambdify(df_ex,x,'numpy')

x0 = 1
tol = 0.00001
roots =[]
 


for i in range (1,100):
    root = x0-f(x0)/df(x0)
    error = abs(root - x0)
    roots.append(root)
    print(i,root,error)
    if error <tol:
        break
    x0 = root
    