# ==============================
# SISTEMA DE EXERCÍCIOS EM PYTHON
# ==============================

# 1. Verificação de votação
def verificar_voto():
    idade = int(input("Qual a sua idade? "))
    if idade >= 16:
        print("Você já pode votar!")
    else:
        print("Você ainda não tem idade para votar.")

# 2. Positivo, negativo ou zero
def verificar_numero():
    n = int(input("Digite um número: "))
    if n > 0:
        print("Número positivo")
    elif n < 0:
        print("Número negativo")
    else:
        print("Número zero")

# 3. Desconto
def calcular_desconto():
    valor = float(input("Valor da compra: "))
    if valor > 100:
        valor *= 0.9
        print(f"Valor com desconto: R$ {valor:.2f}")
    else:
        print("Sem desconto")

# 4. Sistema de notas
def sistema_notas():
    nota = float(input("Digite a nota: "))
    if nota >= 9:
        print("Aprovado com excelência")
    elif nota >= 7:
        print("Aprovado")
    elif nota >= 4:
        print("Recuperação")
    else:
        print("Reprovado")

# 5. Par ou ímpar
def par_ou_impar():
    n = int(input("Digite um número: "))
    print("Par" if n % 2 == 0 else "Ímpar")

# 6. IMC
def calcular_imc():
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}")

# Menu principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Votação")
        print("2 - Número")
        print("3 - Desconto")
        print("4 - Notas")
        print("5 - Par/Ímpar")
        print("6 - IMC")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            verificar_voto()
        elif op == "2":
            verificar_numero()
        elif op == "3":
            calcular_desconto()
        elif op == "4":
            sistema_notas()
        elif op == "5":
            par_ou_impar()
        elif op == "6":
            calcular_imc()
        elif op == "0":
            break
        else:
            print("Opção inválida")

menu()