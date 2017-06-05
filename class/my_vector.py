class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        msg = "(" + str(self.x) + "," + str(self.y) + ")"
        return msg


    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)


p = vec2(3,5)
q = vec2(-1,2)
r = p+q

print(p)
print(q)
print(r)