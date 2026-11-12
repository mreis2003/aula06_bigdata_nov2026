venda = float(input('valor de venda: '))

match venda:
    case venda if venda < 100:
        print('venda pequena')
    case venda if venda < 500:
        print('venda média')
    case _:
        print('venda grande')


