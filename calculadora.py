opcao = ""
historico = []


def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Você precisa digitar um número válido!")


def obter_operacao():
    while True:
        operacao = input("Digite a operação (+, -, *, /): ").strip()

        if operacao in ["+", "-", "*", "/"]:
            return operacao

        print("Você precisa digitar uma operação válida!")


def fazer_calculo(primeiro_numero, operacao, segundo_numero):
    if operacao == "+":
        return primeiro_numero + segundo_numero
    elif operacao == "-":
        return primeiro_numero - segundo_numero
    elif operacao == "*":
        return primeiro_numero * segundo_numero
    elif operacao == "/":
        if segundo_numero != 0:
            return primeiro_numero / segundo_numero
        else:
            raise ValueError("Não pode dividir por 0")


def formatar_numero(numero):
    if numero.is_integer():
        return int(numero)
    else:
        return numero


def fazer_operacao():
    while True:
        primeiro_numero = obter_numero("Digite o primeiro número: ")
        operacao = obter_operacao()
        segundo_numero = obter_numero("Digite o segundo número")

        try:
            resultado = fazer_calculo(
                primeiro_numero,
                operacao,
                segundo_numero
            )
        except ValueError as e:
            print("Erro:", e)
            continue

        resultado = formatar_numero(resultado)

        return primeiro_numero, operacao, segundo_numero, resultado


def ver_historico(historico):
    if historico:
        print("---Histórico de cálculos:---")
        contador = 1

        for item in historico:
            print(f"{contador} - {item}")
            contador += 1
    else:
        print("O histórico está vazio.")

    print("----------------------------")
    input("Pressione Enter para continuar...")


def limpar_historico(historico):
    if historico:
        historico.clear()
        print("O histórico foi limpo com sucesso.")
    else:
        print("O histórico já está vazio.")


while opcao != "3":

    print("1 - Fazer um cálculo")
    print("2 - Ver histórico de cálculos")
    print("3 - Sair")
    print("4 - Limpar histórico de cálculos")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        primeiro_numero, operacao, segundo_numero, resultado = fazer_operacao()

        calculo = f"{primeiro_numero} {operacao} {segundo_numero} = {resultado}"
        print("Resultado: ", resultado)
        historico.append(calculo)

    elif opcao == "2":
        ver_historico(historico)

    elif opcao == "3":
        print("Saindo da calculadora...")
        break

    elif opcao == "4":
        limpar_historico(historico)




