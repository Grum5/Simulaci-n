
class Tinkerbell:
    '''
        Clase para la generación de numeros pseudoaleatorios,
        mediante el mapa de Tinkerbell
    '''

    def __init__(
            self,
            a: float,
            b: float,
            c: float,
            d: float,
            x0: float,
            y0: float
    ) -> None:
        ''' Constructor '''

        # Parametros de entrada para el modelo
        self._a, self._b = a, b
        self._c, self._d = c, d
        self._x0, self._y0 = x0, y0

        # Listas donde se almacenaran los datos del modelo
        self.x_array, self.y_array = [], []

    def get_pseudonumber(self) -> tuple:
        ''' Generación de un numero pseudoaleatorio '''

        pow2x = pow(self._x0, 2)    # x0^2
        pow2y = pow(self._y0, 2)    # y0^2

        x1 = pow2x - pow2y + (self._a * self._x0) + (self._b * self._y0)

        product2xy = 2 * self._x0 * self._y0  # 2 * x0 * y0

        y1 = product2xy + (self._c * self._x0) + (self._d * self._y0)

        self._x0, self._y0 = x1, y1

        # Almacenamos los datos en una lista
        self.x_array.append(x1)
        self.y_array.append(y1)

        return x1, y1
