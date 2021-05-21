from colaborador import Colaborador
from movimentofolha import MovimentoFolha
from folhapagamento import FolhaPagamento
import time


if __name__ == '__main__':
	# Construindo objeto da classe FolhaPagamento
	FP = FolhaPagamento(9, 2019)

	# Construindo objetos da classe Colaborador
	CL01 = Colaborador(100, "Manoel Claudino", "Av 13 de Maio 2081", "Benfica", "60020-060", "88671020", "124543556-89", 4500.00)
	CL02 = Colaborador(200, "Carmelina da Silva", "Avenida dos Expedicionários 1200", "Aeroporto", "60530-020", "3035-1280", "301789435-54", 2500.00)
	CL03 = Colaborador(300, "Gurmelina Castro Saraiva", "Av João Pessoa 1020", "Damas", "60330-090", "3235-1089", "350245632-76", 3000.00)

	# Construindo objetos da classe MovimentoFolha
	MF01 = MovimentoFolha(CL01, "Salario", 4500.00, "P")
	FP.inserirMovimentos(MF01)
	MF02 = MovimentoFolha(CL01, "Plano Saúde", 1000.00, "P")
	FP.inserirMovimentos(MF02)
	MF03 = MovimentoFolha(CL01, "Pensão", 600.00, "D")
	FP.inserirMovimentos(MF03)

	MF04 = MovimentoFolha(CL02, "Salario", 2500.00, "P")
	FP.inserirMovimentos(MF04)
	MF05 = MovimentoFolha(CL02, "Gratificação", 1000.00, "P")
	FP.inserirMovimentos(MF05)
	MF06 = MovimentoFolha(CL02, "Faltas", 600.00, "D")
	FP.inserirMovimentos(MF06)

	MF07 = MovimentoFolha(CL03, "Salario", 4500.00, "P")
	FP.inserirMovimentos(MF07)
	MF08 = MovimentoFolha(CL03, "Plano Saúde", 1000.00, "P")
	FP.inserirMovimentos(MF08)
	MF09 = MovimentoFolha(CL03, "Pensão", 600.00, "D")
	FP.inserirMovimentos(MF09)

	# Imprimindo resultados
	op = 0
	s = (FP.calcularFolha())
	while op != 5:
		time.sleep(1)
		print("O que você quer fazer?")
		time.sleep(0.5)
		print("1 - Ver Folha de Pagamento Funcionário 100")
		time.sleep(0.5)
		print("2 - Ver Ver Folha de Pagamento Funcionário 200")
		time.sleep(0.5)
		print("3 - Ver Folha de Pagamento Funcionário 300")
		time.sleep(0.5)
		print("4 - Ver Folha de Pagamento Geral da Empresa")
		time.sleep(0.5)
		print("5 - Sair")
		op = int(input())
		if op == 1:
			print()
			print("=" * 50)
			time.sleep(0.25)
			print(CL01.calcularSalario())
			time.sleep(0.5)
			print("-" * 50)
			time.sleep(0.25)
			print(s)
			time.sleep(0.25)
			print("=" * 50)
			print()
		elif op == 2:
			print()
			print("=" * 50)
			time.sleep(0.25)
			print(CL02.calcularSalario())
			time.sleep(0.5)
			print("-" * 50)
			time.sleep(0.25)
			print(s)
			time.sleep(0.25)
			print("=" * 50)
			print()
		elif op == 3:
			print()
			print("=" * 50)
			time.sleep(0.25)
			print(CL03.calcularSalario())
			time.sleep(0.5)
			print("-" * 50)
			time.sleep(0.25)
			print(s)
			time.sleep(0.25)
			print("=" * 50)
			print()
		elif op == 4:
			print()
			print("=" * 50)
			time.sleep(0.25)
			print(CL01.calcularSalario())
			time.sleep(0.5)
			print()
			print(CL02.calcularSalario())
			time.sleep(0.5)
			print()
			print(CL03.calcularSalario())
			print("-" * 50)
			print(s)
			time.sleep(0.25)
			print("=" * 50)
			print()
