import pandas as pd
import matplotlib.pyplot as plt

#Cargar el archivo
df = pd.read_csv("data/players_data-2026_2027.csv")

#ver columnas y primeras filas
#print(df.columns.tolist())
#print(df.head())

# Número de equipos únicos en la temporada
print(f"Equipos únicos en la temporada: {df['Squad'].nunique()}")

#Agrupar por equipo y calcular estadísticas
ataque_equipos = df.groupby("Squad")[["Gls","Sh","SoT","Ast"]].sum()

#Ordenar por goles
ataque_equipos = ataque_equipos.sort_values(by="Gls", ascending=False)

# efectividad de tiro por equipo
ataque_equipos["Efectividad_Tiro"] = ataque_equipos["Gls"] / ataque_equipos["Sh"]

# Redondear a 3 decimales
ataque_equipos ["Efectividad_Tiro"] = ataque_equipos ["Efectividad_Tiro"].round(3)

# ordenar por efectividad de tiro
print("Ranking efectividad de tiro:")
print(ataque_equipos.sort_values(by="Efectividad_Tiro", ascending=False))

#Grafico
# Tomar los 10 equipos con más goles
top10 = ataque_equipos.head(10)

plt.figure(figsize=(10,6))
plt.barh(top10.index, top10["Gls"], color='steelblue')
plt.xlabel("Goles")
plt.ylabel("Equipos")
plt.title("Top 10 Equipos con más Goles en la Temporada 2026/2027")
plt.gca().invert_yaxis()  # Primer equipo queda arriba
plt.tight_layout()


plt.show()