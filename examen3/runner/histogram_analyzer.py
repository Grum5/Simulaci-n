import numpy as np
import matplotlib.pyplot as plt
import os


class HistogramAnalyzer:
    '''
    Clase encargada de generar y guardar histogramas por canal (R, G, B)
    de una imagen cifrada.
    '''

    def __init__(self, output_dir: str = "resources/histograms"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_histograms(
            self,
            image: np.ndarray,
            name_prefix: str = "output"
    ) -> None:
        '''
            Genera y guarda los histogramas por canal RGB.

            :param image: imagen en formato numpy (RGB)
            :param name_prefix: prefijo para los nombres de los archivos guardados
        '''

        canales = ['R', 'G', 'B']
        colores = ['red', 'green', 'blue']

        for i, (canal, color) in enumerate(zip(canales, colores)):
            datos = image[:, :, i].flatten()
            plt.figure()
            plt.hist(datos, bins=256, color=color, alpha=0.7)
            plt.title(f"Histograma - Canal {canal}")
            plt.xlabel("Valor")
            plt.ylabel("Frecuencia")
            plt.grid(True)

            filename = f"{name_prefix}_hist_{canal}.png"
            plt.savefig(os.path.join(self.output_dir, filename))
            plt.close()
