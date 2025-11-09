#variavel
contador = 0
#processamento
while contador <100:
	print(f"O valor do contador é: {contador}")
	contador += 1
	if contador %10 == 0:
		print(f"{contador} é multiplo de 10")