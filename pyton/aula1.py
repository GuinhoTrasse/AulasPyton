# dia = input("Digite um dia da semana\n")
# match dia:
#     case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
#         print("Tem aula")
#     case "Sábado" | "Domingo":
#         print("Sem aula :D")
#     case _:
#         print("Fala um dia que exista, burro pra cacete!")



# numero = int(input("Digite um número inteiro qualquer\n"))

# match numero:
#     case n if n < 0:
#         print("Numero negativo")
#     case n if n % 2 == 0:
#         print(f"O número {numero} é par positivo")
#     case n:
#         print(f"{n} é um número impar positivo")


# ATIVIDADE 1 com if!
# idade = int(input("Digite a sua idade\n"))
# if idade >= 5 and idade < 8:
#     print("infantil")
# elif idade >= 8 and idade < 11:
#     print("jovenil")
# elif idade >= 11 and idade < 16:
#     print("Adolecente")
# elif idade >= 16 and idade < 31:
#     print("Adulto")
# elif idade >= 31:
#     print("Senhor")


# ATIVIDADE 1 com case!
# idade =int(input("Digite a sua idade\n"))
# match idade:
#     case n if n >= 5 and n < 8:
#         print("infantil")
#     case n if n >= 8 and n < 11:
#         print("jovenil")
#     case n if n >= 11 and n < 16:
#         print("Adolecente")
#     case n if n >= 16 and n < 31:
#         print("Adulto")
#     case n if n >= 31:
#         print("Senhor")

# ATIVIDADE 2 com if!
# codigo = int(input("Digite o codigo de origem do produto\n"))
# if codigo == 1:
#     print("Sul")
# elif codigo == 2:
#     print("Norte")
# elif codigo == 3:
#     print("Leste")
# elif codigo == 4:
#     print("Oeste")
# elif codigo == 5 or codigo == 6:
#     print("Nordeste")
# elif codigo >= 7 and codigo < 10:
#     print("sudeste")
# elif codigo >= 10 and codigo < 21:
#     print("Centro-Oeste")
# elif codigo >= 21 and codigo < 31:
#     print("Noroeste")
# else:
#     print("Código incorreto")

# ATIVIDADE 2 com case!
# codigo = int(input("Digite o número do código"))
# match codigo:
#     case n if n == 1:
#         print("Sul")
#     case n if n == 2:
#         print("Norte")
#     case n if n == 3:
#         print("Leste")
#     case n if n == 4:
#         print("Oeste")
#     case n if n == 5 or codigo == 6:
#         print("Nordeste")
#     case n if n >= 7 and n < 10:
#         print("sudeste")
#     case n if n >= 10 and n < 21:
#         print("Centro-Oeste")
#     case n if n >= 21 and n < 31:
#         print("Noroeste")
#     case _:
#         print("Código incorreto")