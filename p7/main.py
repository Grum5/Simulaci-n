
from runner.serial_test import SerialTest
from runner.prng import Prng


def imprimir_tabla_resultados(resultados):
    print("Modelo Caótico   -     Monobit   -   Two-bit         -      Poker test")
    print("                 -  umbral≈1.821 -   umbral≈5.991    -   umbral∈[1.03,57.4]")
    print("_________________________________________________________________________________")

    for modelo, valores in resultados.items():
        x1, x2, x3 = valores
        print(f"{modelo:<20}X1 = {x1:<12.4f}X2 = {x2:<12.4f}X3 = {x3:<.4f}")


if __name__ == '__main__':

    # Crear instancia de generador de numeros pseudoaletorios
    random = Prng()

    # Crear las instancias de los modelos caoticos (Tinkerbell, Henon, Chen)
    random.create_tinkerbell(0.9, -0.6013, 2.0, 0.50, 0.1, 0.1)
    random.create_henon(1.4, 0.3, 0.1, 0.3)
    random.create_chen(2.0, 0.5, 0.1, 0.1)

    # Crear los archivos binarios
    random.create_data()

    modelos = {
        "Henon": ".prng_metadata/henon.txt",
        "Chen": ".prng_metadata/chen.txt",
        "Tinkerbell": ".prng_metadata/tinkerbell.txt"
    }

    resultados = {}

    for nombre, archivo in modelos.items():
        test = SerialTest(archivo)
        x1 = test.monobit_test()
        x2 = test.twobit_test()
        x3 = test.poker_test()
        resultados[nombre] = (x1, x2, x3)

    imprimir_tabla_resultados(resultados)
