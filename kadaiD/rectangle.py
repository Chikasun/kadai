class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return f'{self.height * self.width:.2f}'

    def diagonal(self):
        return f'{(self.height ** 2 + self.width ** 2) ** 0.5:.2f}'


rectangle1 = Rectangle(height=5, width=6)
rectangle2 = Rectangle(height=3, width=3)
print(rectangle1.area())
print(rectangle1.diagonal())
print(rectangle2.area())
print(rectangle2.diagonal())
