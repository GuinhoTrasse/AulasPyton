notas = [0.0, 0.0, 0.0, 0.0]
quantidade_alunos = 4

for i in range(quantidade_alunos):
    notas[i] = float(input(f"Informe a nota do aluno {i+ 1}: "))

soma_notas = 0.0
for i in range(quantidade_alunos):
    soma_notas += notas[i]

print(notas)
media_turma = soma_notas / quantidade_alunos
print(f"\nA média da turma foi: {media_turma:.2f}")

