class MyPoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self, x, y):
        
p1 = MyPoint(1, 2)
print(p1.x, p1.y)