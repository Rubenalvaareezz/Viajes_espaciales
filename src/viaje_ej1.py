distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")

#Eso depende de la manera en la que escribamos las lineas del programa, cuando usamos una única / nos sale el resultado en números decimales, en cambio cuando utilizamos // el resultado solo sale en el número entero más cercano.