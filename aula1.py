# p rodar o codigo: shift + f10
var1 = 50
var2 = 10
var3 = 'oi'

print(var1)
print(var2)
print(var1 + var2)

print('olá, mundo')
print(456)
print(100,55)
print('oi',5)
print(10+3)

conta = var1 * var2
print(conta)

# usa-se '#' pra fazer comentarios

def faz_conta():
    return 0
print(faz_conta())

# def e uma declaraçao de funçao, ela cria uma o funçao
# return vai retornar o valor q vc especificou anteriormente: usa se isso p naop ter q repetir a mesma funçao varias vezes

def oi():
    print ('oi')

oi()

# o ideal é sempre declarar as funçoes do nosso codigo

def soma_dois_valores(valor1, valor2):
   return valor1 + valor2

x = soma_dois_valores(3,4)
print(x)
x = soma_dois_valores(1,2)
print(x)

def raiz_quadrada(valor):
    return valor**(1/2)
# p fazer raiz de algo precisa de **

y = raiz_quadrada(4)
print(y)
y = raiz_quadrada(53)
print(y)

def raiz(valor3, valor4):
    return  valor3**(1/valor4)

z = raiz(25, 2)
print(z)


def e_par(valor):
    return (valor % 2) == 0
print(e_par(2))
print(e_par(5))


def div_por_seis(valor):
    return ((valor % 2 )-- 0 and (valor % 3) == 0)


def testes():
    print(div_por_seis(7))
    print(div_por_seis(9))
    print(div_por_seis(12))
    x = soma_dois_valores(3,4)
    print(x)

def testa_par():
    # le um valor inserido pelo usuario, verifica se o valor e par e retorna uma mensagem
    parada = False
    while parada == False:
        valor = input('Insira um valor numérico, ou aperte ENTER para encerrar ...\n')
        if valor == '':
            parada = True
        else:
            if e_par(int(valor)) == True:
                print('O valor inserido é par.')
            else:
                print('O valor inserido é ímpar.')
# int significa q o valor e inteiro

testa_par()

def dez_mult_tres():
    #imprimen os primeiros 10 numeros nao negativos de 3
    cont = 0
    numero = 1
    while cont < 10:
        if numero % 3 == 0:
            print(numero)
            cont = cont + 1
        numero += 1   # mesma coisa q numero = numero + 1



dez_mult_tres()

