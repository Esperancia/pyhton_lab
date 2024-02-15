class Grade:

    _nbrInstances = 0

    # =======================constructeur=============================
    def __init__(self, department: str, courseNum: int, percent: float):
        self.__department = department.upper()
        self.__courseNum = courseNum
        self.__percent = percent

        if self.__percent < 0 or self.__percent > 100:
            print("Impossible de donner une note inferieure a 0 ou superieure a 100")
            return

        if self.__percent < 50:
            self.__letter = 'E'
        elif self.__percent < 57:
            self.__letter = 'D'
        elif self.__percent < 66:
            self.__letter = 'C'
        elif self.__percent < 75:
            self.__letter = 'B'
        elif self.__percent <= 100:
            self.__letter = 'A'

        Grade._nbrInstances += 1

#=======================accesseurs=============================
    def getDepartment(self):
        return self.__department

    def getCourse(self):
        return self.__courseNum

    def getPercent(self):
        return self.__percent

    def getLetter(self):
        return self.__letter


    @classmethod
    def getInstanceCount(cls):
        return cls._nbrInstances

    # =======================__str__=============================

    def __str__(self) -> str:
        return "{}{} {} {}".format(self.__department, self.__courseNum, self.__letter, self.__percent)


# =======================Programme principal=============================
if __name__ == "__main__":
    note1 = Grade('GTI', 121, 68.5)
    print(note1.__str__())

    note2 = Grade('MAT', 144, 57)
    print(str(note2))

    note3 = Grade('MAT', 350, 74.99)
    print(note3.__str__())

    print('nombre de notes : ', Grade.getInstanceCount())
    # print(g.getInstanceCount())

