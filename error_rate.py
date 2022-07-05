import sympy as sp

class Func:
    
    def __init__(self, f, znac, pog): # функция должно быть функцией от массива
        self.f = f
        self.znac = znac
        self.pog = pog

    def d1(self, N): # функция возвращает значение частной производной по перемен X_N в точк M0. N = 0 , 1..
        d = 0.0000001
        M2 = self.znac.copy()
        M1 = self.znac.copy()
        M2[N] += d
        M1[N] -= d
        return (self.f(M2)-self.f(M1))/(2*d)
            
    def p(self):
        s = 0
        for i in range(len(self.znac)):
            s += (self.d1(i)*self.pog[i])**2
        return s**(1/2)
    
    def z(self):
        return self.f(self.znac)


def main():
    data = {
    "B": [1.9*10**(-6), 0.1*10**(-6)],
    "A": [3.558*10**(-4), 1.53*10**(-5)]
    }
    f = "A*3.71*297.5/(B*740*133.31)"
    print("результат функции pogresh(): ", pogresh(f,data))
    print("результат функции pog_prib(): ", pog_prib(f,data,0.000001))

    def f(x): 
        
        return x[0]*3.71*297.5/(x[1]*740*133.31)

    a = Func(f, [3.558*10**(-4), 1.9*10**(-6) ], [1.53*10**(-5), 0.1*10**(-6)])
    print("результат класса Func: ", a.z(), ' +- ', a.p())



#return [znach, pogr, pogr_masiv, pogr_formula]
def pogresh(f, data):
    # data = {
    #     "a": [12, 1],
    #     "b": [13, 2],
    #     "c": [11, 2.4]
    # }

    # f = "(a+b) ** 2 + b ** 3 + c ** 4"
    f = sp.sympify(f)

    pogr = 0
    pogr_masiv = []
    pogr_formula = []

    perem = []

    for i in data.keys():                          # perem = [(a,12), (b,12), (c,11)]
        perem.append((i, data[i][0]))

    for i in data.keys():                          # i = "a"
        x = sp.diff(f, i)                             # x = 2*a + 2*b
        pogr_formula.append(x)
        chast = x.subs(perem)
        pogr_masiv.append(chast * data[i][1])       #pogr_masiv = [x(perem)*Sa]

    for i in pogr_masiv:
        pogr += i ** 2

    pogr = pogr**(1/2)
    znach = f.subs(perem)

    return [znach, pogr, pogr_masiv, pogr_formula]   #return [znach, pogr, pogr_masiv, pogr_formula]

#return [znach, pogr, pogr_masiv]
def pog_prib(f, data, h):
    pogr = 0
    pogr_masiv = []

    # data = {
    #     "a": [12, 1],
    #     "b": [13, 2],
    #     "c": [11, 2.4]
    # }

    # h = 0.0001

    # f = "(a+b) ** 2 + b ** 3 + c ** 4"
    f = sp.sympify(f)

    perem = []

    for i in data.keys():  # perem = [(a,12), (b,12), (c,11)]
        perem.append((i, data[i][0]))

    for i in data.keys():  # i = a
        perem1 = []
        perem2 = []
        # ----------------------------------------------------------------
        for j in data.keys():
            if j != i:
                perem1.append((j, data[j][0]))                                # perem1 = [(b,12),(c,13)]
                perem2.append((j, data[j][0]))                                # perem2 = [(b,12),(c,13)]
        perem1.append((i, data[i][0] - h))
        perem2.append((i, data[i][0] + h))
        # ----------------------------------------------------------------
        chast = (f.subs(perem2) - f.subs(perem1)) / (2 * h)
        pogr_masiv.append(chast * data[i][1])

    for i in pogr_masiv:
        pogr += i ** 2
    pogr = pogr ** (1 / 2)
    znach = f.subs(perem)
    return [znach, pogr, pogr_masiv]

if __name__ == "__main__":
    main()





