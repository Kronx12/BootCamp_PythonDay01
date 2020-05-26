class Vector:
    def __init__(self, plist):
        if isinstance(plist, list):
            self.values = plist
            self.size = len(plist)
        elif isinstance(plist, int):
            self.values = []
            self.size = plist
            for i in range(plist):
                self.values.append(float(i))
        elif isinstance(plist, tuple):
            self.values = []
            for i in range(plist[0], plist[1]):
                self.values.append(float(i))
            self.size = len(self.values)
        else:
            print("Vector Error, float needed")
            raise ValueError

    def __add__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            r = []
            for i in range(self.size):
                r.append(self.values[i] + other.values[i])
        elif (isinstance(other, list) or isinstance(other, tuple)):
            if len(other) == self.size:
                r = []
                for i in range(self.size):
                    r.append(self.values[i] + other[i])
        elif (isinstance(other, int) or isinstance(other, float)):
            r = []
            for i in range(self.size):
                r.append(self.values[i] + other)
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Vector(r)

    def __radd__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            r = []
            for i in range(self.size):
                r.append(self.values[i] + other.values[i])
        elif (isinstance(other, list) or isinstance(other, tuple)):
            if len(other) == self.size:
                r = []
                for i in range(self.size):
                    r.append(self.values[i] + other[i])
        elif (isinstance(other, int) or isinstance(other, float)):
            r = []
            for i in range(self.size):
                r.append(self.values[i] + other)
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Vector(r)

    def __sub__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            r = []
            for i in range(self.size):
                r.append(self.values[i] - other.values[i])
        elif (isinstance(other, list) or isinstance(other, tuple)):
            if len(other) == self.size:
                r = []
                for i in range(self.size):
                    r.append(self.values[i] - other[i])
        elif (isinstance(other, int) or isinstance(other, float)):
            r = []
            for i in range(self.size):
                r.append(self.values[i] - other)
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Vector(r)

    def __rsub__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            r = []
            for i in range(self.size):
                r.append(other.values[i] - self.values[i])
        elif (isinstance(other, list) or isinstance(other, tuple)):
            if len(other) == self.size:
                r = []
                for i in range(self.size):
                    r.append(other[i] - self.values[i])
        elif (isinstance(other, int) or isinstance(other, float)):
            r = []
            for i in range(self.size):
                r.append(other - self.values[i])
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Vector(r)

    def __truediv__(self, other):
        try:
            if isinstance(other, Vector) and other.size == self.size:
                r = []
                for i in range(self.size):
                    r.append(self.values[i] / other.values[i])
            elif (isinstance(other, list) or isinstance(other, tuple)):
                if len(other) == self.size:
                    r = []
                    for i in range(self.size):
                        r.append(self.values[i] / other[i])
            elif (isinstance(other, int) or isinstance(other, float)):
                r = []
                for i in range(self.size):
                    r.append(self.values[i] / other)
            else:
                print("Error, Incompatible type or size")
                raise ArithmeticError
        except ZeroDivisionError:
            print("Error Dvision by Zero")
            return None
        return Vector(r)

    def __rtruediv__(self, other):
        try:
            if isinstance(other, Vector) and other.size == self.size:
                r = []
                for i in range(self.size):
                    r.append(other.values[i] / self.values[i])
            elif (isinstance(other, list) or isinstance(other, tuple)):
                if len(other) == self.size:
                    r = []
                    for i in range(self.size):
                        r.append(other[i] / self.values[i])
            elif (isinstance(other, int) or isinstance(other, float)):
                r = []
                for i in range(self.size):
                    r.append(other / self.values[i])
            else:
                print("Error, Incompatible type or size")
                raise ArithmeticError
        except ZeroDivisionError:
            print("Error Dvision by Zero")
            return None
        return Vector(r)

    def __mul__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            r = 0
            for i in range(self.size):
                r += (self.values[i] * other.values[i])
            return (r)
        elif (isinstance(other, list) or isinstance(other, tuple)):
            if len(other) == self.size:
                r = []
                for i in range(self.size):
                    r.append(self.values[i] * other[i])
        elif (isinstance(other, int) or isinstance(other, float)):
            r = []
            for i in range(self.size):
                r.append(self.values[i] * other)
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Vector(r)

    def __rmul__(self, other):
        if isinstance(other, Vector) and other.size == self.size:
            r = 0
            for i in range(self.size):
                r += (self.values[i] * other.values[i])
        elif (isinstance(other, list) or isinstance(other, tuple)):
            if len(other) == self.size:
                r = []
                for i in range(self.size):
                    r.append(self.values[i] * other[i])
        elif (isinstance(other, int) or isinstance(other, float)):
            r = []
            for i in range(self.size):
                r.append(self.values[i] * other)
        else:
            print("Error, Incompatible type or size")
            raise ArithmeticError
        return Vector(r)

    def __str__(self):
        return "Vector " + str(self.values)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
