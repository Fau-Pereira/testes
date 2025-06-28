print("Bem-Vindo ao Sistema de Notas do Aluno")

aluno = input("Digite o nome do aluno: ")
print("O nome do aluno é:", aluno)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média do aluno", aluno, "é:", media)
if media >= 7:
    print("O aluno", aluno, "está aprovado.")
elif media >= 3 and media < 7:
    print("O aluno", aluno, "está realizará a AV5.")
else:
    print("O aluno", aluno, "está reprovado.")
