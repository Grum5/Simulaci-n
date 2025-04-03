from serial_test import SerialTest
from henon_prng import HenonBitSteam


if __name__ == '__main__':

    filename = "binary.txt"
    filepath = f"henon_output/{filename}"

    # Crea una instancia del generador de numeros pseudoaletorios
    prng = HenonBitSteam(a=1.4, b=0.3, x0=0.0, y0=0.0, iterations=1000)

    # Crear una instancia de los test
    tests = SerialTest(filepath)
    tests.monobit_test()
    tests.twobit_test()
