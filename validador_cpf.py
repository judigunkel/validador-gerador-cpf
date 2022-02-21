print('~' * 40)
print('VALIDADOR DE CPF'.center(40))
print('~' * 40)
print('Digite abaixo o CPF para verificação:\n'
      '\033[1;37m--- Para sair digite 0 ---\033[m')

while True:
    print()
    cpf = input('CPF: ').replace('.', '').replace('-', '').replace(' ', '')
    if cpf == '0':
        print('\033[33mEncerrando o programa...\033[m')
        break

    if len(cpf) < 11:
        print('\033[33mValor inválido. Tente novamente\033[m')
        continue

    if cpf.isnumeric():
        teste_cpf = cpf[0:9]
        soma = 0
        multi = 10  # multi é o fator de multiplicação

        for index in range(19):
            if index > 8:  # se o index for = 9, ele volta a ser zero, para não
                # dar erro, pois inicialmente "teste_cpf" tem somente 9 digitos
                index -= 9

            soma += int(teste_cpf[index]) * multi  # somando todas as
            # multiplicações para gerar o próximo dígito
            multi -= 1

            if multi < 2:  # quando o fator de multiplicação for 2,
                # acrescentamos o dígito encontrado e iniciamos novamente a
                # multiplicação, dessa vez, nosso multi vale 11 e a soma é
                # zerada
                multi = 11
                d = 11 - (soma % 11)
                if d > 9:
                    d = 0
                teste_cpf += str(d)  # acrescentando o dígito encontrado no
                # nosso teste de cpf
                soma = 0
        sequencia = teste_cpf == str(cpf[0]) * 11  # verificando se o cpf
        # digitado é uma sequência

        if cpf == teste_cpf and not sequencia:
            print('\033[1;32mCPF válido\033[m')
        else:
            print('\033[1;31mCPF inválido\033[m')
    else:
        print('\033[33mDigite apenas números\033[m')
