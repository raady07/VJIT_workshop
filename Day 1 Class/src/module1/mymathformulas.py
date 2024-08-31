

class MyMathFormalus(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def _area(self):
        return self.x * self.y

    def _perimeter(self):
        return (self.x + self.y)*2
    
    def _square(self):
        return self.x ** self.y
    
    def run(self):
        return {
            "area": self._area(),
            "perimeter": self._perimeter(),
            "square": self._square()
        }