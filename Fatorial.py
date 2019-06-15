numero = int(input('Digite um numero: '))
controle = int
resultado = int


def CalcularFatorial(numero):
    controle = numero
    resultado = numero

    while (controle >= 2):
        controle = controle - 1
        print(f'{resultado} x {controle} = {resultado * controle}')
        resultado = resultado * controle

    return resultado


CalcularFatorial(numero)



