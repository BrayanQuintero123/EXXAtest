import os
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def extract_and_save_fits_images(input_dir: str, output_dir: str, cmap='gray'):
    """
    Extrae la capa [0, 0, 0] de cada archivo .fits y la guarda como .png.

    Args:
        input_dir (str): Carpeta que contiene los archivos .fits.
        output_dir (str): Carpeta donde se guardarán las imágenes .png.
        cmap (str): Colormap para guardar la imagen (por defecto 'gray').
    """
    os.makedirs(output_dir, exist_ok=True)

    fits_files = [f for f in os.listdir(input_dir) if f.endswith('.fits')]

    for file in tqdm(fits_files, desc="Procesando FITS"):
        file_path = os.path.join(input_dir, file)
        hdul = fits.open(file_path)
        data = hdul[0].data  # forma (4, 1, 1, 600, 600)

        if data is not None and data.shape == (4, 1, 1, 600, 600):
            image = data[0, 0, 0]  # (600, 600)
            output_path = os.path.join(output_dir, file.replace('.fits', '.png'))

            # Normalizamos entre 0-1 para guardar como imagen
            norm_image = (image - np.min(image)) / (np.max(image) - np.min(image))

            plt.imsave(output_path, norm_image, cmap=cmap)
        else:
            print(f"Formato inesperado en: {file}")
            continue