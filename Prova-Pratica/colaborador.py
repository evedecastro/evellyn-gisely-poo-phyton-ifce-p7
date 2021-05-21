from movimentofolha import MovimentoFolha


class Colaborador:
    def __init__(self, codigo, nome, endereco, bairro, cep, telefone, cpf, salarioatual):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.bairro = bairro
        self.cep = cep
        self.telefone = telefone
        self.cpf = cpf
        self.salarioAtual = salarioatual
        self.movimentos = []

    def retornaCodigo(self):
        return self.codigo

    def retornaSalario(self):
        return self.salarioAtual

    def calcularSalario(self):
        proventos = 0
        descontos = 0
        for x in self.movimentos:
            if x.retornaTipo() == "P":
                proventos += x.retornaValor()
            else:
                descontos += x.retornaValor()

        valorliq = float((self.salarioAtual + proventos) - descontos)

        text = f'Código: {self.codigo:<12d} |Nome: {self.nome:}\n'\
               f'Salário: {self.salarioAtual:}\nProventos: {proventos:}\nDescontos: {descontos:}\n'\
               f'Valor Liquido: {valorliq}'
        return text

    def inserirMovimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.movimentos.append(movimento)
