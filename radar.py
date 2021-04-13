from random import randrange
#simulando o radar
velociade = randrange(60, 120, 10)

print(f"Numero gerado: {velociade}")

if velociade > 80:
    multa = (velociade - 80) * 7
    print("MULTADO!")
    print(f"O carro passou a {velociade}Km/h")
    print(f"O valor da multa é R${multa}")
else:
    print("Velocidade OK")
