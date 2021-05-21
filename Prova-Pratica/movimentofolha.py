

class MovimentoFolha:
    def __init__(self, colaborador, descricao, valor, tipo):
        self.colaborador = colaborador
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo

    def retornaColaborador(self):
        return self.colaborador

    def retornaValor(self):
        return self.valor

    def retornaTipo(self):
        return self.tipo
