import sys

sys.path.append("/")

import my_vector

a = my_vector.vec2(9,0)
b = my_vector.vec2(-1,-2)
c = a + b

print(c)