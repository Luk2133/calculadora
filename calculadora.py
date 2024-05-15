
print("Selecione a operacao:")

print("1. Adicao")

print("2. Subtracao")

print("3. Multiplicacao")

print("4. Divisao")

opcao = int(input("Digite sua escolha (1/2/3/4): "))

num1 = float(input("Digite o primeiro número de sua escolha: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print("O Resultado da adição é:", num1 + num2)
elif opcao == 2:
    print("O Resultado da substração é:", num1 - num2)
elif opcao == 3:
    print("Resultado da multiplicação é:", num1 * num2)
elif opcao == 4:
    print("Resultado da divisão é:", num1 / num2)
else:
    print("Opção indisponível")