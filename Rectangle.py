#Marty Wallace CIS261 Rectangle

class rectangle():
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        area = self.height * self.width
        return area
    
    def perimeter(self):
        perimeter = 2 * self.height + 2 * self.width
        return perimeter
    
    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height -1:
                print('*' * self.width)
            else:
                print('*' + ' ' * (self.width - 2) + '*')


def rectangle_size():
    height = int(input("Height:     "))
    width = int(input("Width:      "))
    shape = rectangle(height, width)
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Perimeter:  {perimeter}")
    print(f"Area:       {area}")
    shape.print_rectangle()
    restart = input("Continue?  (y/n): ")
    if restart == "y":
        rectangle_size()
    
if __name__ == '__main__':
    print("Rectangle Calculator")
    print("")
    rectangle_size()
