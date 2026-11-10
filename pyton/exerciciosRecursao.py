# Exercício 1: Soma Recursiva de Lista

# Escreva uma função recursiva que receba uma lista de números inteiros e retorne a soma de todos os seus elementos sem utilizar o comando 'sum()' nem laços 'for/while'.

def somaDeLista(lista):
    if len(lista) == 0:
        return lista
    return lista + somaDeLista(lista.pop())

resultado = somaDeLista([1,2,3])
print(f"Soma da lista [1,2,3] = {resultado}")