from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2025_02(DayBase):
    YEAR = "2025"
    DAY = "02"
    PREFIX = "ec"

class Complex:
    def __init__(self,x,y):
        (self.x, self.y) = (x,y)

    def __add__(self,other):
        return Complex(self.x + other.x,self.y+other.y)
    
    def __mul__(self,other):
        return Complex(self.x *other.x - self.y*other.y,self.x*other.y + self.y * other.x)
    
   

    def __truediv__(self,other):
        def floordiv(a,b):
            if a*b > 0:
                return a//b
            else:
                return - (-a//b)
        return Complex(floordiv(self.x,other.x),floordiv(self.y,other.y))
    
    def __str__(self):
        return f"[{self.x},{self.y}]"

    def outOfBounds(self):
        return self.x < -1000000 or self.x > 1000000 or self.y < -1000000 or self.y > 1000000
    
def part_1(input):
    line = next(input_generator(input))
    m = re.search(r'(\d+),(\d+)', line)
    assert m
    x = int(m.group(1))
    y = int(m.group(2))
    R = Complex(0,0)
    A = Complex(x,y)
    for _ in range(3):
        R = R * R
        R = R / Complex(10,10)
        R = R + A
    return R.__str__()    

def part_2(input, part=2):
    line = next(input_generator(input))
    m = re.search(r'(-?\d+),(-?\d+)', line)
    assert m
    x_start = int(m.group(1))
    y_start = int(m.group(2))
   
    count = 0
    if part == 2:
        step = 10
    else:
        step = 1    
    for x in range(x_start, x_start + 1001,step):
        for y in range(y_start, y_start + 1001,step):
            R = Complex(0,0)
            A = Complex(x,y)
            for i in range(100):
                R = R * R
                R = R / Complex(100000,100000)
                R = R + A
                if R.outOfBounds():
                    break
            else:
                count += 1         
    return count            




def part_3(input):
    return part_2(input, part=3)


if __name__ == "__main__":
    Run_2025_02().run_cmdline()
