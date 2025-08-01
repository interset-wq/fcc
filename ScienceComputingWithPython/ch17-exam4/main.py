class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        """面积"""
        return self.width * self.height
    
    def get_perimeter(self):
        """周长"""
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        """对角线长度"""
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        """图形"""
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            return f'{"*" * self.width}\n' * self.height

    def get_amount_inside(self, shape):
        a = self.width // shape.width
        b = self.height // shape.height
        return a * b

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)

    def __repr__(self):
        return f'{self.__class__.__name__}(side={self.width})'

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area()) # 50
    rect.set_height(3)
    print(rect.get_perimeter()) # 26
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area()) # 81
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)  # Square(side=4)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
