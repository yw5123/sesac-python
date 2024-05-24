class Calculator:
    mode = None

    def __init__(self,mode):
        self.mode = mode
    
    def get_mode(self):
        return self.mode
    
    def calc_add(self, num1, num2):
        return num1+num2
    
    def calc_sub(self, num1, num2):
        return num1-num2
    
my_calc = Calculator("표준")
print(my_calc.calc_add(1,2))
print(my_calc.calc_sub(1,2))


class EngCalculator(Calculator):
    def calc_mul(self, num1, num2):
        return num1*num2

my_calc = EngCalculator("공학용")
print(my_calc.calc_mul(2,3))
print(my_calc.calc_add(2,3))
print(my_calc.calc_sub(2,3))