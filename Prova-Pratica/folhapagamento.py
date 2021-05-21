from movimentofolha import MovimentoFolha


class FolhaPagamento:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano
        self.totalDescontos = 0
        self.totalProventos = 0
        self.movimentos = []


    def inserirMovimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.movimentos.append(movimento)

    def calcularFolha(self):
        colaboradores = [self.movimentos[0].retornaColaborador()]
        for x in self.movimentos:
            if x.retornaColaborador().retornaCodigo() not in [colaborador.retornaCodigo() for colaborador in colaboradores]:
                colaboradores.append(x.retornaColaborador())
            if x.retornaTipo() == "P":
                self.totalProventos += x.retornaValor()
            else:
                self.totalDescontos += x.retornaValor()

            x.retornaColaborador().inserirMovimentos(x)

        salarios = 0
        for i in colaboradores:
            salarios += i.retornaSalario()

        total = float((salarios + self.totalProventos) - self.totalDescontos)
        saida = f'Total Salários: {salarios:}\nTotal Proventos: {self.totalProventos:}\n'\
               f'Total Descontos: {self.totalDescontos:<10f}\n'\
               f'Valor Total a Pagar: {total}'
        return saida
