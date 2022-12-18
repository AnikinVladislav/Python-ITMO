import RatNum

""""
I Main use in mathimatical equations
II ADT
    Abstarct fields: coef = [coef0 coef1 ... coefn], var
    Abstaract operations: degree, get_coef, is_nan, scale_coeff, negate, add, sub, mul, div
    eval, differentiate, anti_differentiate, integrate, value_of, __str__, __hash__, __eq__ 
    Spec: 
    degree returns max power of poly

    get_coef returns coef by power

    is_nan returns True if coef[k] == NaN


"""

class RatPoly:

    def __init__(self, coef, var):
        coef_temp = []
        for elem in coef:
            coef_temp.append(RatNum.RatNum(elem))
        
        self.k = coef_temp
        self.symb = var


    def degree(self):
        return len(self.k)-1


    def get_coef(self, pwr):
        if pwr < 0:
            pwr = 0
        return self.k[len(self.k)-1-pwr]


    def is_nan(self):
        for elem in self.k:
            if elem.is_nan():
                return True
        return False
                
        

    def __str__(self):
        poly_str = "["
        temp = 1
        for elem in self.k:
            if temp == len(self.k):
                poly_str += f" {elem}"
            else:
                if elem == 1 or elem == -1:
                    if elem > 0:
                        poly_str += f"{self.symb}^{len(self.k) - temp}, "
                    else:
                        poly_str += f"-{self.symb}^{len(self.k) - temp}, "
                else:
                    poly_str += f"{elem}*{self.symb}^{len(self.k) - temp}, "
            temp += 1
        poly_str += "]"
        return poly_str


if __name__ == '__main__':
    p1 = RatPoly([1.5, -2, RatNum.RatNum(3,6), -4], "x")
    print(p1)

    if p1.degree() == 3:
        print('degree test passed!')
    else:
        print('degree test failed!')

    if p1.get_coef(-2) == -4:
        print('get_coef test passed!')
    else:
        print('get_coef test failed!')

    p2 = RatPoly([1.5, 'NaN', 9, -4], "x")
    print(p1.is_nan())