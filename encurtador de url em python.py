import tkinter as tk
import pyshorteners as shr
import tkinter.messagebox as messagebox

def encurtar_url():
    url_longa = entry.get()
    shortener = shr.Shortener()
    shortURL = shortener.tinyurl.short(url_longa)
    label_resultado.config(text=f"A URL encurtada é: {shortURL}")

def copiar_url():
    url_encurtada = label_resultado.cget("text")
    janela.clipboard_clear()
    janela.clipboard_append(url_encurtada.split(": ")[1])
    messagebox.showinfo("Sucesso", "URL encurtada copiada para a área de transferência!")

# Criação da janela
janela = tk.Tk()
janela.title("Encurtador de URL")
janela.geometry("400x200")  # Definindo o tamanho da janela

# Criação dos widgets
label_url = tk.Label(janela, text="Digite a URL:")
label_url.pack()

entry = tk.Entry(janela, width=50)  # Ajustando o tamanho do campo de entrada
entry.pack()

button_encurtar = tk.Button(janela, text="Encurtar", command=encurtar_url)
button_encurtar.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

button_copiar = tk.Button(janela, text="Copiar", command=copiar_url)
button_copiar.pack()

# Execução da janela
janela.mainloop()
