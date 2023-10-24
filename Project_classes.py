from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

class Patrat(FormaGeometrica):

    __latura = None

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        aria = self.__latura * self.__latura
        return aria

    def set_latura(self, __latura):
        self.__latura = __latura

    def get_latura(self):
        return self.__latura

class Cerc(FormaGeometrica):

    __raza = None

    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def delete_raza(self):
        self.__raza = None

    def aria(self):
        aria = self.PI * self.__raza * self.__raza
        return aria

    def descrie(self):
        print("Eu nu am colturi")


patrat1 = Patrat(4)
cerc1 = Cerc(5)

patrat1.set_latura(5)
print(patrat1.get_latura())
print(patrat1.aria())


cerc1.descrie()
print(cerc1.aria())
cerc1.delete_raza()
print(cerc1.get_raza())
