from pymongo import MongoClient 
from pymongo.errors import ConnectionFailure

class DatabaseManager:
    """
    Clase que gestiona operaciones en la base de datos MongoDB
    """

    def __init__(self, uri, db_name):
        """
        Construcutor de la clase.
        :param uri: URI de conexion a MongoDB
        :param db_name: Nombre de la base de datos
        """
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None
    
    def connect(self):
        """
        Metodo para establecer la conexion a la ase de datos
        """
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"conexion a la base de datos{self.db_name} establecida con exito.")
        except ConnectionFailure as e:
            print(f"Error al conectar a la base de datos:{e}")
            raise
    
    def disconnect(self):
        """
        Metodo para desconectar de la base de datos
        """
        if self.client:
            self.client.close()
            print(f"Desconectando de la base de datos")

    def insert(self, collection_name, data):
        """
        Metodo para reLizar una operacion de insercion en la base de datos.
        :param collection_name: Nombre de la coleccion en la que se realizara la insercion
        :param data: Datos a insertar en la coleccion.
        :return: ID del documento insertado.
        """
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id
    
    def select(self, collection_name, query, projection= None):
        """
        Metodo para realizar una operacion de seleccion en la base de datos.
        :param collection_name: Nombre de la coleccion en la que se realizara la seleccion.
        :param query: condiciones para la seleccion.
        :param projection: campos a seleccionar (por defecto, todos).
        :return:Documentos que coinciden con la consulta.
        """
        collection = self.db[collection_name]
        return collection. find(query, projection)
    
    def update(self, collection_name, query, update_data):
        """
        Método para realizar una operación de actualización en la base de datos.
        :param collection_name: Nombre de la colección en la que se realizará la actualización.
        :param query: Condiciones para la actualización.
        :param update_data: Datos a actualizar en la colección.
        :return: Resultado de la operación de actualización.
        """
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': update_data})
        return result.modified_count

    def delete(self, collection_name, query):
        """
        Método para realizar una operación de eliminación en la base de datos.
        :param collection_name: Nombre de la colección en la que se realizará la eliminación.
        :param query: Condiciones para la eliminación.
        :return: Resultado de la operación de eliminación.
        """
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count