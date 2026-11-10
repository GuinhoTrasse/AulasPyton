def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

resultado = fatorial(4)
print(f"4! = {resultado}")



def inverter_string(txt):
    # Caso Base: String vazia ou de 1 caractere
    if len(txt)<= 1:
        return txt

    # Passo Recursivo: ultimo + inverso do restante
    return txt[-1] + inverter_string(txt[:-1])
print(inverter_string("PYTHON"))

inverter_string("PYTHON")


def eh_palindromo(txt):
    txt = txt.lower().replace(" ","")
    if len(txt) <= 1:
        return True
    if txt[0] != txt[-1]:
        return False
    return eh_palindromo(txt[1:-1])

print(eh_palindromo("arara"))
print(eh_palindromo("python"))