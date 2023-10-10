class Om:
    nume = None
    varsta = None
    greutate = None
    data_nastere = None

    def __init__(self, nume, varsta, greutate, data_nastere):

        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
        self.data_nastere = data_nastere


    def print_self(self):
        print("sunt in functia print self \n")
        print(self.nume, self.data_nastere, self.greutate, self.varsta)

    def __str__(self):
        return f"{self.nume}, {self.varsta}, {self.greutate}, {self.data_nastere}"


