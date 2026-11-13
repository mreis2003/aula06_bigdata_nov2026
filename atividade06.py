total_arrecadado = 0.0
for venda in range(1, 6):
    valor_compra = float(input(f"\nDigite o valor da {venda}ª compra: R$ "))

    if valor_compra >= 200.00:
        desconto = valor_compra * 0.10

        valor_compra =< 200.00:
        desconto = valor_compra * 0
        
        valor_final = valor_compra - desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}")

    else:
        valor_final = valor_compra
        print("Sem desconto aplicado.")
        
        print(f"Valor final da compra: R$ {valor_final:.2f}")
                   
     total_arrecadado = valor_final
      