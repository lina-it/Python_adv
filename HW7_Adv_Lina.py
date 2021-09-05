
class Matrix:
    def __init__(self, a11, a12, a13,
                 a21, a22, a23,
                 a31, a32, a33):
        self.a11 = a11
        self.a12 = a12
        self.a13 = a13
        self.a21 = a21
        self.a22 = a22
        self.a23 = a23
        self.a31 = a31
        self.a32 = a32
        self.a33 = a33

    def __str__(self):
        return f"Результирующая матрица:\n" \
               f"[{self.a11}] [{self.a12}] [{self.a13}]\n" \
               f"[{self.a21}] [{self.a22}] [{self.a23}]\n" \
               f"[{self.a31}] [{self.a32}] [{self.a33}]"

    def __add__(self, other: 'Matrix'):
        if type(other) != Matrix:
            raise TypeError(f"Unsupported type for summarize with type Matrix! {type(other)}")
        return Matrix(self.a11 + other.a11,
                      self.a12 + other.a12,
                      self.a13 + other.a13,
                      self.a21 + other.a21,
                      self.a22 + other.a22,
                      self.a23 + other.a23,
                      self.a31 + other.a31,
                      self.a32 + other.a32,
                      self.a33 + other.a33)

    def __sub__(self, other: 'Matrix'):
        if type(other) != Matrix:
            raise TypeError(f"Unsupported type for summarize with type Matrix! {type(other)}")
        return Matrix(self.a11 - other.a11,
                      self.a12 - other.a12,
                      self.a13 - other.a13,
                      self.a21 - other.a21,
                      self.a22 - other.a22,
                      self.a23 - other.a23,
                      self.a31 - other.a31,
                      self.a32 - other.a32,
                      self.a33 - other.a33)

    def __mul__(self, other: 'Matrix'):
        if type(other) != Matrix:
            raise TypeError(f"Unsupported type for summarize with type Matrix! {type(other)}")
        return Matrix(self.a11 * other.a11,
                      self.a12 * other.a12,
                      self.a13 * other.a13,
                      self.a21 * other.a21,
                      self.a22 * other.a22,
                      self.a23 * other.a23,
                      self.a31 * other.a31,
                      self.a32 * other.a32,
                      self.a33 * other.a33)


    def __truediv__(self, other: int):
        other = int(input("Введите делитель: "))
        return Matrix(self.a11 / other,
                      self.a12 / other,
                      self.a13 / other,
                      self.a21 / other,
                      self.a22 / other,
                      self.a23 / other,
                      self.a31 / other,
                      self.a32 / other,
                      self.a33 / other)

    def equal(self, other):
        if self.a11 == other.a11 and self.a12 == other.a12 and self.a13 == other.a13 and \
            self.a21 == other.a21 and self.a22 == other.a22 and self.a23 == other.a23 and \
            self.a31 == other.a31 and self.a32 == other.a32 and self.a33 == other.a33:
            return True
        else:
            return False


    def __iter__(self):
        """Альтернативный протокол итерации"""
        return iter([self.a11, self.a12, self.a13,
                     self.a21, self.a22, self.a23,
                     self.a31, self.a32, self.a33])


Matrix_1 = Matrix(1,2,3,4,5,6,7,8,9)
Matrix_2 = Matrix(9,8,7,6,5,4,3,2,1)
Matrix_10 = Matrix(1,2,3,4,5,6,7,8,9)
Matrix_3 = Matrix_1 + Matrix_2 + Matrix_1
print(Matrix_3)
Matrix_4 = Matrix_1 - Matrix_2 - Matrix_1
print(Matrix_4)
Matrix_5 = Matrix_1 * Matrix_2 * Matrix_1
print(Matrix_5)
Matrix_6 = Matrix_1/0
print(Matrix_6)
Matrix_7 = Matrix.equal(Matrix_1, Matrix_10)
Matrix_8 = Matrix.equal(Matrix_1, Matrix_2)
print(Matrix_7)
print(Matrix_8)

# for el in Matrix_3:
#     print(el)