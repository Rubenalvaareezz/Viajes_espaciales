distancia_km = int(input("Introduce la distancia en km:"))  
velocidad_kmh = int(input("Introduce la velocidad en km/h: "))

tiempo_horas  = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas//24
semanas = tiempo_dias // 7

print(f"Tardarias {semanas} semanas y {tiempo_horas} horas , yendo en una velocidad de {velocidad_kmh} km/h a una distancia de {distancia_km} km")
