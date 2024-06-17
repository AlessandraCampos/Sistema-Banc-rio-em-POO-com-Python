class Conta:
    def __init__(self, saldo = 0):
        self._saldo = saldo
    def __str__(self) -> str:
        return f'Seu saldo é de {self._saldo}'

class ContaCorrente(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)


class ContaPoupanca(Conta):
    def __init__(self,saldo):
        super().__init__(saldo)



c = ContaCorrente(150)
print(c)

