import pandas as pd
import requests
from bs4 import BeautifulSoup
# Guardar el script completo en un archivo .py local
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://guvier.com/collections/anillos-compromiso-guvier"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
productos = texto.find_all("div", class_="inner")

datos = []
for item_div in productos:
  if not item_div.find("a", class_="product-link"):
        continue
  titulo_element = item_div.find("div", class_="product-block__title")
  titulo = titulo_element.text.strip() if titulo_element else "N/A"
  precio_element = item_div.find("span", class_="product-price__item")
    if precio_element:
        precio_texto = precio_element.text
        precio = float(precio_texto.replace("$", "").replace(",", "").strip())
    else:
        precio = None
  color_container = item_div.find("div", class_="product-block-options__inner")
  color_element = None
  if color_container:
      color_element = color_container.find("span", class_="product-block-options__item__text")

  color = color_element.text.strip() if color_element else "N/A"

  datos.append({
      "titulo": titulo,
      "precio_mxn": precio,
      "color": color
    })
df = pd.DataFrame(datos)
df.to_csv("catalogo_productos.csv", index=False)
print("Scraping exitoso y archivo catalogo_productos.csv creado.")
"""
with open("productos.py", "w", encoding="utf-8") as f:
    f.write(script_code)
