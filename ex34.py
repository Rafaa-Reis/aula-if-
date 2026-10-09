saldo = float(input("Digite seu saldo: "))
valor_compra = float(input("Informe o valor da compra: "))
if saldo >= valor_compra:
    confirmaçao = input("Deseja confirmar a compra?: ")
    if confirmaçao == "sim":
        print("Compra permitida")
    else:
        print("Compra não permitida")
else:
    print("Saldo insuficiente")
    