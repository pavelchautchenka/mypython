# ============================== 1 ===============================
print("\n N-1 ")


class Matrix:

    def __init__(self, matrix1: list[list], matrix2: list[list] = 0, scalar: int = 1):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.scalar = scalar

    def __str__(self):
        result = ""
        for row in self.matrix1:
            result += "  ".join(str(i) for i in row) + "\n"
        return result

    def __eq__(self, other):
        return self.matrix1 == other

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix1) != len(other.matrix1) or len(self.matrix1[0]) != len(other.matrix1[0]):
                return "Must have the same dimensions"
            else:
                return [[self.matrix1[i][j] + other.matrix1[i][j] for j in range(len(self.matrix1[0]))]
                        for i in range(len(self.matrix1))]

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix1) != len(other.matrix1) or len(self.matrix1[0]) != len(other.matrix1[0]):
                return "Must have the same dimensions"
            else:
                return [[self.matrix1[i][j] - other.matrix1[i][j] for j in range(len(self.matrix1[0]))]
                        for i in range(len(self.matrix1))]

    def __mul__(self, other):
        return [[self.matrix1[i][j] * other for j in range(len(self.matrix1[0]))]
                for i in range(len(self.matrix1))]

    def get(self):
        return self.matrix1

    def transpon(self):
        return [[self.matrix1[j][i] for j in range(len(self.matrix1))]
                for i in range(len(self.matrix1[0]))]

    @classmethod
    def indentity_matrix(cls, n: int,m: int):
        res = [[1 if i == j else 0 for j in range(n)] for i in range(m)]
        return cls(res)

    @classmethod
    def nul_matrix(cls, n: int, m: int):
        res = [[0 for j in range(n) for i in range(m)]]
        return cls(res)

    @classmethod
    def diagonal_matrix(cls, t: list):
        res = [[t[i] if i == j else 0 for j in range(len(t))] for i in range(len(t))]
        return cls(res)

    def size_of_matrix(self):
        return len(self.matrix1[0]), len(self.matrix1)

    def count_elements(self):
        return len(self.matrix1[0])*len(self.matrix1)

    def summ_of_all_elements(self):
        return (sum(r) for r in self.matrix1)

    def positive_matrix(self):
        return [[max(0, num) for num in r] for r in self.matrix1]


matrixs = Matrix([[-1, 3], [0, 1], [-2, 2]], [[2, 0], [-1,  1], [3, -2]], 5)

print("transponation of matrixs: ",  matrixs.transpon())

matrix_iden = Matrix.indentity_matrix(3, 5)
print("Identity matrix: ", matrix_iden.get())

matrix_zero = Matrix.nul_matrix(5, 6)
print("Zero matrix: ", matrix_zero.get())

diag_matrix = Matrix.diagonal_matrix([1, 3, 8, 99, 44, 55, 66])
print("Diagonal matrix: ", diag_matrix.get())

print("Size of matrix:", matrixs.size_of_matrix())

print("quantity of element in matrix:",   matrixs.count_elements())

print("summ of all elements in matrix:", matrixs.summ_of_all_elements())

print("positive matrix: ", matrixs.positive_matrix())

mat1 = Matrix([[2, 3], [0, 1], [2, 2]])

mat2 = Matrix([[2, 0], [-1,  1], [3, -2,2]])
mat3 = Matrix([[151,123], [101, -1], [2222, 500]])



print("\n", mat3 == mat2)

print("\n", mat1 + mat2)

print("\n", mat1 * 5)

print("\n", mat1 - mat2,"\n")

print(mat1)