# from my_math import operations

# print(operations.mul(3,4))

import math

def test(x1,x2,y1,y2) :
    dis = 0.0
    dis = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    
print(test(2,1,2,1))