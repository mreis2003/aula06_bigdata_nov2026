num = float(input('Informe um número:'))

match num:
    case num if num > 0:
        print(f'{num} é positivo')
    case num if num < 0:
        print(f'{num} é Negativo')

    case _:
        print(f'{num} é Neutro')
