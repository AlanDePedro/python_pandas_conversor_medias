import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# leer el archivo excel
df = pd.read_excel("muebles_medidas.xlsx")

# añadir una columna al DataFrame que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["pulgadas"] = df["centímetros"].apply(cm_a_pulgadas)

# Prueba de diagnóstico: verifica si el DataFrame se actualizó
print("Columna de pulgadas añadida.")

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print(
    "conversión completada y guardada en un nuevo archivo llamado 'mueble_medidas_convertidas.xlsx'"
)
