def oi():
    print("oi")
# oi()



def mostrar_disciplina(nome_disciplina):
    print(nome_disciplina)

# mostrar_disciplina("Banco de dados")



def mostrar_disciplina(nome, curso): #recebendo argumentos/parametros
    print(f"Disciplina, {nome}! Do curso {curso}.")

    # disciplina = input("informe a disciplina")
    # mostrar_disciplina, "TADS"
# mostrar_disciplina("Banco de dados", "TADS")




def somar(val1, val2): #val1 e val2 só existem dentro da função
    resultado = val1 + val2 #variável local
    print(resultado)

# valor1 = input("informe o primeiro valor")
# valor2 = input("informe o segundo valor")
# somar(int(valor1), int(valor2))



def realizar_prova(tentativas=3, tempo=30):
    print(f"Foram: {tentativas} tentativas no tempo de {tempo} minutos")

# realizar_prova() #não passei parâmetro
# realizar_prova(2)
# realizar_prova(5, 120)



# def calcular_dobro(n):
#     return n + 2 #return devolve algo para quem chamar a função

def calcular_dobro(n:int) -> int:
    return n +2

resultado = calcular_dobro(7)
print(f"O dobro é: {resultado}")

