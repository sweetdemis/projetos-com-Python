import random

num1p = random.randint(0, 9)
num2p = random.randint(0, 9)
num3p = random.randint(0, 9)
num4p = random.randint(0, 9)
num5p = random.randint(0, 9)
num6p = random.randint(0, 9)
num7p = random.randint(0, 9)
num8p = random.randint(0, 9)
num9p = ""
num10p = ""
num11p = ""

regiao = input("digite o estado em que você nasceu: ").strip().lower()

if regiao == "distrito federal" or regiao == "tocantins" or \
    regiao == "goias" or regiao == "mato grosso" or \
    regiao == "mato grosso do sul":
    num9p = 1
elif regiao == "pará" or regiao == "amazonas" or regiao == "acre" \
    or regiao == "amapá" or regiao == "rondonia" or regiao == "roraima":
    num9p = 2
elif regiao == "ceará" or regiao == "maranhao" or regiao == "piaui":
    num9p = 3
elif regiao == "pernambuco" or regiao == "rio grande do norte" or \
      regiao == "paraiba" or regiao == "alagoas":
    num9p = 4
elif regiao == "bahia" or regiao == "sergipe":
    num9p = 5
elif regiao == "minas gerais":
    num9p = 6
elif regiao == "rio de janeiro" or regiao == "espirito santo":
    num9p = 7
elif regiao == "sao paulo":
    num9p = 8
elif regiao == "santa catarina" or regiao == "parana":
    num9p = 9
elif regiao == "rio grande do sul":
    num9p = 0
else:
    print("dado inválido")

num1 = num1p*1
num2 = num2p*2
num3 = num3p*3
num4 = num4p*4
num5 = num5p*5
num6 = num6p*6
num7 = num7p*7
num8 = num8p*8
num9 = num9p*9

soma1 = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9)
soma1 = soma1 % 11
if soma1 == 10:
    num10p = 0
else:
    num10p = soma1

num10p = int(str(num10p)[0])

num1 = num1p*0
num2 = num2p*1
num3 = num3p*2
num4 = num4p*3
num5 = num5p*4
num6 = num6p*5
num7 = num7p*6
num8 = num8p*7
num9 = num9*8
num10 = num10p*9

soma2 = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10)
soma2 = soma2 % 11
if soma2 == 10:
    num1p1 = 0
else:
    num11p = soma2

num11p = int(str(num11p)[0])

cpf = (f"{num1p}{num2p}{num3p}.{num4p}{num5p}{num6p}.{num7p}{num8p}{num9p}-{num10p}{num11p}")
print(cpf)
