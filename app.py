import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

# URL de la página web de donde vamos a hacer scraping
url = 'https://easylaptopec.com/catalogo/eaci/'

def obtener_datos():
    # Realizamos la solicitud HTTP GET
    response = requests.get(url)

    # Verificamos que la solicitud fue exitosa
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ejemplo: extraer todos los nombres de los productos
        productos = soup.find_all('div', class_='product-name')
        
        # Crear una lista con los nombres de los productos
        datos = []
        for producto in productos:
            nombre = producto.get_text(strip=True)
            datos.append(nombre)
        
        return datos
    else:
        return []

@app.route('/api/productos', methods=['GET'])
def get_productos():
    datos = obtener_datos()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
