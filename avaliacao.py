avaliação = list()
print("avaliação de satisfação de usuários : considerações ao filme que assistiu")

for i in range (1, 6):
	avaliação.append(int(input("  digite 1 para regular,  2 para bom e 3 para ótimo:  ")))

bom = 0
otimo = 0
regular = 0

for resposta in avaliação:
	if resposta == 1:
		regular = regular + 1
	if resposta == 2:
		bom = bom +1
	if resposta == 3:
		otimo = otimo +1

print (" resultado regular foi:  %d" % regular)
print (" resultado bom foi:  %d" % bom)
print (" resultado otimo foi:  %d" % otimo)
print ("agradecemos sua opinião , vote sempre...")
