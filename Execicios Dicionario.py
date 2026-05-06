##Exercicio 1 Dicionarios

#dic = dict(Nome = "Matheus", Idade = 18, Cidade = "Colombo")
#x = str(input("Digite a chave para o valor desejado(Nome, Idade, Cidade): "))
#print(dic.get(x))

##Exercicio 2

#dic = {"produto1": 5, "produto2": 10, "produto3":20}
#P = str(input("Digite o produto a ser alterado(produto1, produto2, produto3): "))
#V = float(input("Digite o novo valor do produto: "))
#dic2 = {P:V}
#dic.update(dic2)
#print(dic)

##Exercicio 3

#dic = {}
#chave = input("Digite a Chave a ser adicionada: ")
#valor = input("Digite o Valor da Chave equivalente: ")
#dic[chave] = valor
#print(dic)

##Exercicio 4

#chaves = []
#valores = []
#for i in range(3):
#    chave = str(input(f"Digite a {i+1}º Chave a ser adicionada: "))
#    valor = str(input("Digite o Valor da Chave equivalente: "))
#    chaves.append(chave)
#    valores.append(valor)
#dic = dict(zip(chaves, valores))
#print(dic)

##Exercicio 5

#dic = dict(Arcano= "Torre", Nome= "Matheus", idade= 18)
#print(dic)
#resp = str(input("\nDeseja apagar o Dicionario?(S/N) "))
#if resp == "S":
#    dic.clear()
#    print(dic)
#else:
#    print("Ok!")

##Exercicio 6

#dic = dict(Nome="Matheus", Idade=18, Cidade="Colombo")
#ic2 = dic.copy()
#dic2["Curso"]= "Eng. Software"
#dic2["Idade"]= 20
#print(dic)
#print(dic2)

##Exercicio 7

#Nomes = str(input("Digite os nomes(separe por virgula): "))
#lnomes = [nome.strip() for nome in Nomes.split(",")]
#dic = dict.fromkeys(lnomes, 0)
#print(dic)

##Exercicio 8

#dic = dict(Matheus=10, Arthur=7, Marcos=8, Cesar=9)
#x = str(input("Digite o nome do aluno escolhido: "))
#print(dic.get(x, "Aluno não identificado"))

##Exercicio 9

#dic = dict(produto1=5, produto2=10, produto3=15, produto4=20)
#print(dic.items())
#print(dic.keys())
#print(dic.values())

##Exercicio 10

#dic = {"Matheus": 10, "Arthur": 7, "Marcos": 8, "Cesar": 9}
#cha = str(input("Digite uma Chave a ser removida(Matheus, Arthur, Marcos, Cesar): "))
#dic.pop(cha)
#dic.popitem()
#print(dic)
#Nchaves = input('Digite as Chaves a serem adicionadas (separe por virgula): ')
#Chaves = [chave.strip() for chave in Nchaves.split(",") ]
#Nvalores = input('Digite os Valores das chaves (separe por virgula): ')
#Valores = [valor.strip() for valor in Nvalores.split(",") ]
#Ndic = dict(zip(Chaves, Valores))
#dic.update(Ndic)
#print(dic)

##Exercicio 11

dic = {"Matheus": 18, "Arthur": 23, "Marcos": 40, "Cesar": 9}
print("==============================")
print("SISTEMA DE EXERCÍCIOS EM PYTHON")
print("==============================")
#1. verificação keys
def verificar_nome():
    print(dic.keys())
#2. Idade
def verificar_idade():
    print(dic.values())
#3. Items
def verificar_itens():
    print(dic.items())
#4. Buscar aluno
def buscar_aluno():
    nome = input("Digite o nome do aluno: ")
    if nome in dic:
        print(dic.get(nome))
    else:
        print("Aluno não encontrado!")
#5  Adicionar aluno
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    dic[nome] = idade
    print(dic)
#6. Atualizar idade
def atualizar_idade():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a nova idade do aluno: "))
    dic [nome] = idade
    print(dic)
#7. Remover aluno especifico
def remover_aluno():
    nome = input("Digite o nome do aluno: ")
    dic.pop(nome)
    print(dic)
#8. Remover ultimo aluno
def remover_ultimo():
    dic.popitem()
    print(dic)
#9  Copiando o dicionario
def copiar_dic():
    dic2 = dic.copy()
    print(dic2)
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a nova idade do aluno: "))
    dic2[nome] = idade
    print(dic2)
    print(dic)
#10 Novos usuarios
def novos_usuarios():
    Nomes = str(input("Digite os nomes(separe por virgula): "))
    lnomes = [nome.strip() for nome in Nomes.split(",")]
    idade = int(input("Digite a idade padrão: "))
    dic = dict.fromkeys(lnomes, idade)
    print(dic)
#11 Atualizando principal
def atualizando_principal():
    print("Dicionário atual:")
    print(dic)
    novo_dic = {}
    qtd = int(input("\nQuantos itens deseja adicionar? "))
    for i in range(qtd):
        chave = input(f"Digite a chave {i + 1}: ")
        valor = input(f"Digite o valor da chave {chave}: ")
        novo_dic[chave] = valor
    dic.update(novo_dic)
    print("\nDicionário atualizado:")
    print(dic)
#12 Apagando o dicionario
def apagando_dic():
    resp = str(input("\nDeseja apagar o Dicionario?(S/N) "))
    if resp == "S":
        dic.clear()
        print(dic)
    else:
        print("Ok!")
#13 Atualizando Tuplas
def atualizando_tuplas():
    Mchaves = input('Digite as Chaves a serem adicionadas (separe por virgula): ')
    chaves = [chave.strip() for chave in Mchaves.split(",") ]
    Lvalores = input('Digite os Valores das chaves (separe por virgula): ')
    fValores = [valor.strip() for valor in Lvalores.split(",") ]
    dic2 = dict(zip(chaves, fValores))
    print(dic2)
#14 Menu
def menu():
    while True:
        print("1 - Verificar chaves")
        print("2 - Verificar idade")
        print("3 - Verificar itens")
        print("4 - Buscar aluno")
        print("5 - Adicionar aluno")
        print("6 - Atualizar idade")
        print("7 - Remover aluno")
        print("8 - Remover ultimo aluno")
        print("9 - Copiando o dicionario")
        print("10 - Novos usuarios")
        print("11 - Atualizando principal")
        print("12 - Apagando o dicionario")
        print("13 - Atualizando Tuplas")
        print("0 - Sair")
        op = input("Escolha: ")
        if op == "1":
            verificar_nome()
        elif op == "2":
            verificar_idade()
        elif op == "3":
            verificar_itens()
        elif op == "4":
            buscar_aluno()
        elif op == "5":
            adicionar_aluno()
        elif op == "6":
            atualizar_idade()
        elif op == "7":
            remover_aluno()
        elif op == "8":
            remover_ultimo()
        elif op == "9":
            copiar_dic()
        elif op == "10":
            novos_usuarios()
        elif op == "11":
            atualizando_principal()
        elif op == "12":
            apagando_dic()
        elif op == "13":
            atualizando_tuplas()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida")

menu()