
import numpy as np
from runner.models.tinkerbell import Tinkerbell
from runner.models.henon import Henon
from runner.models.chen import Chen
from runner.models.logistico import Logistico


class Encryption:

    def __init__(self) -> None:
        ''' Constructor '''

        # Valores estandar pre-estalecidos
        self.tinkerbell = Tinkerbell(0.9, -0.6013, 2.0, 0.50, 0.1, 0.1)
        self.henon = Henon(1.4, 0.3, 0.1, 0.3)
        self.chen = Chen(2.0, 0.5, 0.1, 0.1)
        self.logistico = Logistico(3.99, 3.97, 0.1234, 0.5678)

    def encrypt_tinkerbell(self, image: np.ndarray) -> np.ndarray:
        '''
            Cifra una imagen RGB usando un PRNG dado mediante cifrado
            en flujo (XOR).
        '''

        encrypted_image = np.empty_like(image)

        height, width, channels = image.shape

        for i in range(height):
            for j in range(width):
                for channel in range(channels):
                    pseudo_value = self.tinkerbell.get_pseudonumber()

                    if isinstance(pseudo_value, tuple):
                        pseudo_value = pseudo_value[0]

                    scaled = int(pseudo_value * 256) % 256
                    encrypted_image[i, j, channel] = image[i, j, channel] ^ scaled

        return encrypted_image

    def encrypt_henon(self, image: np.ndarray) -> np.ndarray:
        '''
            Cifra una imagen RGB usando un PRNG dado mediante cifrado
            en flujo (XOR).
        '''

        encrypted_image = np.empty_like(image)

        height, width, channels = image.shape

        for i in range(height):
            for j in range(width):
                for channel in range(channels):
                    pseudo_value = self.henon.get_pseudonumber()

                    if isinstance(pseudo_value, tuple):
                        pseudo_value = pseudo_value[0]

                    scaled = int(pseudo_value * 256) % 256
                    encrypted_image[i, j, channel] = image[i, j, channel] ^ scaled

        return encrypted_image

    def encrypt_chen(self, image: np.ndarray) -> np.ndarray:
        '''
            Cifra una imagen RGB usando un PRNG dado mediante cifrado
            en flujo (XOR).
        '''

        encrypted_image = np.empty_like(image)

        height, width, channels = image.shape

        for i in range(height):
            for j in range(width):
                for channel in range(channels):
                    pseudo_value = self.chen.get_pseudonumber()

                    if isinstance(pseudo_value, tuple):
                        pseudo_value = pseudo_value[0]

                    scaled = int(pseudo_value * 256) % 256
                    encrypted_image[i, j, channel] = image[i, j, channel] ^ scaled

        return encrypted_image

    def encrypt_logistico(self, image: np.ndarray) -> np.ndarray:
        '''
            Cifra una imagen RGB usando un PRNG dado mediante cifrado
            en flujo (XOR).
        '''

        encrypted_image = np.empty_like(image)

        height, width, channels = image.shape

        for i in range(height):
            for j in range(width):
                for channel in range(channels):
                    pseudo_value = self.logistico.get_pseudonumber()

                    if isinstance(pseudo_value, tuple):
                        pseudo_value = pseudo_value[0]

                    scaled = int(pseudo_value * 256) % 256
                    encrypted_image[i, j, channel] = image[i, j, channel] ^ scaled

        return encrypted_image
