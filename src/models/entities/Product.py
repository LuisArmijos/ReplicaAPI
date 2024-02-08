from utils.DateFormat import DateFormat

class Product():

    def __init__(self, Id, nombre=None, categoria=None, fecha_expiracion=None, cantidad=None) -> None:
        # Estructura de la tabla
        self.Id = Id
        self.nombre = nombre
        self.categoria = categoria
        self.fecha_expiracion = fecha_expiracion
        self.cantidad = cantidad

    def to_json(self):
        # Convertir la fecha de expiración a una cadena en el formato 'dd-mm-yyyy'
        fecha_expiracion_str = self.fecha_expiracion.strftime('%d-%m-%Y')

        return {
            'Id': self.Id,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'fecha_expiracion': DateFormat.convert_date(fecha_expiracion_str),
            'cantidad': self.cantidad
        }
