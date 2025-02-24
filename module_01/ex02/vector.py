class Vector:
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), len(values[0])) if len(values[0]) > 1 else (len(values), 1)

    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        result = sum(self.values[i][0] * other.values[i][0] for i in range(self.shape[0]))
        return result

    def T(self):
        if self.shape == (1, 1):
            return Vector([[self.values[0][0]]])
        return Vector([[self.values[i][0] for i in range(self.shape[0])]])

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        result = [[self.values[i][0] + other.values[i][0]] for i in range(self.shape[0])]
        return Vector(result)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        result = [[self.values[i][0] - other.values[i][0]] for i in range(self.shape[0])]
        return Vector(result)

    def __mul__(self, scalar):
        result = [[self.values[i][0] * scalar] for i in range(self.shape[0])]
        return Vector(result)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Division by zero")
        result = [[self.values[i][0] / scalar] for i in range(self.shape[0])]
        return Vector(result)

    def __rtruediv__(self, scalar):
        raise ArithmeticError("Cannot divide vector by scalar from the right")
