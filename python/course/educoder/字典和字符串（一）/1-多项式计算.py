def Parse(str):
    # '+1x^0+2x^4'
    # {0: 1, 4: 2}
    res_dict = {}
    exp_arr = [str[i:i + 5] for i in range(0, len(str), 5)]
    for exp in exp_arr:
        zhi_shu = int(exp[-1])
        xi_shu = int(exp[0:2])
        res_dict[zhi_shu] = xi_shu
    return res_dict


def Eval(poly, x):
    sum = 0
    for zhi_shu in poly.keys():
        zhi_shu = int(zhi_shu)
        xi_shu = int(poly[zhi_shu])
        sum += xi_shu * pow(x, zhi_shu)
    return sum


polystr = '+1x^0+2x^4'
poly = Parse(polystr)
print(poly)
x = 2

print(Eval(poly, x))