import qrcode

# Solicitar ao usuário o link e o nome da imagem
link = input("Digite o link que deseja codificar no QR code: ")
nome_imagem = input("Digite o nome do arquivo de imagem (por exemplo, qr_code.png): ")

# Crie um objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR code (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erros (L, M, Q, H)
    box_size=10,  # Tamanho dos quadrados dentro do QR code
    border=4,  # Tamanho da borda
)

# Adicione os dados (o link) ao QR code
qr.add_data(link)
qr.make(fit=True)

# Crie uma imagem do QR code
img = qr.make_image(fill_color="black", back_color="white")

# Salve a imagem com o nome fornecido pelo usuário
img.save(nome_imagem)

# Exiba uma mensagem informando que a imagem foi criada com sucesso
print(f"O QR code foi gerado com sucesso e salvo como '{nome_imagem}'!")

# Mostre a imagem
img.show()
