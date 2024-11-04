import pandas as pd 

#dataframe es la informacion basica con el nombre de las piezas y centimetros para poder armar el excel

data = {
    "piezas:" : ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "centímetros" : [40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

#guardar el DataFrame en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)
