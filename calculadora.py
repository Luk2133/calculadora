def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero!"
    else:
        return x / y
    

print("Selecione a operacao:")

print("1. Adicao")

print("2. Subtracao")

print("3. Multiplicacao")

print("4. Divisao")

opcao = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número de sua escolha: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("O Resultado da adição é", adicao(num1, num2))
elif opcao == '2':
    print("O Resultado da substração é", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado da multiplicação é", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado da divisão é", divisao(num1, num2))
else:
    print("Opção indisponível")