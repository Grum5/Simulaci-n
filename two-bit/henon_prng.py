'''
    Generador de numeros pseudoaleatorios
    Elaborado con el mapa de Hénon
'''
import os
from typing import override


class Henon:

    def __init__(self, a: float, b: float, x0: float, y0: float):
        ''' Constructor '''

        # Parametros de entrada para el modelo
        self._a = a
        self._b = b
        self._x0 = x0
        self._y0 = y0

        # Arrays donde se almacenaran los datos del modelo
        self.x_array, self.y_array = [], []

    def get_pseudonumber(self) -> tuple:
        ''' Generación de un numero pseudoaleatorio '''

        x1 = round(1 - self._a * pow(self._x0, 2) + self._y0, 9)
        y1 = round(self._b * self._x0, 9)

        self._x0, self._y0 = x1, y1

        # Store the data in the array
        self.x_array.append(x1)
        self.y_array.append(y1)

        return x1, y1


class HenonBitSteam(Henon):
    '''
        Clase hija del mapa de Hénon
        * Genera y almacena numeros pseudoaleatorios en un formato binario
    '''

    def __init__(
        self,
        a: float,
        b: float,
        x0: float,
        y0: float,
        filename: str = 'binary.txt',
        dir_name: str = 'henon_output',
        iterations: int = 100,
    ) -> None:
        ''' Constructor '''

        # Llamar al constructor Padre
        super().__init__(a, b, x0, y0)

        # Declarar atributos de la clase
        self.filename = filename
        self.filedir = dir_name
        self.iterations = iterations

        # Crear una lista vacia para la cadena de binarios
        self.binary_str = []

        # Generar los archivos del modelo
        self.__run_model()

    @staticmethod
    def float_to_binary(number: float, bits: int = 32) -> str:
        '''
            Metodo estatico para usarlo sin instanciarlo de ser necesario
            Convierte un número entero a una representación binaria
        '''

        number = abs(number)
        number = int(number * 1e9)

        binary_str = bin(number)[2:].zfill(bits)

        return binary_str

    @staticmethod
    def write_file(filename: str, data: list) -> None:
        '''
            Metodo estatico para usarlo sin instanciarlo de ser necesario
            Escribir la serie de binarios en un archivo de texto
        '''

        # Abrir el archivo como file
        with open(filename, 'w') as file:

            # Iterar cada elemento de la lista
            for binary in data:

                # Escribir el binario y dar salto de linea
                file.write(binary + '\n')

            # Cerrar el archivo ya editado
            file.close()

        # Mostrar en pantalla una confirmacion de la creacion del archivo
        print(f'Archivo {filename} creado exitosamente\n')

    @override
    def get_pseudonumber(self) -> tuple:
        ''' Generación de un numero pseudoaleatorio '''

        x1 = round(1 - self._a * pow(self._x0, 2) + self._y0, 9)
        y1 = round(self._b * self._x0, 9)

        self._x0, self._y0 = x1, y1

        # Store the data in the array
        self.x_array.append(x1)
        self.y_array.append(y1)

        return x1, y1

    def check_for_filedir(self) -> None:
        ''' Metodo para verificar/crear el directorio de salida'''

        # Verificar si existe el directorio
        if not os.path.exists(self.filedir):

            # Crear el directorio
            os.makedirs(self.filedir)

            # Mostrar en la CLI que se creo el directorio
            print(f'Directorio creado: {self.filedir}')

    def __run_model(self) -> None:
        ''' Metodo que corre el modelo '''

        # Verificar si existe el directorio para almacenar los datos
        self.check_for_filedir()

        # Iterar n cantidad de veces para generar los numeros pseudoaleatorios
        for index in range(self.iterations):

            # Almacenar los numeros pseudoaleatorios
            x, _ = self.get_pseudonumber()

            # Convertir en formato binario el numero pseudoaleatorio
            self.binary_str.append(self.float_to_binary(x))

        # Guardar el path donde se guardara el archivo
        filepath = self.filedir + '/' + self.filename

        # Crear el archivo en el path
        self.write_file(filename=filepath, data=self.binary_str)
