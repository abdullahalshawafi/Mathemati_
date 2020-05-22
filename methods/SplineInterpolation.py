import numpy as np

def get_interval_list (n , Po):
    sngP = []
    for i in range(n-1):
        sngP.append('{' + Po[i][0].__str__() + '<=x<' + Po[i+1][0].__str__() + '}')

    return sngP

def linear_spline(n, Po):
    Po.sort()
    sngL = []
    mat = np.zeros((2*n-2, 2*n-2))
    vec = np.zeros((2*n-2))
    ans = np.zeros((2*n-2))

    mat[2 * (n - 1) - 2][0] = Po[0][0]
    mat[2 * (n - 1) - 2][1] = 1
    vec[2 * (n - 1) - 2] = Po[0][1]

    mat[2 * (n - 1) - 1][2 * (n - 1) - 2] = Po[n-1][0]
    mat[2 * (n - 1) - 1][2 * (n - 1) - 1] = 1
    vec[2 * (n - 1) - 1] = Po[n-1][1]

    j = 1
    for i in range(0, 2*(n-1)-2, 2):
        mat[i][(j - 1) * 2] = mat[i + 1][j * 2] = Po[j][0]
        mat[i][(j - 1) * 2 + 1] = mat[i + 1][j * 2 + 1] = 1
        vec[i] = vec[i + 1] = Po[j][1]
        j = j + 1
    ans = np.dot(np.linalg.inv(mat), vec)

    Eq = np.zeros((n-1, 2))
    for j in range(n - 1):
        Eq[j] = [ans[j * 2], ans[j * 2 + 1]]
        sngL.append("%.5f"%(Eq[j][0]) + "*x + " + "%.5f"%(Eq[j][1]))

    return sngL


def quad_spline(n, Po):
    Po.sort()
    sngQ = []
    mat = np.zeros((3*n-3, 3*n-3))
    vec = np.zeros((3*n-3))
    ans = np.zeros((3*n-3))

    mat[0][0] = 1

    for i in range(1, n-1, 1):
        mat[i] [(i - 1) * 3] = 2 * Po[i][0]
        mat[i] [(i - 1) * 3 + 1] = 1
        mat[i] [i * 3] = -2 * Po[i][0]
        mat[i] [i * 3 + 1] = -1

    mat[3 * (n - 1) - 2][0] = Po[0][0] * Po[0][0]
    mat[3 * (n - 1) - 2][1] = Po[0][0]
    mat[3 * (n - 1) - 2][2] = 1
    vec[3 * (n - 1) - 2] = Po[0][1]

    mat[3 * (n - 1) - 1][3 * (n - 1) - 3] = Po[n-1][0] * Po[n-1][0]
    mat[3 * (n - 1) - 1][3 * (n - 1) - 2] = Po[n-1][0]
    mat[3 * (n - 1) - 1][3 * (n - 1) - 1] = 1
    vec[3 * (n - 1) - 1] = Po[n-1][1]

    j = 1
    for i in range(n-1, 3*(n-1)-2, 2):
        mat[i][(j - 1) * 3] = mat[i + 1][j * 3] = Po[j][0] * Po[j][0]
        mat[i][(j - 1) * 3 + 1] = mat[i + 1][j * 3 + 1] = Po[j][0]
        mat[i][(j - 1) * 3 + 2] = mat[i + 1][j * 3 + 2] = 1
        vec[i] = vec[i + 1] = Po[j][1]
        j = j + 1

    ans = np.dot(np.linalg.inv(mat), vec)

    Eq = np.zeros((n-1, 3))

    for j in range(n - 1):
        Eq[j] = [ans[j * 3], ans[j * 3 + 1], ans[j * 3 + 2]]
        sngQ.append("%.5f"%(Eq[j][0]) + "*x^2 + " + "%.5f"%(Eq[j][1]) + "*x + " + "%.5f"%(Eq[j][2]))

    return sngQ


def cubic_spline(n, Po):
    Po.sort()
    sngC = []
    if n == 2:
        X = quad_spline(n, Po)
        Eq = [[0, X[0][0], X[0][1], X[0][2]]]
        return Eq

    mat = np.zeros((4*n-4, 4*n-4))
    vec = np.zeros((4*n-4))
    ans = np.zeros((4*n-4))

    mat[0][0] = 1
    mat[1][4*(n-1)-4] = 1

    j = 1
    for i in range(2, n, 1):
        mat[i][(j - 1) * 4] = 3 * Po[j][0] * Po[j][0]
        mat[i][(j - 1) * 4 + 1] = 2 * Po[j][0]
        mat[i][(j - 1) * 4 + 2] = 1
        mat[i][j * 4] = -3 * Po[j][0] * Po[j][0]
        mat[i][j * 4 + 1] = -2 * Po[j][0]
        mat[i][j * 4 + 2] = -1
        j = j + 1

    j = 1
    for i in range(n, 2 * (n - 1), 1):
        mat[i][(j - 1) * 4] = 3 * Po[j][0]
        mat[i][(j - 1) * 4 + 1] = 1
        mat[i][j * 4] = -3 * Po[j][0]
        mat[i][j * 4 + 1] = -1
        j = j + 1

    mat[4 * (n - 1) - 2][0] = Po[0][0] * Po[0][0] * Po[0][0]
    mat[4 * (n - 1) - 2][1] = Po[0][0] * Po[0][0]
    mat[4 * (n - 1) - 2][2] = Po[0][0]
    mat[4 * (n - 1) - 2][3] = 1
    vec[4 * (n - 1) - 2] = Po[0][1]

    mat[4 * (n - 1) - 1][4 * (n - 1) - 4] = Po[n-1][0] * Po[n-1][0] * Po[n-1][0]
    mat[4 * (n - 1) - 1][4 * (n - 1) - 3] = Po[n-1][0] * Po[n-1][0]
    mat[4 * (n - 1) - 1][4 * (n - 1) - 2] = Po[n-1][0]
    mat[4 * (n - 1) - 1][4 * (n - 1) - 1] = 1
    vec[4 * (n - 1) - 1] = Po[n-1][1]

    j = 1
    for i in range(2*(n-1), 4*(n-1)-2, 2):
        mat[i][(j - 1) * 4] = mat[i + 1][j * 4] = Po[j][0] * Po[j][0] * Po[j][0]
        mat[i][(j - 1) * 4 + 1] = mat[i + 1][j * 4 + 1] = Po[j][0] * Po[j][0]
        mat[i][(j - 1) * 4 + 2] = mat[i + 1][j * 4 + 2] = Po[j][0]
        mat[i][(j - 1) * 4 + 3] = mat[i + 1][j * 4 + 3] = 1
        vec[i] = vec[i + 1] = Po[j][1]
        j = j + 1

    ans = np.dot(np.linalg.inv(mat), vec)

    j = 1
    for j in range(4*(n - 1)):
        if abs(ans[j] - round(ans[j])) < 1e-6:
            ans[j] = round(ans[j])

    Eq = np.zeros((n-1, 4))

    for j in range(n - 1):
        Eq[j] = [ans[j * 4], ans[j * 4 + 1], ans[j * 4 + 2], ans[j * 4 + 3]]
        sngC.append("%.5f"%(Eq[j][0]) + "*x^3 + " + "%.5f"%(Eq[j][1]) + "*x^2 + " + "%.5f"%(Eq[j][2]) + "*x + " + "%.5f"%(Eq[j][3]))
    return sngC