import re

def remove(cpf):
    return re.sub(r'[^a-zA-Z0-9\s]', '', cpf)

while True:
    cpf = input("Digite o CPF para validação: ")
    cpf_limpo = remove(cpf)

    if cpf_limpo.isdigit():
        if len(cpf_limpo) == 11:
            break
        else:
            print("O CPF não está completo")
            continue
    else:
        print("digite apenas números: ")

cpf = cpf_limpo
num = [int(cpf[i]) for i in range(11)]

soma1 = sum(num[i] * (i+1) for i in range(9))
digito1 = soma1 % 11
if digito1 == 10:
    num10 = 0

if digito1 != num[9]:
    print("CPF inválido!")
 
soma2 = sum(num[i] * i for i in range(10))
digito2 = soma2 % 11
if digito2 == 10:
    digito2 = 0

if digito2 != num[10]:
    print("CPF inválido!")
else:
    print("CPF válido!")