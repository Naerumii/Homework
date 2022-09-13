import math

class Area(): # Area라는 이름의 class 선언
    def set_area(self, w, h):
        self.w = w
        self.h = h

    def square(self):
        result = self.w * self.h
        return result

    def triangle(self):
        result = self.w * self.h / 2
        return result

    def circle(self):
        result = (self.w / 2)**2 * math.pi
        return result            

area = Area()

area.set_area(10, 20)

print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이