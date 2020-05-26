from vector import Vector


class Matrix:
    def __init__(self, plist_of_list, tup=None):
        if tup is not None and isinstance(plist_of_list, list):
            if isinstance(tup, tuple):
                if len(tup) != 2:
                    print("Tuple need a size of 2")
                    raise ValueError
                tmp_len = -1
                if len(plist_of_list) < tup[0]:
                    print("All arrays don't have ", end='')
                    print("the same size or lower than tuple size")
                    raise ValueError
                for i in plist_of_list:
                    if tmp_len != -1 and tmp_len < tup[1]:
                        print("All arrays don't have ", end='')
                        print("the same size or lower than tuple size")
                        raise ValueError
                    tmp_len = len(i)
                self.data = plist_of_list
                self.shape = tup
        elif isinstance(plist_of_list, list):
            tmp_len = -1
            for i in plist_of_list:
                if tmp_len != -1 and tmp_len != len(i):
                    print("All arrays don't have the same size")
                    raise ValueError
                tmp_len = len(i)
            self.data = plist_of_list
            self.shape = (len(plist_of_list), tmp_len)
        elif isinstance(plist_of_list, tuple):
            if len(plist_of_list) != 2:
                print("Tuple need a size of 2")
                raise ValueError
            self.data = [[0.0] * plist_of_list[1]] * plist_of_list[0]
            self.shape = plist_of_list
        else:
            raise ArithmeticError

    def __add__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] + other.data[i][j])
        elif isinstance(other, Vector) and self.shape[0] == other.size:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] + other.values[i])
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __radd__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] + other.data[i][j])
        elif isinstance(other, Vector) and self.shape[0] == other.size:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] + other.values[i])
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __sub__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] - other.data[i][j])
        elif isinstance(other, Vector) and self.shape[0] == other.size:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] - other.values[i])
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __rsub__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(other.data[i][j] - self.data[i][j])
        elif isinstance(other, Vector) and self.shape[0] == other.size:
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(other.values[i] - self.data[i][j])
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] / float(other))
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(float(other) / self.data[i][j])
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.shape[0] == other.shape[1]:
            if self.shape[1] == other.shape[0]:
                r = []
                for line in range(self.shape[0]):
                    r.append([])
                    for column in range(other.shape[1]):
                        val = 0
                        for i in range(len(self.data[line])):
                            val += self.data[line][i] * other.data[i][column]
                        r[line].append(val)
                return Matrix(r)
        elif isinstance(other, Vector) and self.shape[0] == other.size:
            r = []
            for i in range(self.shape[0]):
                rsum = 0
                for j in range(self.shape[1]):
                    rsum += self.data[i][j]
                r.append(rsum * other.values[i])
            return (Vector(r))
        elif isinstance(other, int) or isinstance(other, float):
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] * float(other))
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __rmul__(self, other):
        if isinstance(other, Matrix) and self.shape[0] == other.shape[1]:
            if self.shape[1] == other.shape[0]:
                r = []
                for line in range(self.shape[0]):
                    r.append([])
                    for column in range(other.shape[1]):
                        val = 0
                        for i in range(len(self.data[line])):
                            val += self.data[line][i] * other.data[i][column]
                        r[line].append(val)
                return Matrix(r)
        elif isinstance(other, Vector) and self.shape[0] == other.size:
            r = []
            for i in range(self.shape[0]):
                rsum = 0
                for j in range(self.shape[1]):
                    rsum += self.data[i][j]
                r.append(rsum * other.values[i])
            return (Vector(r))
        elif isinstance(other, int) or isinstance(other, float):
            r = []
            for i in range(self.shape[0]):
                r.append([])
                for j in range(self.shape[1]):
                    r[i].append(self.data[i][j] * float(other))
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Matrix(r, self.shape)

    def __str__(self):
        return ("Matrix " + str(self.data))

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
