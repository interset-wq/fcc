class R2Vector:
    """二维向量"""
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        """向量的模"""
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        """返回向量的坐标
        调用print()和str()时会自动调用这个方法
        例如 (2, 3)
        """
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        """返回对象的详细信息
        调用repr()函数时自动调用这个方法
        如果没有定义__str__魔术方法 调用print()和str()时也自动调用这个方法
        例如 R2Vector(x=2, y=3)
        """
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        """向量加法"""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """向量减法"""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """向量乘法"""
        if type(other) in (int, float):
            # 数乘向量
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            # 点乘向量（数量积）
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        """是否相等"""
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        """是否不相等"""
        return not self == other

    def __lt__(self, other):
        """比较是否小于"""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        """比较是否大于"""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        """比较是否小于等于"""
        return not self > other

    def __ge__(self, other):
        """比较是否大于等于"""
        return not self < other

class R3Vector(R2Vector):
    """三维向量"""
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        
    def cross(self, other):
        """向量叉乘"""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }   
        return self.__class__(**kwargs)
    
v1 = R3Vector(x=2, y=3, z=1)
print(v1)
print(repr(v1))
# v2 = R3Vector(x=0.5, y=1.25, z=2)
# print(f'v1 = {v1}')
# print(f'v2 = {v2}')
# v3 = v1 + v2
# print(f'v1 + v2 = {v3}')
# v4 = v1 - v2
# print(f'v1 - v2 = {v4}')
# v5 = v1 * v2
# print(f'v1 * v2 = {v5}')
# v6 = v1.cross(v2)
# print(f'v1 x v2 = {v6}')
# print(vars(v1))