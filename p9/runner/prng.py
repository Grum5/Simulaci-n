
# Importando los generadores de modelos caoticos
from runner.models.tinkerbell import Tinkerbell
from runner.models.henon import Henon
from runner.models.chen import Chen

# Importando librerias necesarias
# import math
import os


class Prng:
    '''
        Clase para generar numeros pseudoaletorios.
        Utiliza 3 diferentes modelos caoticos.
            1. Mapa de Henon.
            2. Mapa de Chen.
            3. Mapa de Tinkerbell.

        Tambien almacena los valores generados en un directorio oculto
        (.prng_metadata)".
        para cada modelo caotico, siempre y cuando este exista
    '''

    def __init__(self) -> None:
        ''' Constructor '''

        # Crea las instancias para los modelos
        self.henon = None
        self.chen = None
        self.tinkerbell = None

        # Nombre de los archivo binarios
        self.__binary_files = {
            'henon': 'henon.txt',
            'chen': 'chen.txt',
            'tinkerbell': 'tinkerbell.txt',
        }

        # Crear un directorio para almacenar los datos binarios
        self._metadata_dir_name = ".prng_metadata"
        self._metadata_dir()

    def create_data(self, iterations: int = 2000) -> str:
        '''
            Metodo para crear los archivos .txt con los binarios
            de los modelos caoticos.
            Recibe como parametro la catidad de iteraciones
            que se generaran en numeros binarios (por defecto 2000)
        '''

        # Si existe al menos un modelo crear los binarios
        if self.henon or self.chen or self.tinkerbell:

            if self.henon:

                # Lista con los binarios generados
                henon_binary_str = []

                # Generar n cantidad de numeros pseudoaletorios
                for _ in range(iterations):

                    # Generar dos numeros pseudoaletorios
                    x, y = self.henon.get_pseudonumber()

                    # Convertir en formato binario
                    henon_binary_str.append(self.float_to_binary(x))

                # Guardar el path donde se guardara el archivo
                filepath = (
                    f'{self._metadata_dir_name}/'
                    f'{self.__binary_files["henon"]}'
                )

                # Crear el archivo en el directorio designado
                self.write_file(filepath, henon_binary_str)

            if self.chen:

                # Lista con los binarios generados
                chen_binary_str = []

                # Generar n cantidad de numeros pseudoaletorios
                for _ in range(iterations):

                    # Generar dos numeros pseudoaletorios
                    x, y = self.chen.get_pseudonumber()

                    # Convertir en formato binario
                    chen_binary_str.append(self.float_to_binary(x))

                # Guardar el path donde se guardara el archivo
                filepath = (
                    f'{self._metadata_dir_name}/'
                    f'{self.__binary_files["chen"]}'
                )

                # Crear el archivo en el directorio designado
                self.write_file(filepath, chen_binary_str)

            if self.tinkerbell:

                # Lista con los binarios generados
                tinkerbell_binary_str = []

                # Generar n cantidad de numeros pseudoaletorios
                for _ in range(iterations):

                    # Generar dos numeros pseudoaletorios
                    x, y = self.tinkerbell.get_pseudonumber()

                    # Convertir en formato binario
                    tinkerbell_binary_str.append(self.float_to_binary(x))

                # Guardar el path donde se guardara el archivo
                filepath = (
                    f'{self._metadata_dir_name}/'
                    f'{self.__binary_files["tinkerbell"]}'
                )

                # Crear el archivo en el directorio designado
                self.write_file(filepath, tinkerbell_binary_str)

    def _metadata_dir(self) -> None:
        '''
            Metodo protegido para crear un directorio que almacene
            la información generada por la clase misma
        '''

        # Intentar crear el directorio
        try:
            # Verificar que exista el directorio
            if not os.path.exists(self._metadata_dir_name):

                # Crear el directorio
                os.makedirs(self._metadata_dir_name)

        # En caso de fallar tirar un except
        except Exception as e:
            print("Error generando un directorio para almacenar los binarios:")
            print(e)

    @staticmethod
    def float_to_binary(number: float, bits: int = 32) -> str:
        '''
            Metodo estatico para usarlo sin instanciarlo de ser necesario
            Convierte un número entero a una representacioón binaria
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

    def create_tinkerbell(
            self,
            a: float,
            b: float,
            c: float,
            d: float,
            x0: float,
            y0: float
    ) -> None:
        ''' Crea la instancia del mapa de Tinkerbell'''

        self.tinkerbell = Tinkerbell(a, b, c, d, x0, y0)

    def create_henon(self, a: float, b: float, x0: float, y0: float) -> None:
        ''' Crea la instancia del mapa de Henon '''

        self.henon = Henon(a, b, x0, y0)

    def create_chen(self, a: float, b: float, x0: float, y0: float) -> None:
        ''' Crea la instancia del mapa de Chen '''

        self.chen = Chen(a, b, x0, y0)
