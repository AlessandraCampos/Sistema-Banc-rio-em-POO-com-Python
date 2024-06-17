class Cliente:
    
    def __init__(self, nome):
          self._nome= nome
                    
    def cadastrar(self,nome):
        lista =[]
        self._nome = nome
        dict = {}
        if self._nome not in dict:
            dict["nome"] = self._nome
            lista.append(dict)
            return f'O Cliente {self._nome} foi cadastrado com sucesso!'
        else:
            return f'Cliente {self._nome} já está cadastrado no sistema'
                
    
    def __str__(self) -> str:
     return f'O Cliente {self._nome} foi cadastrado com sucesso!'
    
    def consultar(self,nome):
        self._nome =nome
        return f'Cliente {self._nome} foi cadastrado com sucesso!'
        
c = Cliente("nomecliente")
c.cadastrar("nomecliente")
print(c)

