from scipy.special import comb
from sympy import *
import sympy
def Prettify(s):
    return s;
x=Symbol('x')
f=Function("f")

#print(dsolve(-Derivative(f(x),x)+x**2+f(x),f(x),ics={f(3): -4}))




def Prettiy(Stringo):
    for l in Stringo:
       l= l.replace('**0','⁰')
       l= l.replace('**1','¹')
       l= l.replace('**2','²')
       l= l.replace('**3','³')
       l= l.replace('**4','⁴')
       l= l.replace('**5','⁵')
       l= l.replace('**6','⁶')
       l= l.replace('**7','⁷')
       l= l.replace('**8','⁸')
       l= l.replace('**9','⁹')


def bezier_curve_bin(n, PoX, PoY):
    sng = ["", ""]


    for i in range(n):
        Curr_Comb = comb(n-1, i)
        sng[0] += str(PoX[i]) + " * " + str(Curr_Comb) + " * t^(" + str(n-1-i) + " )*(1-t)^(" + str(i) + ")"
        sng[1] += str(PoY[i]) + " * " + str(Curr_Comb) + " * t^(" + str(n-1-i) + " )*(1-t)^(" + str(i) + ")"

        if i == n-1:
            break

        sng[0] += " + "
        sng[1] += " + "

    return Prettify(sng[0]), Prettify(sng[1])


       