##Lista de exercícios - Funções

## 1.
def soma(a, b):
    resultado = a + b
    return  resultado

## 2.
def multiplicação(c, d):
    result = c * d
    return result

## 3.
def saudar(nome, mensagem= "Olá"):
    print(f"{mensagem}, {nome}!")

## 4.
def maior(a, b):
    if a >= b:
        print(a)
    else:
        print(b)
## 5.
def dividir(a, b):
    quociente = a // b
    resto = a % b
    print(quociente, resto)
## 6.
def par_impar(n):
    if n%2 == 0:
        return ("True")
    else:
        return("False")
## 7.
def teste():
    print("Olá")
    resultado = teste()
    return(resultado) #Exibira Olá e None

## 8.
def apresentar(nome, idade, cidade):
    return(f"{nome} tem {idade} anos e mora em {cidade}")

## 9.
#print(apresentar("Matheus", 18, "Colombo"))
#print(apresentar(cidade='colombo', idade=18, nome="Matheus"))

## 10.
#Retorno "Ana tem Curitiba anos e mora em 20"

## 11.
def saudacao(nome, periodo='dia'):
    return (f"{nome} no periodo: {periodo}")

## 12.
def saudacao2(nome, periodo='dia'):
    if periodo == "":
        periodo = "dia"
    print(f"Bom {periodo}, {nome}")

## 13.
#def exemplo(a=1, b): #a ordem, de fosse (a, b=1) daria certo
#    return a + b

## 14.
def somar_todos(*args):
    return (sum(args))
#print(saudacao2('Matheus'))

## 15.
def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
    return
## 16.
#Args somará todos os dados, Kwargs os juntara em uma lista

## 17.
#x = 10
#def teste():
#    x = 5
#    print(x)
#teste()
#print(x) # 5 e 10, primeiro o 5 da função dps o 10 pois print está como variavel global.

## 18.

def incrementar(c):
    contador = 0
    while contador <= c:
        print(contador)
        contador += 1

## 19.
def triplo(x):
    return (x*3)
operacao = triplo

## 20.
#print(operacao(5))

## 21.
#quadrado = lambda x:x ** 2
#print(quadrado(4))

## 22.
#numeros  = [1,2,3,4,5]
#dobrados = list(map(lambda x:x ** 2, numeros))
#print(dobrados)

## 23.
#numeros  = [1,2,3,4,5]
#pares = list(filter(lambda x: x % 2 == 0, numeros))
#print(pares)

##24.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

##25.
def contagem(x):
    print(f"Contagem regressiva...{x}...")
    if x == 0:
        return "Fim!"
    else:
        return contagem(x-1)

##26.
def erro(n):
    return n * erro(n - 1) #O comando não permite fim

##27.
# Exercício 27: Crie função media(lista) com docstring
def media(lista):
    """
    Calcula a média dos valores de uma lista.

    Parâmetros:
    lista (list): lista de números

    Retorna:
    float: média dos valores
    """
    return sum(lista) / len(lista)

##28.
# Exercício 28: Use help() para exibir a documentação
def media(lista):
    """
    Calcula a média dos valores de uma lista.

    Parâmetros:
    lista (list): lista de números

    Retorna:
    float: média dos valores
    """
    return sum(lista) / len(lista)
help(media)

##29.
# Exercício 29: Crie calculadora(a, b, operacao)
def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida"

##30
# Exercício 30: Crie processar_dados(*args, **kwargs)
def processar_dados(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)