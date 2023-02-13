import numpy as np
import matplotlib.pyplot as plt


v1 = int(input("Enter v1: "))
v2 = int(input("Enter v2: "))

v = np.array([v1, v2])
deg = int(input("Enter the angle in degrees: "))
a = np.deg2rad(deg)

A = np.array([[np.cos(a), -np.sin(a)],
             [np.sin(a), np.cos(a)]])

b = np.dot(A, v)

plt.arrow(0, 0, v[0], v[1], head_width=0.05,
          head_length=0.1, fc='r', ec='r', label='v')
plt.arrow(0, 0, b[0], b[1], head_width=0.05,
          head_length=0.1, fc='b', ec='b', label='A(v)')
plt.axis('equal')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.text(0.5, 0.5, r'$\theta$={:.2f} degrees'.format(deg), fontsize=20)

plt.legend()
plt.show()
