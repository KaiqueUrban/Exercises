#variavel
contador = 100
#processamento
while contador <200:
	contador += 1
	if contador %2 == 0:
		continue
	else:
		print(f"O número {contador} é impar")