class Vector:# задание 1
    error_code = 0  # Переменная состояния

    def __init__(self, size_or_value=None, value=None):
        if size_or_value is None:  # Конструктор без параметров
            self.elements = [0]
            self.size = 1
        elif value is None:  # Конструктор с одним параметром
            self.elements = [size_or_value]
            self.size = size_or_value
        else:  # Конструктор с двумя параметрами
            self.elements = [value] * size_or_value
            self.size = size_or_value

    def __del__(self):
        del self.elements  # Деструктор освобождает память

    def set_value(self, index, value=0):# установить значение
        try:
            self.elements[index] = value
        except IndexError:
            self.error_code = 1  # Устанавливаем код ошибки при вызове за пределами массива

    def get_value(self, index):# получить значение
        try:
            return self.elements[index]
        except IndexError:
            self.error_code = 1
            return None

    def print_vector(self):# вывести значение
        print(self.elements)

    def __add__(self, other):# сложение
        if isinstance(other, int):
            return [x + other for x in self.elements]
        elif isinstance(other, Vector):
            return [x + y for x, y in zip(self.elements, other.elements)]

    def __sub__(self, other):# вычитание
        if isinstance(other, int):
            return [x - other for x in self.elements]
        elif isinstance(other, Vector):
            return [x - y for x, y in zip(self.elements, other.elements)]

    def __mul__(self, other):# умножение
        if isinstance(other, int):
            return [x * other for x in self.elements]
        elif isinstance(other, Vector):
            return [x * y for x, y in zip(self.elements, other.elements)]

    def __gt__(self, other): # метод >
        if isinstance(other, Vector):
            return sum(self.elements) > sum(other.elements)
        else:
            return sum(self.elements) > other

    def __lt__(self, other):# метод <
        if isinstance(other, Vector):
            return sum(self.elements) < sum(other.elements)
        else:
            return sum(self.elements) < other

    def __eq__(self, other):# метод ==
        if isinstance(other, Vector):
            return self.elements == other.elements
        else:
            return False

    @classmethod
    def count_objects(cls):
        # Метод для подсчета числа объектов данного типа
        # Возможно, стоит использовать дополнительную переменную для хранения количества объектов.
        pass

v1 = Vector(3, 10)  # Создание вектора с тремя элементами, инициализированными значением 10
v2 = Vector(3, 5)  # Создание второго вектора

v1.print_vector()  # Вывод вектора
print(v1.get_value(1))  # Получение значения второго элемента
v1.set_value(1, 20)  # Установка значения второго элемента
v1.print_vector()  # Вывод измененного вектора

# Проверка арифметических операций
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2
print(v3, v4, v5)

# Проверка методов сравнения
print(v1 > v2)
print(v1 < v2)
print(v1 == v2)

class Matrix:
    def __init__(self, rows=0, cols=0):# конструктор матрицы
        self.rows = rows
        self.cols = cols
        self.data = [0] * (rows * cols)
        self.error = 0

    def __del__(self):# деструктор освобождает память
        del self.data

    def get_element(self, i, j):# получить элемент матрицы
        return self.data[i * self.cols + j]

    def get_element_address(self, i, j):# получить идентификатор элемента
        return id(self.data[i * self.cols + j])

    def print_matrix(self):# вывести матрицу
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i * self.cols + j], end=' ')
            print()

    def add_matrix(self, other):# cложение матриц
        if self.rows != other.rows or self.cols != other.cols:
            self.error = 1
            return
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i * self.cols + j] = self.data[i * self.cols + j] + other.data[i * self.cols + j]
        return result

    def subtract_matrix(self, other):# вычитание матриц
        if self.rows != other.rows or self.cols != other.cols:
            self.error = 1
            return
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i * self.cols + j] = self.data[i * self.cols + j] - other.data[i * self.cols + j]
        return result

    def multiply_matrix(self, other):# умножение матриц
        if self.cols != other.rows:
            self.error = 1
            return
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                for k in range(self.cols):
                    result.data[i * result.cols + j] += self.data[i * self.cols + k] * other.data[k * other.cols + j]
        return result

    def multiply_by_scalar(self, scalar):# умножение матрицы на число
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i * self.cols + j] = self.data[i * self.cols + j] * scalar
        return result
print("-------------")
m1 = Matrix(2, 2)
m1.data = [1, 2,
           3, 4]

m2 = Matrix(2, 2)
m2.data = [5, 6,
           7, 8]
#Сложение матриц
result_add = m1.add_matrix(m2)
result_add.print_matrix()

# Вычитание матриц
result_sub = m1.subtract_matrix(m2)
result_sub.print_matrix()

# Умножение матриц
result_mul = m1.multiply_matrix(m2)
result_mul.print_matrix()


result_scalar_mul = m1.multiply_by_scalar(2)
result_scalar_mul.print_matrix()
print("-------------")

class Date:# задание 3
    def __init__(self, day, month, year):# конструктор даты
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    def set_day(self, day):# установка дня(1-31)
        if 1 <= day <= 31:
            self.day = day
        else:
            print("Некорректное значение для дня")

    def set_month(self, month):# установка месяца(1-12)
        if 1 <= month <= 12:
            self.month = month
        else:
            print("Некорректное значение для месяца")

    def set_year(self, year):# установка года
        if isinstance(year, int):
            self.year = year
        else:
            print("Некорректное значение для года")

    def get_day(self):# вернуть день
        return self.day

    def get_month(self):# вернуть месяц
        return self.month

    def get_year(self):# вернуть год
        return self.year

    def print_date1(self):# вывести дату в в формате дд месяц гггг
        months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
        print(f"{self.day} {months[self.month - 1]} {self.year} года")

    def print_date2(self):# вывести дату в в формате дд.мм.гггг
        print(f"{self.day:02d}.{self.month:02d}.{self.year}")

d = Date(5, 1, 1997)
d.print_date1()# Выводит: 5 января 1997 года
d.print_date2()# Выводит 05.01.1997

