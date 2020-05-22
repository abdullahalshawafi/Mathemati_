from scipy.special import comb

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

    return sng[0], sng[1]