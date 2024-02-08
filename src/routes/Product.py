from flask import Blueprint, jsonify, request
import uuid
# Entities
from models.entities.Product import Product
# Models
from models.ProductModel import ProductModel

main = Blueprint('product_blueprint', __name__)

@main.route('/get')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Para get con id
@main.route('/<Id>')
def get_product(Id):
    try: 
        product = ProductModel.get_product(Id)
        if product != None:
            return jsonify(product.to_json())
        else:
            return jsonify({'message': 'El producto no existe'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Metodo post
@main.route('/add', methods=['POST'])
def add_product():
    try:
        product = request.get_json()
        if product!= None:
            product = Product(product['Id'], product['nombre'], product['categoria'], product['fecha_expiracion'], product['cantidad'])
            affected_rows = ProductModel.add_product(product)
            if affected_rows > 0:
                return jsonify({'message': 'El producto se ha añadido correctamente'}), 201
            else:
                return jsonify({'message': 'El producto no se ha añadido correctamente'}), 400
        else:
            return jsonify({'message': 'No se ha enviado el producto'}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
