import numpy as np
from scipy.stats import entropy


class EntropyCalculator:
    '''
    Clase para calcular la entropía de Shannon en cada canal de una imagen RGB.
    '''

    @staticmethod
    def calculate(image: np.ndarray) -> dict:
        '''
        Calcula la entropía por canal (R, G, B).

        :param image: Imagen como arreglo NumPy en formato RGB.
        :return: Diccionario con entropía por canal.
        '''
        entropies = {}
        canales = ['R', 'G', 'B']

        for i, canal in enumerate(canales):
            datos = image[:, :, i].flatten()
            hist, _ = np.histogram(datos, bins=256, range=(0, 256), density=True)
            entropies[canal] = entropy(hist, base=2)

        return entropies
