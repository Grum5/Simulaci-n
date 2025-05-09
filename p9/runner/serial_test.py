
import math
from collections import Counter


class SerialTest:

    def __init__(self, filename: str):
        with open(filename, 'r') as file:
            self.binary_data = file.read().replace('\n', '')

    def monobit_test(self) -> float:
        n1 = self.binary_data.count('1')
        n0 = self.binary_data.count('0')
        n = len(self.binary_data)
        Sabs = abs(n1 - n0) / math.sqrt(n)
        return Sabs

    def twobit_test(self) -> float:
        n = len(self.binary_data)
        n0 = self.binary_data.count('0')
        n1 = self.binary_data.count('1')
        n00 = self.binary_data.count('00')
        n01 = self.binary_data.count('01')
        n10 = self.binary_data.count('10')
        n11 = self.binary_data.count('11')
        x2 = (4 / (n - 1)) * (n00**2 + n01**2 + n10**2 + n11**2) - (2 / n) * (n0**2 + n1**2) + 1
        return x2

    def poker_test(self, m: int = 4) -> float:
        blocks = []
        for i in range(0, len(self.binary_data), m):
            block = self.binary_data[i:i + m]
            blocks.append(block)
        if len(blocks[-1]) < m:
            blocks.pop()
        n = len(blocks)
        conteo = Counter(blocks)
        suma_fi2 = sum(f**2 for f in conteo.values())
        poker = ((16 / n) * suma_fi2) - n
        return poker

    def autocorrelation_test(self, d: int = 8) -> float:
        '''
            Aplica el test de autocorrelacion con desplazamiento d.

            Retorna el valor estadistico X5, el cual se compara con el umbral +-1.96
        '''

        n = len(self.binary_data)
        if not (1 < d < n // 2):
            raise ValueError(f'El valor de "d" debe estar entre 2 y {n // 2 - 1}')

        a_d = sum(int(self.binary_data[i]) ^ int(self.binary_data[i + d]) for i in range(n - d))
        x5 = 2 * (a_d - (n - d) / 2) / math.sqrt(n - d)
        return x5


