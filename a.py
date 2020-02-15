import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
I, B = np.loadtxt('a.txt', unpack=True,delimiter=',')

def f(x,a, b):
    return a*x +b
Werte, Fehler = curve_fit(f, I, B)
print(Werte)
print(np.sqrt(np.diag(Fehler)))

x_new = np.linspace(I[0], I[-1], 500)

I1 = np.array([4.0,2.0,5.2])
B1 = Werte[0]*I1 + Werte[1]
print(B1)



plt.figure(1)
plt.plot(I,B,'o', label='Messwerte')
plt.plot(x_new,f(x_new,*Werte),'-', label='Lineare Regression')
plt.xlabel(r'$I/\mathrm{A}$')
plt.ylabel(r'$B/\mathrm{T}$')
plt.grid()
plt.legend()




plt.savefig('a.pdf')
print ('Fertig')
