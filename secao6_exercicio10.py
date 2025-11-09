#entrada
idade = int(input("Insira sua idade: "))
#processamento
if 5 <= idade <= 7:
	print("Infantil A")
elif 8 <= idade <= 11:
	print("Infantil B")
elif 12 <= idade <= 13:
	print("Juvenil A")
elif 14<= idade <= 17:
	print("Juvenil B")
else:
	print("Adulto")