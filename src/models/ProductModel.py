from databases.db import get_connection
from .entities.Product import Product

class ProductModel:


# Para llamar al metodo sin necesidad de instanciar la clase
    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT Id, nombre, categoria, fecha_expiracion, cantidad FROM product ORDER BY nombre ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    product = Product(row[0], row[1], row[2], row[3], row[4])
                    products.append(product.to_json())
            # Cerrar la conexión después de trabajar con ella
            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)
        
# Metodo get por Id         
    @classmethod
    def get_product(self, Id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT Id, nombre, categoria, fecha_expiracion, cantidad FROM product WHERE Id=%s",(Id,))
                resultset = cursor.fetchone()
                if resultset is not None:
                    product = Product(resultset[0], resultset[1], resultset[2], resultset[3], resultset[4])
                    connection.close()
                    return product
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

# Metodo post (create)          
    @classmethod
    def add_product(self, product):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO product (Id, nombre, categoria, fecha_expiracion, cantidad) VALUES (%s, %s, %s, %s, %s)",
                            (product.Id, product.nombre, product.categoria, product.fecha_expiracion, product.cantidad))
                affected_rows = cursor.rowcount
                connection.commit()
            # Cerrar la conexión después de trabajar con ella
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
