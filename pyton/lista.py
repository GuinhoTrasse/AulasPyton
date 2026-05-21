# notas = [0.0, 0.0, 0.0, 0.0,]
# quantidade_alunos = 4

# for i in range(quantidade_alunos):
#     notas[i] = float(input(f"Informe a nota do aluno {i + 1}: "))

# soma_notas = 0.0
# for i in range(quantidade_alunos):
#     soma_notas += notas[i]

# media_turma = soma_notas / quantidade_alunos
# print(f"\nA média da turma foi: {media_turma:.2f}")

# alunos_acima = 0
# for i in range(quantidade_alunos):
#     if notas[i] >= media_turma:
#         alunos_acima = alunos_acima + 1

# print(f"A quantidade de alunos na média ou acima da média é {alunos_acima}")

carrinho = []

print("--- Cadastro de Produtos (Digite 'sair' para encerrar) ---")

while True:
    produto = input("Informe o nome do produto: ")
    # .lower() passa tudo minusculo
    if produto.lower() == 'sair':
        break
    # append adiciona o item no fim da lista
    carrinho.append(produto)

print("\n--- Itens no seu Carrinho ---")
# len retorna o tamanho do objeto
tamanho_carrinho = len(carrinho)

for i in range(tamanho_carrinho):
    print(f"Posição [{i}] -> Produto: {carrinho[i]}")