# app.py
from flask import Flask
from config import Config
from routes import Product

app = Flask(__name__)
app.config.from_object(Config)

# Método para las páginas no encontradas
def page_not_found(error):
    return "<h1>Not Found Page</h1>", 404

# Registro del Blueprint para asignar rutas
app.register_blueprint(Product.main, url_prefix='/api/products')

# Manejador de errores
app.register_error_handler(404, page_not_found)

if __name__ == '__main__':
    app.run(debug=True)
