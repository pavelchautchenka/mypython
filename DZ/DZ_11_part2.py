# ============================== 1 ===============================
print("\n N-1 ")


class Matrix:

    def __init__(self, matrix1: list[list], matrix2: list[list] = 0, n: int = 1):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.n = n

    def __str__(self):
        return f"\n first matrix: {self.matrix1} \n second matrix: { self.matrix2} \n numer for " \
               f"multiplication {self.n}"

    def get(self):
        return self.matrix1

# ======================================> все верно или надо через __new__?????
    def addition(self):
        return [[self.matrix1[i][j] + self.matrix2[i][j] for j in range(len(self.matrix1[0]))]
                for i in range(len(self.matrix1))]

    def deduction(self):
        return[[self.matrix1[i][j] - self.matrix2[i][j] for j in range(len(self.matrix1[0]))]
               for i in range(len(self.matrix1))]

    def multiplication(self):
        return [[self.matrix1[i][j] * self.n for j in range(len(self.matrix1[0]))]
                for i in range(len(self.matrix1))]

    def transpon(self):
        return [[self.matrix1[j][i] for j in range(len(self.matrix1))]
                for i in range(len(self.matrix1[0]))]


    @classmethod
    def indentity_matrix(cls, n: int,m: int):
        res = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
        return cls(res)

    @classmethod
    def nul_matrix(cls, n: int, m: int):
        res = [[0 if i == j else 0 for j in range(n)] for i in range(m)]
        return cls(res)

    @classmethod
    def diagonal_matrix(cls, t: list):
        res = [[t[i] if i == j else 0 for j in range(len(t))] for i in range(len(t))]
        return cls(res)
# от сюда в задании, у меня опять все методы черного цвета

    def size_of_matrix(self):
        return len(self.matrix1[0]), len(self.matrix1)

    def cont_elements(self):
        return len(self.matrix1[0])*len(self.matrix1)

    def summ_of_all_elements(self):
        return (sum(r) for r in self.matrix1)

    def positive_matrix(self):
        return [[max(0, num) for num in r] for r in self.matrix1]

    def equality_matrix(self):
        return self.matrix1 == self.matrix2

# ================================> как вывести на печать матрицу красивыми колонками,

# ================================> Скажите правильно ли вызваны все методы?
# ================================= и правильно ли  созданы объекты класса???


matrixs = Matrix([[-1, 3], [0, 1], [-2, 2]], [[2, 0], [-1,  1], [3, -2]], 5)
print("addition of matrix: ", matrixs.addition())

print("deduction of matrixs: ", matrixs.deduction())

print("matrix multiplication: ", matrixs.multiplication())

print("transponation of matrixs: ",  matrixs.transpon())

matrix_iden = Matrix.indentity_matrix(3, 5)
print("Identity matrix: ", matrix_iden.get())

matrix_zero = Matrix.nul_matrix(5, 6)
print("Zero matrix: ", matrix_zero.get())

diag_matrix = Matrix.diagonal_matrix([1, 3, 8, 99, 44, 55, 66])
print("Diagonal matrix: ", diag_matrix.get())

print("Size of matrix:", matrixs.size_of_matrix())

print("quantity of element in matrix:",   matrixs.cont_elements())

print("summ of all elements in matrix:", matrixs.summ_of_all_elements())

print("positive matrix: ", matrixs.positive_matrix())

print("equality of matrix is: ", matrixs.equality_matrix())

print(matrixs)