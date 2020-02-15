import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphikbitte')
print('Steigung','Y-Achsenabschnitt')
dels, ds = np.loadtxt('a2.txt', unpack=True,delimiter=',')
 
dell = 4.89*10**(-11)

dl = 1/2*ds/dels*dell
print(dl)



y=np.mean(dl)
print(y)

#Fehler des Mittelwerts
u = np.std(dl, ddof=1) / np.sqrt(len(dl))
print(u)