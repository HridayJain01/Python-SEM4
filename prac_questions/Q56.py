#create a function that takes one argument and that argument will be multiplied with an unknown given number

def multiplier_factory(factor):
    def multiplier(x):
        return x*factor;
    return multiplier

factor_3 = multiplier_factory(3)
factor_5 = multiplier_factory(5)

print(factor_3(5))
print(factor_5(10))