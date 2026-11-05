import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Crearemos nuestra tabla y la guardaremos con pandas
# tenemos 6 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkedin', 7277, False, 2012]
# Creamos una lista de listas (conformando la tabla)
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]
# Utilizar pandas para organizar la tabla (DataFrame o Marco de Datos)
df_redes_sociales = pd.DataFrame(lista_redes_sociales, columns=["Nombre", "Cantidad", "Es_FB", "Año"])
print(df_redes_sociales)
# Creamos el archivo CSV y lo guardamos
df_redes_sociales.to_csv("redessociales.csv", index=False)
# 1. Gráfica de líneas
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Grafica redes sociales 0120")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# 2. Gráfica de puntos
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"], 'o')
plt.title("Gráfica de redes sociales 0120")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# 3. Gráfica de barras
plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Redes sociales 0120")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# 4. Gráfica de barras ordenada de manera descendente (con colores)
df_rs_ordenar = df_redes_sociales.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"], 
    color=["b", "g", "c", "m", "y", "r"])
plt.title("Redes sociales ordenadas de mayor a menor")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()

#Grafica de pastel
# plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()