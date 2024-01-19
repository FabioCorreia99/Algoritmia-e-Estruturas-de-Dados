from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Seletor de Imagem")
        self.root.geometry("400x400")

        self.imagem_label = tk.Label(root, text="Nenhuma imagem selecionada")
        self.imagem_label.pack(pady=10)

        self.botao_selecionar = tk.Button(root, text="Selecionar Imagem", command=self.selecionar_imagem)
        self.botao_selecionar.pack(pady=10)

        self.botao_salvar = tk.Button(root, text="Salvar Imagem", command=self.salvar_imagem)
        self.botao_salvar.pack(pady=10)

        self.imagem = None
        self.caminho_imagem = ""

    def selecionar_imagem(self):
        # Abre uma janela de diálogo para selecionar a imagem
        self.caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")])

        if self.caminho_imagem:
            # Carrega a imagem e exibe na interface
            imagem_pil = Image.open(self.caminho_imagem)
            imagem_resized = imagem_pil.resize((200, 200))  # Remova Image.ANTIALIAS
            self.imagem = ImageTk.PhotoImage(imagem_resized)
            self.imagem_label.config(image=self.imagem, text="")
        else:
            self.imagem_label.config(text="Nenhuma imagem selecionada")

    def salvar_imagem(self):
        if self.imagem and self.caminho_imagem:
            # Obtém o diretório onde o script está localizado
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))

            # Define o caminho para salvar a imagem (pode ser ajustado conforme necessário)
            caminho_destino = os.path.join(diretorio_atual, "imagem_salva.png")

            # Salva a imagem no novo local
            imagem_pil = Image.open(self.caminho_imagem)
            imagem_pil.save(caminho_destino)

            messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem selecionada para salvar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()