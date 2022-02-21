from random import randint
from time import sleep

print('~' * 40)
print('GERADOR DE CPF'.center(40))
print('~' * 40)
sleep(1)
while True:
    cpf = str(randint(000000000, 999999999))
    if cpf == str(cpf[0]) * 11:
        continue
    soma = 0
    multi = 10
    for index in range(19):
        if index > 8:
            index -= 9

        soma += int(cpf[index]) * multi
        multi -= 1

        if multi < 2:
            multi = 11
            d = 11 - (soma % 11)
            if d > 9:
                d = 0
            cpf += str(d)
            soma = 0
    print('O CPF gerado foi: \033[35m', end='')
    for i, c in enumerate(cpf):
        sleep(0.5)
        if i == 2 or i == 5:
            print(c, end='.')
        elif i == 8:
            print(c, end='-')
        else:
            print(c, end='')
    break
