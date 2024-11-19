import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg():
    while True:
        # Solicitar al usuario el nombre de la carpeta
        folder_path = input("Por favor, ingresa la ruta de la carpeta con archivos HEIC: ")

        # Validar si la carpeta existe
        if not os.path.isdir(folder_path):
            print("La carpeta especificada no existe. Por favor, verifica la ruta e inténtalo de nuevo.")
            continue

        # Recorrer la carpeta y todas las subcarpetas
        total_files = 0
        for root, _, files in os.walk(folder_path):
            # Filtrar archivos HEIC en la subcarpeta actual
            heic_files = [f for f in files if f.lower().endswith(".heic")]
            if heic_files:
                # Crear una carpeta de salida para los archivos JPG en la subcarpeta actual
                output_folder = os.path.join(root, "convertedjpg")
                os.makedirs(output_folder, exist_ok=True)

                # Contabilizar archivos y procesar cada uno
                total_files += len(heic_files)
                print(f"\nSubcarpeta '{root}': {len(heic_files)} archivos HEIC encontrados.")

                for index, filename in enumerate(heic_files, start=1):
                    heic_path = os.path.join(root, filename)
                    jpg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

                    try:
                        # Convertir el archivo HEIC a JPG
                        heif_file = pillow_heif.open_heif(heic_path)
                        image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
                        image.save(jpg_path, "JPEG")
                        print(f"Convertido {index}/{len(heic_files)} en '{root}': {filename} -> {os.path.basename(jpg_path)}")
                    except Exception as e:
                        print(f"Error al convertir {filename} en '{root}': {e}")

        if total_files == 0:
            print("No se encontraron archivos HEIC en la carpeta ni en sus subcarpetas.")
        else:
            print("\nConversión completada.")

        # Preguntar si desea procesar otra carpeta
        repeat = input("¿Quieres procesar otra carpeta? (s/n): ")
        if repeat.lower() != 's':
            print("Proceso terminado.")
            break

# Llamada a la función
convert_heic_to_jpg()
