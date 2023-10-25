import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def generate_qr_code():
    link = link_entry.get()
    nome_imagem = nome_imagem_entry.get()

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
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Salve a imagem com o nome fornecido pelo usuário
    qr_img.save(nome_imagem)

    # Exiba uma mensagem informando que a imagem foi criada com sucesso
    result_label.config(text=f"O QR code foi gerado com sucesso e salvo como '{nome_imagem}'!")

    # Carregue a imagem do QR code na interface
    qr_image = Image.open(nome_imagem)
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

# Crie a janela principal
root = tk.Tk()
root.title("Gerador de QR Code")

# Crie e posicione os elementos na janela
link_label = tk.Label(root, text="Digite o link que deseja codificar no QR code:")
link_label.pack()
link_entry = tk.Entry(root)
link_entry.pack()

nome_imagem_label = tk.Label(root, text="Digite o nome do arquivo de imagem:")
nome_imagem_label.pack()
nome_imagem_entry = tk.Entry(root)
nome_imagem_entry.pack()

generate_button = tk.Button(root, text="Gerar QR Code", command=generate_qr_code)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

qr_label = tk.Label(root)
qr_label.pack()

# Inicie a interface
root.mainloop()
