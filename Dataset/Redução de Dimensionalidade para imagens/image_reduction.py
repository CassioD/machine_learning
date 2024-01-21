from PIL import Image

def rgb_to_gray(pixel):
    # Converte a cor RGB para escala de cinza usando a média ponderada
    return int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])

def convert_to_grayscale(image):
    # Converte uma imagem colorida para escala de cinza
    grayscale_image = Image.new("L", image.size)
    for x in range(image.width):
        for y in range(image.height):
            grayscale_value = rgb_to_gray(image.getpixel((x, y)))
            grayscale_image.putpixel((x, y), grayscale_value)
    return grayscale_image

def convert_to_binary(image, threshold=128):
    # Binariza uma imagem em escala de cinza
    binary_image = Image.new("1", image.size)
    for x in range(image.width):
        for y in range(image.height):
            binary_value = 0 if image.getpixel((x, y)) < threshold else 1
            binary_image.putpixel((x, y), binary_value)
    return binary_image

def main():
    # Carrega a imagem
    input_image_path = "imagem.jpg"  # Substitua pelo caminho da sua imagem
    original_image = Image.open(input_image_path)

    # Converte para escala de cinza
    grayscale_image = convert_to_grayscale(original_image)
    grayscale_image.save("escala_de_cinza.jpg")

    # Converte para imagem binarizada
    binary_image = convert_to_binary(grayscale_image)
    binary_image.save("binarizada.jpg")

if __name__ == "__main__":
    main()
