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

    scale_coeff returns [coef[0]*k coef[1]*k ... coef[n]*k], where k - scalee coef n = 1...n 

    negate returns [-coef[0] -coef[1] ... -coef[n]]

    add returns poly1+poly2: [poly1_coef[0] + poly2_coef[0] poly1_coef[1] + poly2_coef[1] + ...]

    sub returns poly1-poly2: [poly1_coef[0] - poly2_coef[0] poly1_coef[1] - poly2_coef[1] + ...]
    
    mul returns poly1*poly2 : [poly1_coef[i]*poly2_coef[j]] where i = 1...n, j = 1 ... k

    div returns poly1/const : [poly1_coef[i]/const] where i = 1...n, j = 1 ... k

    eval(k) retruns float which rerpresents value of equation: poly(x) where x = f

    value_of(string) retruns Ratpoly from string, working only with int coef!!!

    differentiate retruns diff poly by poly.simb

    integrate retruns integral poly by poly.simb



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


    def scale_coeff(self, k):
        if type(k) == RatNum.RatNum or type(k) == int:
            temp_list = []
            for i in range(len(self.k)):
                temp_list.append(self.k[i].mul(k))
            return RatPoly(temp_list, self.symb)
        else:
            raise TypeError('k must be int or RatNum')
            

    def negate(self):  
        temp_list = []
        for elem in self.k:
            temp_list.append(elem.negative()) 
        return RatPoly(temp_list, self.symb)


    def add(self, other):
        if self.symb != other.symb:
            raise ValueError('var symbol not equal')
        else:
            list1 = []
            indx = 0
            for i in range(len(self.k)):
                for k in range(len(other.k)):
                    if i == k:
                        list1.append(self.k[-i-1].add(other.k[-k-1]).simplify())
                    if k > len(self.k)-1+indx and i == len(self.k)-1:
                        list1.append(other.k[-k-1].simplify())
                        indx += 1
                if i > len(other.k)-1:
                    list1.append(self.k[-i-1].simplify())
            return RatPoly(list1[::-1], self.symb)


    def mul(self, other):
        if type(other) == RatNum.RatNum or type(other) == int:
            return self.scale_coeff(other)
        elif type(other) == RatPoly:
            temp_list = []
            for i in range(len(self.k)+len(other.k)-1):
                temp_list.append(0)
            for i in range(len(self.k)):
                for k in range(len(other.k)):
                    temp_list[i+k] = self.k[i].mul(other.k[k]).add(temp_list[i+k]).simplify()
            return RatPoly(temp_list, self.symb)
        else:
            raise TypeError('other val must be int or RatPoly or RatNum')


    def div(self, other):
        if type(other) == RatNum.RatNum or type(other) == int:
            temp_list = []
            for i in range(len(self.k)):
                temp_list.append(self.k[i].div(other).simplify())
            return RatPoly(temp_list, self.symb)
        else:
            raise TypeError('other val must be int or RatNum')
        

    def sub(self, other):
        if type(other) == int:
            temp_other = RatNum.RatNum(other)
        else:
            temp_other = other
        neg_other = temp_other.negate()
        return self.add(neg_other)


    def eval(self, k):
        if type(k) == float:
            ans = 0.0
            for i in range(len(self.k)):
                if len(self.k)-i-1 == 0:
                    ans += self.k[i].float_value()
                else:
                    ans += self.k[i].float_value()*(k**(len(self.k)-i-1))
            return ans

        else: 
            raise TypeError('k must be float')


    def differentiate(self):
        temp_list = []
        for i in range(len(self.k)-1):
            temp_list.append(self.k[i].mul((len(self.k)-i-1)).simplify())
        return RatPoly(temp_list, self.symb)


    def integrate(self):
        temp_list = []
        for i in range(len(self.k)):
            temp_list.append(self.k[i].div((len(self.k)-i)).simplify())
        temp_list.append(1)
        return RatPoly(temp_list, self.symb)


    def value_of(exmpl):
        
        def ckeckList(lst): 
            ele = lst[0]
            chk = True
            # Comparing each element with first item
            for item in lst:
                if ele != item:
                    chk = False
                    break
            return chk

        exmpl_list = list(exmpl)
        expml_list_v2 = []
        indx = -2
        temp = ""
        buf = ""
        for i in range(len(exmpl_list)):
            try:
                a = int(exmpl_list[i])
            except ValueError:
                # exmpl_list[i] = symbol
                buf = exmpl_list[i]
                if temp != "":
                    expml_list_v2.append(temp)
                    temp = ""
                expml_list_v2.append(exmpl_list[i])
            else:
                # exmpl_list[i] = int
                if buf == "-" and temp == "":
                    temp += buf
                    if i < 2:
                        del expml_list_v2[-1]
                    else:
                        if expml_list_v2[-2] != "^":
                            expml_list_v2[-1] = "+"
                        else:
                            del expml_list_v2[-1]
                temp += exmpl_list[i]
                if i == len(exmpl_list)-1:
                    expml_list_v2.append(temp)
                            
        expml_list_v3 = []
        for elem in expml_list_v2:
            try:
                a = int(elem)
            except ValueError:
                # elem = symbol
                expml_list_v3.append(elem)
            else:
                # elem = int
                expml_list_v3.append(int(elem))


        sym = ""
        list_sym = expml_list_v3
        list_sym_v2 = []
        for i in range(len(list_sym)):
            if list_sym[i] not in ["+","-","*","^"] and type(list_sym[i]) != int:
                list_sym_v2.append(list_sym[i]) 
        if not ckeckList(list_sym_v2):
            raise ValueError("In poly myst be only one symb variable")
        else:
            sym = list_sym_v2[0]
            
        powers = []
            
        for i in range(len(list_sym)):
            if i > 1:
                if list_sym[i-1] == "^":
                    powers.append(list_sym[i])

        list_for_poly = []
        for i in range(max(powers)+1):
            list_for_poly.append(0)

        for i in range(len(list_sym)):
            if list_sym[i] == sym:
                if i == 0:
                    if list_sym[i+1] == "^":
                        list_for_poly[-list_sym[i+2]-1] = 1
                    else:
                        list_for_poly[-2] = 1
                else:
                    if list_sym[i-1] == "*":
                        if list_sym[i+1] == "^":
                            list_for_poly[-list_sym[i+2]-1] = list_sym[i-2]
                        else:
                            list_for_poly[-2] = list_sym[i-2]
            else:
                if i < len(list_sym)-1 and i != 0:
                    if type(list_sym[i]) == int and list_sym[i+1] != "*" and list_sym[i-1] != "^":
                        list_for_poly[-1] = list_sym[i]
                else:
                    if type(list_sym[i]) == int:
                        list_for_poly[-1] = list_sym[i]
        return RatPoly(list_for_poly, sym)
                        

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

    
    def __eq__(self, other):
        if type(other) == RatPoly:
            if self.symb != other.symb:
                return False
            else:
                for i in range(len(self.k)):
                    for k in range(len(other.k)):
                        if self.k[i] != other.k[k] and i == k:
                            return False  
            if len(self.k) != len(other.k):
                return False  
        elif type(other) == int or type(other) == RatNum.RatNum:
            if self.k[-1] != other:
                return False
        else: 
            raise TypeError('other val must be int or RatPoly or RatNum')
        return True


    def __hash__(self):
        return hash(self.k, self.symb)


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
    p5 = RatPoly([1, 3, RatNum.RatNum(-4,3), RatNum.RatNum(5,2), 3], "x")
    
    if p3.add(p4) == p5:
        print('add test passed!')
    else:
        print('add test failed!')

    p6 = p5.scale_coeff(2)
    p7 = RatPoly([2, 6, RatNum.RatNum(-8,3), 5, 6], "x")
    if p6 == p7:
        print('scale_coeff test passed!')
    else:
        print('scale_coeff test failed!')    

    p8 = RatPoly([-2, -6, RatNum.RatNum(8,3), -5, -6], "x")
    if p6.negate() == p8:
        print('negate test passed!')
    else:
        print('negate test failed!') 

    p9 = RatPoly([1, 0, RatNum.RatNum(-17,6), RatNum.RatNum(11,3), RatNum.RatNum(4,3), RatNum.RatNum(1,3), RatNum.RatNum(9,2), 2], "x")
    if p3.mul(p4) == p9:
        print('mul test passed!')
    else:
        print('mul test failed!') 

    if (p6.sub(p5) == p5):
        print('sub test passed!')
    else:
        print('sub test failed!') 

    if p9.eval(2.0) == 119.0 and p9.eval(0.0) == 2.0:
        print('eval test passed!')
    else:
        print('eval test failed!')    

    p10 = RatPoly([7, 0, RatNum.RatNum(-85,6), RatNum.RatNum(44,3), 4, RatNum.RatNum(2,3), RatNum.RatNum(9,2)], "x")
    if (p9.differentiate() == p10):
        print('differentiate test passed!')
    else:
        print('differentiate test failed!')    

    p11 = RatPoly([RatNum.RatNum(1, 8), 0, RatNum.RatNum(-17,36), RatNum.RatNum(11,15), RatNum.RatNum(1,3), RatNum.RatNum(1,9), RatNum.RatNum(9,4), 2, 1], "x")
    if p9.integrate() == p11:
        print('integrate test passed!')
    else:
        print('integrate test failed!')  

    p12 = RatPoly([-23, -2345, 0, -1234], "x")
    if (RatPoly.value_of("-23*x^3-2345*x^2-1234") == p12):
        print('value_of test passed!')
    else:
        print('value_of test failed!')  

    p13 = RatPoly([99, 66, 33, 11], "y")
    p14 = RatPoly([9, 6, 3, 1], "y")
    if (p13.div(11) == p14):
        print('div test passed!')
    else:
        print('div test failed!') 




