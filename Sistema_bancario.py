menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saque = 0
deposito = 0
saldo = 500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("deposite")
        deposito = float(input())
        saldo += deposito


    elif opcao == "s":
        print("digite o valor do saque:")
        saque = float(input())
        numero_saques +1
        if saque > limite:
            print("valor inválido, não se pode sacar mais que R$500,00")
            break
        elif numero_saques == LIMITE_SAQUES:   
            print("Você não pode mais sacar, limite de 3 saques por dia")
            break
        elif saldo < saque:
            print("Não há saldo suficiente")
            break
        else:
            saldo -= saque
            print("Saque realizado com sucesso")
            extrato += f"{saque:.2f}\n"


    
    elif opcao == "e":
        if extrato == 0:
            print("Não houveram movimentações na conta")
            print(saldo)
        else:
            print("seu extrato é: ", extrato)
    
    elif opcao == "q":
        print("sair")
        break
    
    else:
        print("Opção digitada inválida")
