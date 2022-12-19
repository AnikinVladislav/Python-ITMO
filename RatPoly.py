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

    scale_coeff ???

    negate ???

    add returns poly1+poly2: [poly1_coef[0] + poly2_coef[0] poly1_coef[1] + poly2_coef[1] + ...]


"""

class RatPoly:

    def __init__(self, coef, var):
        coef_temp = []
        for elem in coef:
            if type(elem) == RatNum.RatNum:
                coef_temp.append(elem)
            else:
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
    

    # def add(self, other):
    #     ans = RatPoly([],self.symb)
    #     if type(other) != RatPoly:
    #         new_other = RatPoly(other,self.symb)
    #     else:
    #         new_other = other
    #     if self.symb != new_other.symb:
    #         raise ValueError('self.symb not equal other.symb')
    #     for elem_s in self.k:
    #         for elem_o in new_other.k:


                
        

    def __str__(self):
        poly_str = "["
        temp = 1
        for elem in self.k:
            if temp == len(self.k):
                poly_str += f" {elem}"
            else:
                if elem == 1 or elem == -1:
                    if elem.int_value() > 0:
                        poly_str += f"{self.symb}^{len(self.k) - temp}, "
                    else:
                        poly_str += f"-{self.symb}^{len(self.k) - temp}, "
                else:
                    poly_str += f"{elem}*{self.symb}^{len(self.k) - temp}, "
            temp += 1
        poly_str += "]"
        return poly_str


if __name__ == '__main__':
    p1 = RatPoly([1, -2, RatNum.RatNum(3,6), -4], "x")
    print(p1)

    if p1.degree() == 3:
        print('degree test passed!')
    else:
        print('degree test failed!')

    if p1.get_coef(-2) == -4:
        print('get_coef test passed!')
    else:
        print('get_coef test failed!')

    p2 = RatPoly([1, 'NaN', 9, -4], "x")
    if p2.is_nan():
        print('is_nan test passed!')
    else:
        print('is_nan test failed!')

    p3 = RatPoly([1, 2, RatNum.RatNum(2,3), 2, 1], "x")
    p4 = RatPoly([1, -2, RatNum.RatNum(3,6), 2], "x")
    list1 = []
    for i in range(len(p3.k)):
            for k in range(len(p4.k)):
                if i == k:
                    list1.append(p3.k[i].add(p4.k[i]).simplify())
                    # print(f'{p3.k[i]} + {p4.k[i]} = {p3.k[i].add(p4.k[i]).simplify()}')
                if i > len(p4.k):
                    list1.append(p3.k[i].simplify())
                elif k > len(p3.k):
                    list1.append(p4.k[i].simplify())
    print(RatPoly(list1, p3.symb))
