# 1 – Crie um programa que ajude um professor a analisar o desempenho de uma turma. 
# O programa deve pedir ao usuário o nome e a nota de vários alunos. O programa para de 
# pedir dados quando o usuário digitar "sair" no nome. Essas notas devem ser salvas em 
# uma lista. 
# Em seguida crie uma função chamada calcular_estatisticas(lista_notas) que recebe a 
# lista de notas e retorne: 
# A média aritmética da turma. 
# A maior e a menor nota (sem usar as funções prontas max() e min()). 
# Crie uma função chamada exibir_ranking(lista_notas) que ordene as notas de forma 
# decrescente (do maior para o menor) e exiba o resultado na tela.

nota = []
nome = []
num_alunos = 0
som_notas = 0

while True:
    print("Digite os nomes e notas dos alunos, digite 'sair' para encerrar o programa \n")
   
    nomeAlunos = str(input("Digite o nome do aluno: \n"))
    nome.append(nomeAlunos)
    if nomeAlunos != "sair":
        num_alunos += 1
    if nomeAlunos == "sair":
        break
    notaAlunos = float(input("Digite a nota do aluno: \n"))
    nota.append(notaAlunos)
    som_notas += notaAlunos
    
nome.remove("sair")

def calcular_estatisticas():
    lista_notas = som_notas / num_alunos

print(nota)
print(nome)
calcular_estatisticas(lista_notas)