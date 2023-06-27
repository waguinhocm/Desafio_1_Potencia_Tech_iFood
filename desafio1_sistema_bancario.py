conta_bancaria = "usuario DIO"

menu = """ 
Escolha a operação desejada:

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
=>
"""
extrato = f""" 
=========================EXTRATO=========================

Olá {conta_bancaria}! Muito obrigado por utilizar nossos serviços!

Movimentações do dia:

""" 
saldo_insuficiente = """
Não foi possível realizar a operação.

        Saldo Insuficiente
"""

saldo = 0
limite = 500
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if deposito < 0:
            print("Valor inválido")
        else:
            saldo += deposito
            extrato += f"- Efetuado deposito de R${deposito:.2f}\n"
            print("Operação realizada com sucesso.")
        
    elif opcao == "s":   
        if numero_saques <= LIMITE_SAQUES:
            print("Saque") 
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            if saque > 0:
                if saque <= saldo:
                    if saque <= limite:
                        saldo -= saque
                        extrato += f"- Efetuado saque de R${saque:.2f}\n"
                        numero_saques += 1
                        print("Operação realizada com sucesso.")

                    else:
                        print(f"O valor limite de cada saque é de R${limite:.2f}")
                    
                else:
                    print(saldo_insuficiente)

            else:
                print("Valor inválido")
                            
        else:
            print("Número de saques diários excedidos. Maiores informações pelo 0800 12345")
        
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo atual de R${saldo:.2f}")

    elif opcao == "q":
        print("""Muito obigado por utilizar nossos serviços!
        Tenha um ótimo dia!
        """)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")