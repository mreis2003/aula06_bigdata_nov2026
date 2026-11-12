# PIX oferece 12% de desconto:
# Débito oferece oferece 8%:
# crédito oferece 5%:
# Dinheiro oferece 15%:

valor = int(input('digitar o valor'))

print('''
[1] - PIX (12% de desconto)
[2] - DÉBITO (8% de Desconto)
[3] - CRÉDITO (5% de Desconto)
[4] - DINHEIRO (15% de Desconto)

''')

# operacao = True 
desconto = 0

opcao = int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
        print('---- PIX ----')
        desconto = valor * 0.12
        
    case 2: 
        print('---- DÉBITO----')
        desconto = valor * 0.08

    case 3:
        print('----DÉBITO----')
        desconto = valor * 0.05

    case 4:
        print('---- DINHEIRO ----')
        desconto = valor * 0.15

    case _:
        operação = False
        print('opção inválida')
         

if opcao in [1, 2, 3, 4 ]:
# if operacao  == True:
# if desconto != 0:
    valor_final = valor - desconto
    print(f'\npreço: {valor} ')
    print(f'Desconto: {desconto}')
    print(f'total a pagar: {valor_final}')

else: 
    print('favor escolha uma das opções acima')
