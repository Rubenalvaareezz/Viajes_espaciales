KM_AUTONOMIA = 150000
distancia_km = int(input("Introduzca la distancia en kms: "))

'''Alternativa 1'''
contador = 0
for parada in range (KM_AUTONOMIA, distancia_km+1, KM_AUTONOMIA): #El rango es abierto, es decir, [4,5) por eso se pone +1, si no no se llegaría al uno
    print(f"parada en el km {parada}")
    contador +=1
print(f"Número total de paradas para repostar: {contador}")


#SOLUCIÓN ALTERNATIVA2
''' 
while km_parada < distancia:
    print(f"parada ene el km {km_parada}")
    paradas +=1
    km_parada += KM_AUTONOMIA
'''