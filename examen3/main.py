
from runner.histogram_analyzer import HistogramAnalyzer
from runner.encryption import Encryption
from runner.image_loader import ImageLoader
from runner.entropy_calculator import EntropyCalculator


if __name__ == '__main__':

    image_handler = ImageLoader()
    e = Encryption()
    h = HistogramAnalyzer()

    image_array = image_handler.image_to_array("imagen.png")

    tinkerbell_encrypt = e.encrypt_tinkerbell(image_array)
    henon_encrypt = e.encrypt_henon(image_array)
    chen_encrypt = e.encrypt_chen(image_array)
    logistico_encrypt = e.encrypt_logistico(image_array)

    image_handler.save_image(tinkerbell_encrypt, "tinkerbell.png")
    image_handler.save_image(henon_encrypt, "henon.png")
    image_handler.save_image(chen_encrypt, "chen.png")
    image_handler.save_image(logistico_encrypt, "logistico.png")

    h.generate_histograms(tinkerbell_encrypt, "h_tinkerbell")
    h.generate_histograms(henon_encrypt, "h_henon")
    h.generate_histograms(chen_encrypt, "h_chen")
    h.generate_histograms(logistico_encrypt, "h_logistico")

    tinkerbell_result = EntropyCalculator.calculate(tinkerbell_encrypt)
    henon_result = EntropyCalculator.calculate(henon_encrypt)
    chen_result = EntropyCalculator.calculate(chen_encrypt)
    logistico_result = EntropyCalculator.calculate(logistico_encrypt)

    print("Entropia por canal Tinkerbell:")
    for canal, valor in tinkerbell_result.items():
        print(f"{canal}: {valor:.4f}")

    print("Entropia por canal Henon:")
    for canal, valor in henon_result.items():
        print(f"{canal}: {valor:.4f}")

    print("Entropia por canal Chen:")
    for canal, valor in chen_result.items():
        print(f"{canal}: {valor:.4f}")

    print("Entropia por canal Logistico2D:")
    for canal, valor in logistico_result.items():
        print(f"{canal}: {valor:.4f}")
