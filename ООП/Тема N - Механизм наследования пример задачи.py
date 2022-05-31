class Polygon:
    """Создадим класс полигон.
    Полигон - замкнутая геометрическая фигура
    с 3 и более сторон"""

    def __init__(self, amount_of_sides):
        print("Введите точки объекта")
        self.n = amount_of_sides  # Количество сторон в полигоне
        self.size_of_sides = []  # Список размеров сторон в полигоне
        for i in range(self.n):
            self.size_of_sides.append(int(input()))

    def print_polygon_coords(self):
        print("Создан полигон по координатам" + str(self.size_of_sides))


class Triangle(Polygon):
    """Создадим класс Теругольник.
    Треугольник - это полигон с тремя сторонами"""
    def __init__(self):
        Polygon.__init__(self, 3)

    def calculate_triangle_area(self):
        a, b, c = self.size_of_sides
        # Расчет площади
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Rectangle(Polygon):
    """Создадим класс прямоугольник.
    Прямоугольник - это полигон с 4 сторонами"""
    def __init__(self):
        Polygon.__init__(self, 4)

    def calculate_rectangle_area(self):
        a, b, c, d = self.size_of_sides
        # Расчет площади
        return a * b


p1 = Polygon(4)
p1.print_polygon_coords()

t1 = Triangle()
print(t1.calculate_triangle_area())

h1 = Hexogon()
