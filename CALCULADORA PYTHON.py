# Programa CALCULADORA com if-elif-else
# 10/03/2026

op = input('Digite: \n 1- Soma; \n 2- Subtração; \n 3- Multiplicação; \n 4- Divisão; \n 5- Potenciação; \n 6- Radiciação. \n Digite sua resposta: ')
op = int(op)

x = input('Digite o primeiro número: ')
x = int(x)

y = input('Digite o segundo número: ')
y = int(y)

if (op == 1):
    print('A soma dos números é: ', x + y)
    
elif (op == 2):
    print('A subtração dos números é: ', x - y)
    
elif (op == 3):
    print('A multiplicação dos números é: ', x * y)
    
elif (op == 4):
    print('A divisão dos números é: ', x / y)
    
elif (op == 5):
    print('A potenciação dos números é: ', x ** y)
    
elif (op == 6):
    print('A radiciação dos números é: ', x ** (1 / y))
    
else:
    print('nenhuma opção existente selecionada') 
    
input() 