
class Logistico:
    '''
        Clase para la generación de numeros pseudoaleatorios,
        mediante el logistico (Mapa logistico).
    '''

    def __init__(self, r1: float, r2: float, x0: float, y0: float) -> None:
        ''' Constructor '''

        self._r1 = r1
        self._r2 = r2
        self._x = x0
        self._y = y0

        # Lista donde se almacenaran los datos del modelo
        self.x_array, self.y_array = [], []

    def get_pseudonumber(self) -> tuple[int, int]:
        ''' Generación de un numero pseudoaleatorio '''

        self._x = self._r1 * self._x * (1 - self._x)
        self._y = self._r2 * self._y * (1 - self._y)

        self.x_array.append(self._x)
        self.y_array.append(self._y)

        return self._x, self._y
