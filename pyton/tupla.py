#Tupla - Lista imutável
# igual criar lista, só muda os [] para ()

# numeros = (100, 50) #mais utilizada
# # numeros = "100", "50"
# print(numeros[0])
# print(numeros[1])




# tupla = ("r")
# print(type(tupla))

# tupla1 = ("r",) #tem que ter a vírgula no final para entender que é uma tupla
# print(type(tupla1))




# t = tuple() #criando uma tupla vazia
# print(t)

# t = tuple("Rogério")
# print(t)




# numeros = (100, 50)
# print("Valores originais")
# for numero in numeros:
#     print(numero)

# print("Valores alterados")
# numeros = (300, 800)
# for numero in numeros:
#     print(numero)




# if (0, 1, 2) < (0, 3, 4):
#     print(True)
# else:
#     print(False)


# if (0, 1, 2000000) < (0, 3, 4):
#     print(True)
# else:
#     print(False)




# email = "guilherme.dias4@estudante.ifms.edu.br"
# nomeusuario, dominio = email.split('@')
# print(nomeusuario)
# print(dominio)



# txt = "Algorítmos é a matéria mais fácil do curso"
# palavras = txt.split()
# lista = list()
# for palavra in palavras:
#     lista.append((len(palavra), palavra))

# print(lista)

# lista.sort(reverse=True)
# res = list()
# for tamanho, palavra in lista:
#     res.append(palavra)
#     print(res)
#     print(tamanho)


# exemplo = ('primeira', 'aula')
# (x, y) = exemplo

# print(x)
# print(y)


x = 20
y = 70

x, y = y, x
print(x, y)