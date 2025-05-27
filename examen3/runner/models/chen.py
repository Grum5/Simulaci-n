
class Chen:
    '''
        Clase para la generación de numeros pseudoaleatorios,
        mediante el mapa de Chen

    '''

    def __init__(self, a: float, b: float, x0: float, y0: float) -> None:
        ''' Constructor '''

        # Parametros de entrada para el modelo
        self._a = a
        self._b = b
        self._x0 = x0
        self._y0 = y0

        # Listas donde se almacenaran los datos del modelo
        self.x_array, self.y_array = [], []

    def get_pseudonumber(self) -> tuple[float, float]:
        ''' Generación de un numero pseudoaleatorio '''

        x1 = 1 - self._a * (pow(self._x0, 2) + pow(self._y0, 2))
        y1 = -2 * self._a * self._b * self._x0 * self._y0

        self._x0, self._y0 = x1, y1

        # Almacenamos los datos en la lista
        self.x_array.append(x1)
        self.y_array.append(y1)

        return x1, y1
