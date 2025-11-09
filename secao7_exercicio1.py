#entrada
numero = int(input("Insira um número: "))
maior = numero
#processamento
while numero > 0:
	numero = int(input("Insira um novo número: "))
	if numero > maior:
		maior = numero
		print(f"{numero}")
		if numero == 0:
			break
	