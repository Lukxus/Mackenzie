'''
1) Faça um programa que mostre um menu para o usuário escolher uma operação ou
sair do programa. Por exemplo:
Soma .................... +
Subtração ............. -
Multiplicação......... *
Divisão................... /
Sair ....................... 0
O programa deve reconhecer a opção escolhida pelo usuário e solicitar a entrada de
dois números caso a opção escolhida seja uma das operações. Depois de fazer a
operação e mostrar o resultado o programa deve continuar em execução para que
o usuário faça selecione operação e outros números.
O programa só terminará caso o usuário digite 0
'''

def operation_Choice():
    print('+:soma ; -:subtração: ; *:multiplicação ; /:divisão')
    user_Choice=input("Qual operação deseja realizar? ")
    while user_Choice not in "+-*/":
        print('Operação inválida!!!!')
        user_Choice=input("Qual operação deseja realizar? ")
    if user_Choice=='+':
        return '+'
    elif user_Choice=='-':
        return '-'
    elif user_Choice=='*':
        return '*'
    elif user_Choice=='/':
        return '/'


def user_Numbers():
    numbers_Choice_One=(input("Qual é o primeiro número que você quer usar? ")).strip()
    while numbers_Choice_One=='' or numbers_Choice_One.isnumeric()==False:
        print('Valor inválido!!!!')
        numbers_Choice_One=(input("Qual é o primeiro número que você quer usar? ")).strip()
    numbers_Choice_Two=(input("Qual é o segundo número que você quer usar? ")).strip()
    while numbers_Choice_Two=='' or numbers_Choice_Two.isnumeric()==False:
        print('Valor inválido!!!!')
        numbers_Choice_One=(input("Qual é o segundo número que você quer usar? ")).strip()
    return float(numbers_Choice_One),float(numbers_Choice_Two)


print('BEM VINDO À CALCULADORA DO LUIZ')

while True:
    keep=None
    number_One,number_Two =user_Numbers()
    operation= operation_Choice()
    if operation=='+':
        print('\nA soma resultou em', number_One+number_Two)
    elif operation=='-':
        print('\nA subtração resultou em', number_One-number_Two)
    elif operation=='*':
        print('\nA multiplicação resultou em', number_One*number_Two)
    elif operation=='/':
        print('\nA divisão resultou em', number_One/number_Two)
    keep=input("\nVocê deseja fazer outra operação? [S/N]").strip().upper()
    while keep not in 'SN':
        keep=input("\nVocê deseja fazer outra operação? [S/N]").strip().upper()
    if keep=='N':
        break


