from math import pi

def hello() :
    return 'Hello'

def area_of_circle(radius) :
    return pi * radius ** 2


if __name__ == "__main__":
    rad = 10
    area = area_of_circle(rad)
    print('area of circle with radius {rad:04d} is {area:015.4f}'.format(rad=rad,area=area))
    print(round(area_of_circle(7)) == 154)
    print(round(area_of_circle(10)) == 314)  
