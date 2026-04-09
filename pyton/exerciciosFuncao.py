# 1. Faça uma função que não receba parâmetros e escreva na tela (print) o texto “OI”.
# 2. Faça uma função que receba um texto por parâmetro e escreva-o na tela (print).
# 3. Faça uma função que receba um texto por parâmetro e escreva-o na tela (print), em 
# seguida retorne “Ok”.
# 4. Faça um procedimento que recebe por parâmetro os valores necessários para o 
# cálculo da fórmula de báskara e imprima as suas raízes, caso seja possível calcular.
# 5. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito 
# quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 
# 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar o valor inteiro 1 para 
# verdadeiro e 0 caso contrário


# Exercício 1
# def oi():
#     print("Oi")

# oi()



# Exercício 2
# def mostrar_nome(nome):
#     print(f"Seu nome é {nome}, que nome FODA!")

# nomeReal=input("Informe o seu nome VERDADEIRO!")
# mostrar_nome(nomeReal)



# Exercício 3
# def mostrar_nome(nome):
#     print(f"Seu nome é {nome}, que nome FODA!")
#     print("Ok")

# nomeReal=input("Informe o seu nome VERDADEIRO!")
# mostrar_nome(nomeReal)



# Exercício 4
# import math

# def baskara(a, b, c):
#     # 1. Calculamos o Delta (discriminante) primeiro
#     delta = (b**2) - (4*a*c)
    
#     # 2. Verificamos se é possível calcular as raízes reais
#     if delta < 0:
#         print("A equação não possui raízes reais (Delta negativo).")
#     elif a == 0:
#         print("O valor de 'a' não pode ser zero em uma equação de segundo grau.")
#     else:
#         # 3. Calculamos as duas raízes corretamente
#         raiz_delta = math.sqrt(delta)
        
#         x = (-b + raiz_delta) / (2 * a)
#         y = (-b - raiz_delta) / (2 * a) # Aqui usamos o sinal de menos
        
#         print(f"1 raiz: {x}")
#         print(f"2 raiz: {y}")

# Entrada de dados
# a = int(input("Digite o valor de a: "))
# b = int(input("Digite o valor de b: "))
# c = int(input("Digite o valor de c: "))

# baskara(a, b, c)




def verificar():
    numero = float(input("Informe o número"))
    n = numero
    soma = 0

    while n > 0:
        n -= 1
        if numero%2 == 0:
            soma += n

    if soma == numero:
        return 1
    else:
        return 0

resultado = verificar()






# def estatisticas_básicas(valores):
#     menor = min(valores)
#     maior = max(valores)
#     return menor, maior

# minimo, maximo = estatisticas_básicas({4, 1, 7, 20})
# print(f"O mínimo é {minimo} e o máximo é {maximo}")



# funções da math + pyton
# funçoes de string + pyton