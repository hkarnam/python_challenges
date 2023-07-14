from module_ import mul_num as ml

z = ml(4,5)

print(z)


# aliasing not just the module but also its inner functions is possible


from module import *

# to import everything in the module