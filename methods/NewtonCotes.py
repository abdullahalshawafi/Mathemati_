
import numpy as np
from sympy import cos, sin, tan, log, acos, asin, atan, cosh, sinh, tanh, acosh, asinh, atanh, cot, acot, coth, acoth,\
    sec, asec, sech, asech, csc, acsc, csch, acsch, sqrt, pi,ln
from scipy.integrate import quad
import sympy  as sp
import numpy as sq

sqr = sq.sqrt
exp = sp.exp
# Team 16 -newton cotes-:
# some instructions :)
# Please, type your function in terms of 'x' if single integration, in terms of 'x' and 'y' if double integration, and interms of 'x' , 'y' and, 'z' if triple integration.
# Be sure that you type the function with lowercase letters only.
# use this symbol ^ to represent the power ex: x^2.
# type " sqr " for square root.
# type " exp " for exponential function.
# for inverse trigonometric functions type 'a' before the function ex: asin ,asec , acsch ..etc
# don't forget to type * between any product terms ( 2*x not 2x ).
# for any root, you can use the same symbol of power ( root 3 => x^(1/3) , root 4 => x^(1/4).. etc).
# thank you!
# -------------------------------------------------- Numerical integration methods ------------------------------------
# first : Trapezoidal method
# single integration:

# in all the functions below :
# a start point of x , b end point of x , n number of intervals
def Trapezoidal_Integ(func, a, b, n):
    h = (b - a) / n
    x = a
    fa = eval(func)
    x = b
    fb = eval(func)
    S = 0.5 * (fa + fb)
    for i in range(1, n):
        x = a + i * h
        S = S + eval(func)
    Integral = h * S
    return Integral


# multiple integration :
# Double integration :
# k start point of y
# l start point of z
def Trapezoidal_Double_Integ_withdiffY(func, a, b, n, k, l):
    h = (b - a) / n
    x = a
    y = k
    z = l
    fa = eval(func)
    x = b
    fb = eval(func)
    S = 0.5 * (fa + fb)
    for i in range(1, n):
        x = a + i * h
        S = S + eval(func)
    Integral = h * S
    return Integral

# c start point of y , d start point of y , m number of intervlas of y

def Trapezoidal_Double_Integ(func, a, b, n, c, d, m):
    k = (d - c) / m
    # get first I
    fa = Trapezoidal_Double_Integ_withdiffY(func, a, b, n, c, 0)

    # Second One
    fb = Trapezoidal_Double_Integ_withdiffY(func, a, b, n, d, 0)

    S = 0.5 * (fa + fb)
    for i in range(1, m):
        y = c + i * k
        S = S + Trapezoidal_Double_Integ_withdiffY(func, a, b, n, y, 0)

    Integral = k * S
    return Integral

# l start point of z
def Trapezoidal_Double_Integ_withdiff_Z(func, a, b, n, c, d, m, l):
    z = l
    k = (d - c) / m
    # get first I
    fa = Trapezoidal_Double_Integ_withdiffY(func, a, b, n, c, l)

    # Second One
    fb = Trapezoidal_Double_Integ_withdiffY(func, a, b, n, d, l)
    S = 0.5 * (fa + fb)
    for i in range(1, m):
        y = c + i * k
        S = S + Trapezoidal_Double_Integ_withdiffY(func, a, b, n, y, l)

    Integral = k * S
    return Integral


# c start point of y , d start point of y , m number of intervlas of y
# e start point of z, f end point of z , g number of intervals of z
def Trapezoidal_Triple_Integ(func, a, b, n, c, d, m, e, f, g):
    l = (f - e) / g
    # get first I

    fa = Trapezoidal_Double_Integ_withdiff_Z(func, a, b, n, c, d, m, e)
    # Second One

    fb = Trapezoidal_Double_Integ_withdiff_Z(func, a, b, n, c, d, m, f)
    S = 0.5 * (fa + fb)
    for i in range(1, g):
        z = e + i * l

    S = S + Trapezoidal_Double_Integ_withdiff_Z(func, a, b, n, c, d, m, z)
    Integral = l * S
    return Integral


# ----------------------------------------------------------------------------------------------------------------------
# second : 1/3 simpsons's method
# single integration
def simpson13(func, a, b, n):
    h = ((b) - (a)) / (n)  # step size
    x = a
    faa = str(func)
    fa = eval(faa)
    x = b
    fbb = str(func)
    fb = eval(fbb)
    const_term = fb + fa
    sum1 = 0
    i = 1
    while i <= (n - 1):
        x = a + h * i
        sum1 += eval(fbb)
        i = i + 2

    sum2 = 0
    j = 2
    while j <= (n - 2):
        x = a + h * j
        sum2 += eval(fbb)
        j = j + 2

    return (h / 3) * (4 * sum1 + 2 * sum2 + const_term)


# multiple integration :
# k start point of y , l start point of z
def simpson13withdiff_Y(func, a, b, n, k, l):
    h = ((b) - (a)) / (n)  # step size
    x = a
    y = k
    z = l
    fa = eval(func)
    x = b
    fb = eval(func)
    const_term = fb + fa
    sum1 = 0
    i = 1
    while i <= (n - 1):
        x = a + h * i
        sum1 += eval(func)
        i = i + 2

    sum2 = 0
    j = 2
    while j <= (n - 2):
        x = a + h * j
        sum2 += eval(func)
        j = j + 2

    return (h / 3) * (4 * sum1 + 2 * sum2 + const_term)

# c start point of y , d start point of y , m number of intervlas of y
def double_integeralsimpson(func, a, b, n, c, d, m):
    k = ((d - c) / m)
    # get first Is
    if n % 2 == 0:
        fa = simpson13withdiff_Y(func, a, b, n, c, 0)
    else:
        fa = simpson_3_over_8_diff_y(func, a, b, n, c, 0)

    # Second One
    if n % 2 == 0:
        fb = simpson13withdiff_Y(func, a, b, n, d, 0)
    else:
        fb = simpson_3_over_8_diff_y(func, a, b, n, d, 0)

    const = fb + fa
    sum1 = 0
    sum2 = 0
    i = 1
    while i <= (m - 1):
        y = c + i * k
        if n % 2 == 0:
            sum1 += simpson13withdiff_Y(func, a, b, n, y, 0)
        elif n % 3 == 0:
            sum1 += simpson_3_over_8_diff_y(func, a, b, n, y, 0)

        i = i + 2

    sum2 = 0
    j = 2
    while j <= (m - 2):
        y = c + k * j
        if n % 2 == 0:
            sum2 += simpson13withdiff_Y(func, a, b, n, y, 0)
        else:
            sum2 += simpson_3_over_8_diff_y(func, a, b, n, y, 0)

        j = j + 2

    return (k / 3) * (4 * sum1 + 2 * sum2 + const)


# l start point of z
# c start point of y , d start point of y , m number of intervlas of y
# a start point of x , b end point of x , n number of intervals
def double_integeralsimpson_diff_z(func, a, b, n, c, d, m, l):
    # k =input("would you like to enter both n&m or one of them only? 1 for n&m,2 for one of them")
    z = l
    k = ((d - c) / m)
    # get first Is
    fa = simpson13withdiff_Y(func, a, b, n, c, l)
    # Second One
    fb = simpson13withdiff_Y(func, a, b, n, d, l)
    const = fb + fa
    sum1 = 0
    i = 1
    while i <= (m - 1):
        y = c + i * k
        sum1 += simpson13withdiff_Y(func, a, b, n, y, l)
        i = i + 2

    sum2 = 0
    j = 2
    while j <= (m - 2):
        y = c + k * j
        sum2 += simpson13withdiff_Y(func, a, b, n, y, l)
        j = j + 2

    return (k / 3) * (4 * sum1 + 2 * sum2 + const)


# e start point of z, f end point of z , g number of intervals of z
# c start point of y , d start point of y , m number of intervlas of y
# a start point of x , b end point of x , n number of intervals
def triple_integeralsimpson(func, a, b, n, c, d, m, e, f, g):
    # k =input("would you like to enter both n&m or one of them only? 1 for n&m,2 for one of them")
    l = ((f - e) / g)
    # get first Is
    if m % 2 == 0:
        fa = double_integeralsimpson_diff_z(func, a, b, n, c, d, m, e)
    else:
        fa = simpson_3_over_8_double_inetegration_diff_z(func, a, b, n, c, d, m, e)

    # Second One
    if m % 2 == 0:
        fb = double_integeralsimpson_diff_z(func, a, b, n, c, d, m, f)
    else:
        fb = simpson_3_over_8_double_inetegration_diff_z(func, a, b, n, c, d, m, f)

    const = fb + fa
    sum1 = 0
    i = 1
    while i <= (g - 1):
        z = e + i * l
        if m % 2 == 0:
            sum1 += double_integeralsimpson_diff_z(func, a, b, n, c, d, m, z)
        else:
            sum1 += simpson_3_over_8_double_inetegration_diff_z(func, a, b, n, c, d, m, z)

        i = i + 2

    sum2 = 0
    j = 2
    while j <= (g - 2):
        z = e + l * j
        if m % 2 == 0:
            sum2 += double_integeralsimpson_diff_z(func, a, b, n, c, d, m, z)
        else:
            sum2 += simpson_3_over_8_double_inetegration_diff_z(func, a, b, n, c, d, m, z)

        j = j + 2

    return (l / 3) * (4 * sum1 + 2 * sum2 + const)


# ----------------------------------------------------------------------------------------------------------------------
# third : 3/8 simpson's method
# single integration
def simpson_3_over_8(func, starting_point, ending_point, number_of_intervals):
    step_size = float((ending_point - starting_point) / number_of_intervals)

    def exp(x):
        return eval(func)

    sum = (exp(starting_point) + exp(ending_point))
    for i in range(1, number_of_intervals):
        if i % 3 == 0:
            sum += 2 * exp(starting_point + step_size * i)
        else:
            sum += 3 * exp(starting_point + step_size * i)
    return (((3 * step_size) / 8) * sum)


# multiple integration
def simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals, d, k):
    step_size = float((ending_point - starting_point) / number_of_intervals)

    def exp(x):
        y = d
        z = k
        return eval(func)

    sum = (exp(starting_point) + exp(ending_point))
    for i in range(1, number_of_intervals):
        if i % 3 == 0:
            sum += 2 * exp(starting_point + step_size * i)
        else:
            sum += 3 * exp(starting_point + step_size * i)
    return (((3 * step_size) / 8) * sum)


def simpson_3_over_8_double_inetegration(func, starting_point, ending_point, number_of_intervals, starting_point2,
                                         ending_point2, number_of_intervals2):
    step_size2 = float((ending_point2 - starting_point2) / number_of_intervals2)

    sum=(simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals,
                             starting_point2, 0) + simpson_3_over_8_diff_y(func, starting_point,
                                                                           ending_point,
                                                                           number_of_intervals,
                                                                           ending_point2, 0))

    for i in range(1, number_of_intervals2):
        if i % 3 == 0:
            sum += 2 * simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals,
                                               starting_point2 + step_size2 * i, 0)

        else:
            sum += 3 * simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals,
                                               starting_point2 + step_size2 * i, 0)
    return (((3 * step_size2) / 8) * sum)


def simpson_3_over_8_double_inetegration_diff_z(func, starting_point, ending_point, number_of_intervals,
                                                starting_point2,
                                                ending_point2, number_of_intervals2, k):
    step_size2 = float((ending_point2 - starting_point2) / number_of_intervals2)

    def exp(y):
        z = k
        return eval(func)

    sum = (simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals,
                                   starting_point2, k) + simpson_3_over_8_diff_y(func, starting_point,
                                                                                 ending_point,
                                                                                 number_of_intervals,
                                                                                 ending_point2, k))
    for i in range(1, number_of_intervals2):
        if i % 3 == 0:
            sum += 2 * simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals,
                                           starting_point2 + step_size2 * i, k)

        else:
            sum += 3 * simpson_3_over_8_diff_y(func, starting_point, ending_point, number_of_intervals,
                                               starting_point2 + step_size2 * i, k)
        return (((3 * step_size2) / 8) * sum)


def simpson_3_over_8_triple_inetegration(func, starting_point, ending_point, number_of_intervals, starting_point2,
                                         ending_point2, number_of_intervals2, starting_point3, ending_point3,
                                         number_of_intervals3):
    step_size3 = float((ending_point3 - starting_point3) / number_of_intervals3)

    if (number_of_intervals2 % 2 != 0):
        sum = (
                simpson_3_over_8_double_inetegration_diff_z(func, starting_point, ending_point, number_of_intervals,
                                                            starting_point2,
                                                            ending_point2, number_of_intervals2,
                                                            starting_point3) + simpson_3_over_8_double_inetegration_diff_z(
            func,
            starting_point, ending_point, number_of_intervals, starting_point2, ending_point2, number_of_intervals2,
            ending_point3))

    else:
        sum = (
                double_integeralsimpson_diff_z(func, starting_point, ending_point, number_of_intervals, starting_point2,
                                               ending_point2, number_of_intervals2,
                                               starting_point3) + double_integeralsimpson_diff_z(func,
                                                                                                 starting_point,
                                                                                                 ending_point,
                                                                                                 number_of_intervals,
                                                                                                 starting_point2,
                                                                                                 ending_point2,
                                                                                                 number_of_intervals2,
                                                                                                 ending_point3))


    for i in range(1, number_of_intervals3):
        if i % 3 == 0:
            if number_of_intervals2 % 3 == 0:
                sum += 2 * simpson_3_over_8_double_inetegration_diff_z(func, starting_point, ending_point,
                                                                       number_of_intervals,
                                                                       starting_point2, ending_point2,
                                                                       number_of_intervals2,
                                                                       starting_point3 +step_size3 * i)
        else:
            if number_of_intervals2 % 3 == 0:
                sum += 3 * simpson_3_over_8_double_inetegration_diff_z(func, starting_point, ending_point,
                                                                       number_of_intervals,
                                                                       starting_point2, ending_point2,
                                                                       number_of_intervals2,
                                                                       starting_point3 +step_size3 * i)
        return (((3 * step_size3) / 8) * sum)


#------------------------------------------ Simpson mixed rule ----------------------------------------------------------
# SINGLE :
def single_mixe_rule ( func,a,b,n):
    if ( n % 2 == 0):
        return simpson13(func,a,b,n),simp_1_over_3_error(func,a,b,n)
    elif(n == 3):
        return simpson_3_over_8(func,a,b,n),simp_3_over_8_error(func, a, b, n)
    else:
        h = (b - a) / n
        n1= n-3
        b1= a+(n1)*h
        I1= simpson13(func,a,b1,n1)
        print(I1)
        I2= simpson_3_over_8(func,b1,b,3)
        print(I2)
        return I1+I2, max(simp_1_over_3_error(func,a,b1,n1),simp_3_over_8_error(func,b1,b,3))


# DOUBLE :
def double_mixed_rule ( func,ax,bx,nx,ay,by,ny):
    if (nx == 3 | ny == 3 ):
        return simpson_3_over_8_double_inetegration(func,ax,bx,nx,ay,by,ny)
    else:
        hx = (bx - ax) / nx
        hy = (by - ay) / ny
        nx1= nx-3
        ny1= ny-3
        bx1 =ax+ nx1*hx
        by1 = ay+ ny1* hy
        print(bx1 ," ", by1)
        I1= double_integeralsimpson(func ,ax,bx1,nx1 ,ay,by1 ,ny1)
        I2= simpson_3_over_8_double_inetegration( func ,bx1,bx,3,by1,by,3)
        print( I1," ",I2)
        return I1+I2


# TRIPLE :
def triple_mixed_rule( func ,ax,bx,nx ,ay,by ,ny,az,bz,nz):
    if ( nx== 3 | ny == 3 | nz==3):
        return simpson_3_over_8_triple_inetegration(func ,ax,bx,nx ,ay,by ,ny,az,bz,nz)
    else:
        nx1 = nx - 3
        ny1 = ny - 3
        nz1 = nz- 3
        hx = (bx - ax) / nx
        hy = (by - ay) / ny
        hz = (bz-az)/ nz
        bx1 = ax+ (nx1) * hx
        by1 = ay+ (ny1) * hy
        bz1 = az+ (nz1)* hz
        I1= triple_integeralsimpson(func ,ax,bx1,nx1 ,ay,by1 ,ny1, az,bz1,nz1)
        I2= simpson_3_over_8_triple_inetegration(func ,bx1,bx,3 ,by1,by ,3, bz1,bz,3)
        return I1+I2


# ----------------------------------------------- error evaluation -----------------------------------------------------

def Trapezoidal_error(func, a, b, n):
    x = sp.Symbol('x')
    equation = eval(func)
    y11 = equation.diff(x)  # first dervative
    y1 = str(y11)
    x = a
    fa = eval(y1)
    x = b
    fb = eval(y1)
    const_term = ((b - a) ** 2) / (12 * (n ** 2))
    return abs(const_term * (fb - fa))


def simp_1_over_3_error(func, a, b, n):
    x = sp.Symbol('x')
    equation = eval(func)
    y1 = equation.diff(x)  # first dervative
    y2 = y1.diff(x)  # second dervative
    y33 = y2.diff(x)  # third dervative
    y3 = str(y33)  # convert it to string
    x = a
    fa = eval(y3)
    x = b
    fb = eval(y3)
    const_term = ((b - a) ** 4) / (180 * (n ** 4))
    return abs(const_term * (fb - fa))

def simp_3_over_8_error(func, a, b, n):
    x = sp.Symbol('x')
    equation = eval(func)
    y1 = equation.diff(x)  # first dervative
    y2 = y1.diff(x)  # second dervative
    y33 = y2.diff(x)  # third dervative
    y3 = str(y33)  # convert it to string
    x = a
    fa = eval(y3)
    x = b
    fb = eval(y3)
    const_term = ((b - a) ** 4) / (80 * (n ** 4))
    return abs(const_term * (fb - fa))
"""
# ---------------------------------------------- Code Test ------------------------------------------------------------
type = int(input(
    'Please, choose the type of your integral problem (1 for single integertion, 2 for double integertion, 3 for triple integertion) : '))
#------------------------------------------------------- single -----------------------------
if (type == 1):
    func = input('Please, enter the function: ')
    func = func.replace("^", "**");
    a = (input("Please, enter the starting point: "))
    if (a == 'pi'):
        a = '3.14159265359'
    starting_point = float(a)
    b = (input("Please, enter the ending point: "))
    if (b == 'pi'):
        b = '3.14159265359'
    ending_point = float(b)
    option = int(input(
        " If you like to enter the number of intervals please enter 1 if you like to enter step size enter 2 and if you din't like both enter 3 :  "))
    number_of_intervals = 0
    if (option == 1):
        number_of_intervals = int(input("Please, enter the number of intervals: "))
    elif (option == 2):
        step_size = float(input('step size: '))
        number_of_intervals = round((ending_point - starting_point) / step_size)
    elif(option ==3 ):
        number_of_intervals=100
    else:
        print( "wrong choice! Rerun,Please " )
# simpson 's 1/3
    if (number_of_intervals % 2 == 0):
        print(" Number of intervals is even, so Simpson's 1/3 Rule is applied.. ")
        print("Is = ", simpson13(func, starting_point, ending_point, round(number_of_intervals)))
        I1=simp_1_over_3_error(func, starting_point, ending_point, round(number_of_intervals));
        I2=simp_3_over_8_error(func, starting_point, ending_point, round(number_of_intervals));
        if(I1<I2):
            print("error = ",I1 );
        else:
            print("error = ",I2);

# mixed rule
    else:
        print(" Number of intervals is odd, so Simpson's mixed Rule is applied.. ")
        print("Is = ", single_mixe_rule(func, starting_point, ending_point, round(number_of_intervals)))
# trapezoidal
    print("The same integral with Trapezoidal Rule, notice the difference: ")
    print("I trap = ", Trapezoidal_Integ(func, starting_point, ending_point, round(number_of_intervals)))
    print("error = ", Trapezoidal_error(func, starting_point, ending_point, round(number_of_intervals)))
# --------------------------------- double -------------------------------------------------------------------------------------
if (type == 2):
    func = input('Please, enter the function: ')
    func = func.replace("^", "**");
    a = (input("Please, enter the starting point of x: "))
    if (a == 'pi'):
        a = '3.14159265359'
    starting_point = float(a)
    b = (input("Please, enter the ending point of x: "))
    if (b == 'pi'):
        b = '3.14159265359'
    ending_point = float(b)
    number_of_intervals = 0
    option = int(input(
        " If you like to enter the number of intervals please enter 1, if you like to enter step size enter 2 and if you din't like both enter 3 :  "))
    if (option == 1):
        number_of_intervals = int(input("Please, enter the number of intervals of x: "))
    elif (option == 2):
        step_size = float(input('step size of x: '))
        number_of_intervals = (ending_point - starting_point) / step_size
    elif (option == 3):
        number_of_intervals = 100
    else:
        print( "wrong choice! Rerun,Please " )
    a = (input("Please, enter the starting point of y: "))
    if (a == 'pi'):
        a = '3.14159265359'
    starting_point2 = float(a)
    b = (input("Please, enter the ending point of y: "))
    if (b == 'pi'):
        b = '3.14159265359'

    ending_point2 = float(b)
    number_of_intervals2 = 0
    option = int(input(
        " If you like to enter the number of intervals please enter 1, if you like to enter step size enter 2 and if you din't like both enter 3 :  "))
    if (option == 1):
        number_of_intervals2 = int(input("Please, enter the number of intervals of y: "))
    elif (option == 2):
        step_size2 = float(input('step size of y: '))
        number_of_intervals2 = (ending_point2 - starting_point2) / step_size2
    elif (option == 3):
        number_of_intervals2 = 100
    else:
        print( "wrong choice! Rerun,Please " )
    if ((round(number_of_intervals2)) % 2 == 0):
        print(" Number of intervals is even, so Simpson's 1/3 Rule is applied.. ")
        print("Is = ",
              double_integeralsimpson(func, starting_point, ending_point, round(number_of_intervals), starting_point2,
                                      ending_point2, round(number_of_intervals2)))
    else:
        print(" Number of intervals is odd, so Simpson's mixed Rule is applied.. ")
        print("Is = ",
              double_mixed_rule(func, starting_point, ending_point, round(number_of_intervals),
                                                   starting_point2,
                                                   ending_point2, round(number_of_intervals2)))
    print("The same integral with Trapezoidal Rule, notice the difference: ")

    print("Itrap = ",
              Trapezoidal_Double_Integ(func, starting_point, ending_point, round(number_of_intervals), starting_point2,
                                       ending_point2, round(number_of_intervals2)))
    print( simpson_3_over_8_double_inetegration(func, starting_point, ending_point, round(number_of_intervals), starting_point2,
                                       ending_point2, round(number_of_intervals2)))
 # ----------------------------------------------------------- triple ------------------------------------------------------
if (type == 3):
    func = input('Please, enter the function: ')
    func = func.replace("^", "**");
    a = (input("Please, enter the starting point of x: "))
    if (a == 'pi'):
        a = '3.14159265359'
    starting_point = float(a)
    b = (input("Please, enter the ending point of x: "))
    if (b == 'pi'):
        b = '3.14159265359'
    ending_point = float(b)
    number_of_intervals = 0
    option = int(input(
        " If you like to enter the number of intervals please enter 1 and if you like to enter step size enter 2 :  "))
    if (option == 1):
        number_of_intervals = int(input("Please, enter the number of intervals of x: "))
    elif (option == 2):
        step_size = float(input('step size of x: '))
        number_of_intervals = round((ending_point - starting_point) / step_size)
    elif (option == 3):
        number_of_intervals2 = 100
    else:
        print( "wrong choice! Rerun,Please " )
    a = (input("Please, enter the starting point of y: "))
    if (a == 'pi'):
        a = '3.14159265359'
    starting_point2 = float(a)
    b = (input("Please, enter the ending point of y: "))
    if (b == 'pi'):
        b = '3.14159265359'
    ending_point2 = float(b)
    number_of_intervals2 = 0
    option = int(input(
        " If you like to enter the number of intervals please enter 1 and if you like to enter step size enter 2 :  "))
    if (option == 1):
        number_of_intervals2 = int(input("Please, enter the number of intervals of y: "))
    elif (option == 2):
        step_size2 = float(input('step size of y: '))
        number_of_intervals2 = round((ending_point2 - starting_point2) / step_size2)
    elif (option == 3):
        number_of_intervals2 = 100
    else:
        print( "wrong choice! Rerun,Please " )
    a = (input("Please, enter the starting point of z: "))
    if (a == 'pi'):
        a = '3.14159265359'
    starting_point3 = float(a)
    b = (input("Please, enter the ending point of z: "))
    if (b == 'pi'):
        b = '3.14159265359'
    ending_point3 = float(b)
    number_of_intervals3 = 0
    option = int(input(
        " If you like to enter the number of intervals please enter 1 and if you like to enter step size enter 2 :  "))
    if (option == 1):
        number_of_intervals3 = int(input("Please, enter the number of intervals of z: "))
    elif (option == 2):
        step_size3 = float(input('step size of z: '))
        number_of_intervals3 = round((ending_point3 - starting_point3) / step_size3)
    elif (option == 3):
        number_of_intervals2 = 100
    else:
        print( "wrong choice! Rerun,Please " )
    if (number_of_intervals3 % 2 == 0):
        print(" Number of intervals is even, So Simpson's 1/3 Rule is applied.. ")
        print("Is = ", triple_integeralsimpson(func, starting_point, ending_point, number_of_intervals, starting_point2,
                                               ending_point2, number_of_intervals2, starting_point3, ending_point3,
                                               number_of_intervals3))
    else:
        print(" Number of intervals is odd, So Simpson's mixed Rule is applied.. ")
        print("Is = ", triple_mixed_rule(func, starting_point, ending_point, number_of_intervals,
                                                            starting_point2, ending_point2, number_of_intervals2,
                                                            starting_point3, ending_point3, number_of_intervals3))

    print("The same integral with Trapezoidal Rule, notice the difference: ")
    print("Itrap = ", Trapezoidal_Triple_Integ(func, starting_point, ending_point, number_of_intervals,
                                               starting_point2, ending_point2, number_of_intervals2,
                                               starting_point3, ending_point3, number_of_intervals3))

# تم بحمدالله
"""
