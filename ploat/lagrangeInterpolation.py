# import numpy as np
# import matplotlib.pyplot as plt
# def lagrange(x_data, y_data, x):

#     result = 0

#     for i in range(len(x_data)):

#         term = y_data[i]

#         for j in range(len(x_data)):

#             if i != j:
#                 term *= ((x - x_data[j]) /
#                          (x_data[i] - x_data[j]))

#         result += term

#     return result
 

# x_data = [0, 2, 3]
# y_data = [1, 2, 4]

# # Points for drawing the curve
# x_values = np.linspace(0, 3, 100)

# # Evaluate Lagrange polynomial
# y_values = [
#     lagrange(x_data, y_data, x)
#     for x in x_values
# ]

# # Plot interpolation polynomial
# plt.plot(x_values, y_values,
#          label="Lagrange Polynomial")

# # Plot original data points
# plt.scatter(x_data, y_data,
#             label="Data Points")

# plt.xlabel("x")
# plt.ylabel("P(x)")
# plt.title("Lagrange Interpolation")

# plt.grid()
# plt.legend()
# plt.show()


import numpy as np
x=np.array([-1,2,3,5])
y=np.array([0,1,1,2])
n=len(x)
def lagrange(x_value):
    p=0
    for i in range(n):
        term=y[i]
        for j in range(n):
            if i!=j:
                term=term*(x_value-x[j])/(x[i]-x[j])
        p=p+term
    return p
print("Lagrange Interpolation Results:")
print("x\t\tGiven y\t\tP(x)")
for i in range(n):
    print(x[i],"\t\t",y[i],"\t\t",lagrange(x[i]))