class Cpf(object):
    def __init__(self, cpf):
        self.cpf = cpf

    def valid(self):
        return self.__validate_format() and self.__validate_cpf()

    def __validate_format(self):
        return (len(self.cpf) == 11 and
                self.cpf.isnumeric() and
                len(set(self.cpf)) != 1)

    def __validate_cpf(self):
        penultimate_sum = sum([(10-idx) * int(digit)
                               for idx, digit in enumerate(self.cpf[0:9])])
        penultimate_rem = (penultimate_sum * 10 % 11
                           if penultimate_sum * 10 % 11 != 10
                           else 0)

        if penultimate_rem != int(self.cpf[-2]):
            return False

        ultimate_sum = sum([(11-idx) * int(digit)
                            for idx, digit in enumerate(self.cpf[0:10])])
        ultimate_rem = (ultimate_sum * 10 % 11
                        if ultimate_sum * 10 % 11 != 10
                        else 0)
        return ultimate_rem == int(self.cpf[-1])
