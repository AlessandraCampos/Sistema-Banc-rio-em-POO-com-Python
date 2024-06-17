
from abc import ABC


class Transacao():
   
    def __init__(self, valor):
        self.valor = valor
        return int(self.valor)

class Saque(Transacao):
      def __init__(self, valor):
        super().__init__(valor)
        return valor - 10
    

    

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        return valor - 10



c = Saque(150)

print(c)