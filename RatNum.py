""""
I Main use in mathimatical equations
II ADT
    Abstarct fields: num, den where num - numerator, den - denominator
    Abstaract operations: is_nan, is_negative, is_positive, compare_to, float_value, int_value, 
    negative, add, sub, mul, div, simplify, gcd, __str__, __hash__, __eq__
    Spec: 
    is nan return True if num == 'NaN' or den == 'NaN'
    is_negative return True if num / den < 0
    is_positive return True if num / den >= 0
    compare_to return True if num1 == num2 and den1 == den2  
    float_value return num/den as float data type
    int_value return num/den as int data type (rounds to a smaller)
    negative return -(num/den)
    add return ((num1*den2) + (num2*den1)) / (den1*den2)
    mul return (num1*num2) / (den1*den2)
    
    div return (num1*den2) / (den1*num2)
    simplify makes fraction reduction to better representation
    gcd return greatest common divisor
"""


class RatNum:
    def __init__(self, numerator, denominator = 1):
        if (type(numerator) != int) or (type(denominator) != int):
            if not((numerator == "NaN") or (denominator == "NaN")):
                raise TypeError('parametrs must be int')
            
        self.num = numerator
        self.den = denominator

    
    def is_nan(self):
        if self.num == 'NaN' or self.den == 'NaN':
            return True
        return False

    
    def is_negative(self):
        if self.num < 0 and self.den > 0:
            return True
        if self.num > 0 and self.den < 0:
            return True  
        return False  


    def is_positive(self):
        return not self.is_negative()
    

    def simplify(self):
        if self.is_nan():
            return self
        else:
            if self.den == 0:
                return RatNum(self.num, self.den)
            new_num = self.num
            new_den = self.den
            if new_num > new_den:
                k = new_num
            else:
                k = new_den
            
            while k != 1:
                if new_num % k == 0 and new_den % k == 0:
                    new_num = new_num // k
                    new_den = new_den // k
                else:
                    k -= 1
            return RatNum(new_num, new_den)


    def compare_to(self, other):
        if self.is_nan() or other.is_nan():
            return self.is_nan() and other.is_nan()
        else:
            if self.den == 0 or other.den == 0:
                if self.num > 0 and other.num > 0:
                    return True
                elif self.num < 0 and other.num < 0:
                    return True
                else:
                    return False
            else:
                own_temp = self.simplify()
                othr_temp = other.simplify()
                if own_temp.num == othr_temp.num and own_temp.den == othr_temp.den:
                    return True
            return False


    def float_value(self):
        if self.is_nan():
            return 'NaN'
        else:
            if self.den == 0:
                return 0
            else:
                return float(self.num/self.den)


    def int_value(self):
        if self.is_nan():
            return 'NaN'
        else:
            if self.den == 0:
                return 0
            else:
                return int(self.num/self.den)
    

    def negative(self):
        if self.is_negative():
            return RatNum(abs(self.num), abs(self.den))
        else:
            return RatNum(-self.num, self.den)
    

    def add(self,other):
        if self.den == 0 or other.den == 0:
            if self.den == 0:
                return RatNum(self.num, self.den)
            else: 
                return RatNum(other.num, other.den)
        elif self.is_nan() or other.is_nan():
            return RatNum('NaN', 'NaN')
        else:
            if self.den == other.den:
                return RatNum((self.num + other.num), self.den)
            else:
                return RatNum(((self.num*other.den) + (other.num*self.den)),  (self.den*other.den))



    def mul(self, other):
        if self.is_nan() or other.is_nan():
            return RatNum('NaN', 'NaN')
        else:
            return RatNum((self.num*other.num) ,  (self.den*other.den))


    def div(self, other):
        if type(other) != RatNum:
            other_new = RatNum(other)
        else:
            other_new = other
        other_temp = RatNum(other_new.den, other_new.num)
        ans = self.mul(other_temp)
        return RatNum(ans.num, ans.den)


    def gcd(n1, n2):
        num1 = n1.float_value()
        num2 = n2.float_value()
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return int(num1) or int(num2)


    def __eq__(self, other):
        if type(other) != RatNum:
            other_new = RatNum(other)
        else:
            other_new = other
        if self.is_nan() or other_new.is_nan():
            return self.is_nan() and other_new.is_nan()
        else:
            if self.den == 0 or other_new.den == 0:
                return False
            else:
                simpl_self = self.simplify()
                simpl_other = other_new.simplify()
                if other_new.is_negative() and self.is_negative():
                    return (abs(simpl_self.num) == abs(simpl_other.num)) and (abs(simpl_self.den) == abs(simpl_other.den))
                elif (simpl_other.is_negative() and not simpl_self.is_negative()) or (simpl_self.is_negative() and not simpl_other.is_negative()):
                    return False
                else:
                    return (simpl_self.num == simpl_other.num) and (simpl_self.den == simpl_other.den)


    def __str__(self):
        if self.num == 0 or self.den == 1:
            return '({0})'.format(self.num)
        else:
            return '({0} / {1})'.format(self.num, self.den)



if __name__ == '__main__':
    ratnum1 = RatNum(4,6)
    ratnum2 = RatNum(2,3)
    if ratnum1.simplify() == ratnum2:
        print('simplify test passed!')
    else:
        print('simplify test failed!')

    ratnum3 = RatNum('NaN',3)
    if ratnum3.is_nan():
        print('is_nan test passed!')
    else:
        print('is_nan test failed!')

    ratnum4 = RatNum(-4,3)
    if ratnum4.is_negative():
        print('is_negative test passed!')
    else:
        print('is_negative test failed!')

    ratnum5 = RatNum(5,3)
    if ratnum5.is_positive():
        print('is_positive test passed!')
    else:
        print('is_positive test failed!')

    ratnum6 = RatNum(1,2)
    ratnum7 = RatNum(15,30)
    if ratnum6.compare_to(ratnum7):
        print('compare_to test passed!')
    else:
        print('compare_to test failed!')

    if ratnum6.float_value() == 0.5:
        print('float_value test passed!')
    else:
        print('float_value test failed!')

    ratnum8 = RatNum(5,4)
    if ratnum8.int_value() == 1:
        print('int_value test passed!')
    else:
        print('int_value test failed!')

    ratnum9 = RatNum(5,-4)
    if ratnum8.negative() == ratnum9:
        print('negative test passed!')
    else:
        print('negative test failed!')

    ratnum10 = RatNum(3,4)
    ratnum11 = RatNum(1,2)
    ratnum12 = RatNum(10,8)
    if ratnum10.add(ratnum11) == ratnum12:
        print('add test passed!')
    else:
        print('add test failed!')

    ratnum13 = RatNum(3,8)
    if ratnum10.mul(ratnum11) == ratnum13:
        print('mul test passed!')
    else:
        print('mul test failed!')

    ratnum14 = RatNum(6,4)
    if ratnum10.div(ratnum11) == ratnum14:
        print('div test passed!')
    else:
        print('div test failed!')

    ratnum15 = RatNum(20)
    ratnum16 = RatNum(8)
    if RatNum.gcd(ratnum15,ratnum16) == 4:
        print('gcd test passed!')
    else:
        print('gcd test failed!')

    z = RatNum(0)
    n1 = RatNum(5, 0)
    n2 = RatNum(5, 2)
    n3 = RatNum(6, 3)
    n4 = n3.add(n2)
    n5 = RatNum(18, 9)
    print(z.add(n2))
    print(n4)
    print(n3 == n5)
