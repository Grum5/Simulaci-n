
import math


class SerialTest:

    def __init__(self, filename: str):
        ''' Constructor '''

        # Open the file with the binary data
        with open(filename, 'r') as file:

            # Read the file and save the data
            self.binary_data = file.read().replace('\n', '')

            # Close the file
            file.close()

    def monobit_test(self) -> bool:

        # Process the data in variables
        n1 = self.binary_data.count('1')
        n0 = self.binary_data.count('0')
        n = len(self.binary_data)

        Sabs = abs(n1 - n0) / math.sqrt(n)

        Pvalue = abs(Sabs) / math.sqrt(2)

        # Display the results on the screen
        print("- MONOBIT TEST -------------------------------------------")
        print(f"Total de bits analizados (n): {n}")
        print(f"Número de 1s (n1): {n1}")
        print(f"Número de 0s (n0): {n0}")
        print(f"Estadístico S: {Sabs}\n")
        print("- RESULTADOS ---------------------------------------------")

        # Evaluate the results and display if its a pseudonumber or not
        if Pvalue > 0.01:
            print("La serie SI es pseudoaletoria")
            return True
        else:
            print("La serie NO es pseudoaletoria")
            return False

    def twobit_test(self) -> bool:

        n = len(self.binary_data)

        n0 = self.binary_data.count('0')
        n1 = self.binary_data.count('1')

        n00 = self.binary_data.count('00')
        n01 = self.binary_data.count('01')
        n10 = self.binary_data.count('10')
        n11 = self.binary_data.count('11')

        x2 = (4 / (n - 1)) * (n00**2 + n01**2 + n10**2 + n11**2) - (2 / n) * (n0**2 + n1**2) + 1

        umbral = 5.9915

        print("\n- SERIAL TEST (Two-Bit Test) -----------------------------")
        print(f"Longitud de la secuencia (n): {n}")
        print(f"Conteo de bits: n0={n0}, n1={n1}")
        print(f"Conteo de pares de bits: n00={n00}, n01={n01}, n10={n10}, n11={n11}")
        print(f"Estadístico X² calculado: {x2:.4f}")
        print(f"Umbral para α=0.05: {umbral}\n")
        print("- RESULTADOS ---------------------------------------------")

        if x2 < umbral:
            print("La serie SI es pseudoaleatoria.")
            return True
        else:
            print("La serie NO es pseudoaleatoria.")
            return False
