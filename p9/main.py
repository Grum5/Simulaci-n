
from runner.serial_test import SerialTest
from runner.prng import Prng


if __name__ == '__main__':

    # Crear instancia de generador de numeros pseudoaletorios
    random = Prng()

    # Crear las instancias de los modelos caoticos (Tinkerbell, Henon, Chen)
    random.create_tinkerbell(0.9, -0.6013, 2.0, 0.50, 0.1, 0.1)
    random.create_henon(1.4, 0.3, 0.1, 0.3)
    # random.create_chen(2.0, 0.5, 0.1, 0.1)

    # Crear los archivos binarios
    random.create_data()

    modelos = {
        "Henon": ".prng_metadata/henon.txt",
        # "Chen": ".prng_metadata/chen.txt",
        "Tinkerbell": ".prng_metadata/tinkerbell.txt"
    }

    resultados = {}

    for nombre, archivo in modelos.items():
        test = SerialTest(archivo)
        # x1 = test.monobit_test()
        # x2 = test.twobit_test()
        # x3 = test.poker_test()
        # resultados[nombre] = (x1, x2, x3)
        x5 = test.autocorrelation_test()

        resultados[nombre] = x5

        print(f'X5 = {resultados[nombre]}')

        if abs(resultados[nombre]) > 1.96:
            print("La serie NO es pseudoaletoria (α=0.05)")
        else:
            print("La serie es pseudoaletoria (α=0.05)")
