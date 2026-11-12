# Tenta ler e converter os dados para número
valor = float(input("Digite o valor do ingresso: R$ "))

print("\nEscolha o tipo de entrada:")
print("1 - Inteira (sem desconto)")
print("2 - Meia entrada (50% de desconto)")
print("3 - Promoção (30% de desconto)")

opcao = int(input("Digite a opção desejada: "))

# Estrutura match/case para calcular o desconto

desconto = 0
opcao = int(input('informe a opção: '))

match opcao:
    
    case 1:
        print('sem desconto: ')

    case 2:
        print('desconto 50%: ')
        desconto = valor * 0.50

    case 3:
        print('desconto 30%: ')
        desconto = valor * 0.30

   
    case _:
        operacao = False
        print('opção invalida')
        
if opcao in [1, 2, 3]:
    valor_final = valor - desconto
    print(f'valor a pagar R$ {valor_final}')
else:
    print('Digiti uma das opções acima')


# if desconto != 0:



        

