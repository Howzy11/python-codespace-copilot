#CONCATENACAO
valor1 = input("Insira o primeiro valor: ")
valor2 = input("Insira o segundo valor: ")

concatenacao = valor1 + " " + valor2

print("Sua concatenação é igual a: ", concatenacao)

#STRING + INTEIRO
string = input("Insira o primeiro valor: ")
num = int(input("Insira o valor inteiro: "))

resultado = (string + " ") * num

print(resultado)

#CALCULADORA
valor1 = int(input("Insira o primeiro valor inteiro: "))
valor2 = int(input("Insira o segundo valor inteiro: "))
operacao = input("Insira o operador: ")

if(operacao == '+'):
    print(valor1 + valor2)
    elif(operacao == '-'):
        print(valor1 - valor2)
    elif(operacao == '*'):
        print(valor1 * valor2)
    elif(operacao == '/'):
        print(valor1 / valor2)
    else:
        print("Operação inválida!")