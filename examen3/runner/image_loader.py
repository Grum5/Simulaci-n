from PIL import Image
import numpy as np
import os


class ImageLoader:
    '''
        Clase encargada de cargar imagenes en formato RGB
        desde la carpeta de resources.
    '''

    def __init__(self, dir_path: str = "resources"):
        ''' Constructor '''

        self.dir_path = dir_path

    def image_to_array(self, filename: str) -> np.ndarray:
        ''' Carga una imagen RGB como un arreglo NumPy '''

        # Obtener la ruta de la imagen
        path = os.path.join(self.dir_path, filename)

        # Verificar la existencia de la imagen
        if not os.path.exists(path):

            # Lanzar un error si no existe la imagen
            raise FileNotFoundError(
                f"La imagen '{filename}' no se encuentra en '{self.dir_path}'."
            )

        try:
            # Se abre la imagen
            with Image.open(path) as img:

                # Se convierte en formato RGB y se retorna un array
                img = img.convert("RGB")
                return np.array(img)

        except Exception as e:

            # Se lanza un error si no se puede abrir la imagen
            raise ValueError(f"No se pudo abrir la imagen: {e}")

    def save_image(self, image: np.ndarray, filename: str) -> str:
        '''
            Guardar un arreglo NumPy como una imagen en formato PNG.
            Retorna el path donde se guardo la imagen.
        '''

        try:

            img = Image.fromarray(image.astype(np.uint8))
            output_path = os.path.join(self.dir_path, filename)
            img.save(output_path)

            return output_path

        except Exception as e:
            raise ValueError(f"No se pudo guardar la imagen: {e}")
