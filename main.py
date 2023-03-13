# Anio bisiesto
def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


print(es_bisiesto(2000))

inicio = 2000
fin = 3000
print(f"Imprimiendo años bisiestos del {inicio} al {fin}")
# Le sumamos uno al fin, porque range no incluye el límite superior
for anio in range(inicio, fin+1):
    if es_bisiesto(anio):
        print(anio, end=", ")