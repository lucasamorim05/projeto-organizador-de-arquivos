import tkinter as tk #biblioteca para criar janelas (interfaces gráficas)
from tkinter import filedialog #abre janela para escolher pasta
from main import executar_organizacao #função onde está a lógica do organizador

def selecionar_pasta():
    pasta = filedialog.askdirectory() #retorna o caminho da pasta
    if pasta:
        label_pasta.config(text=pasta) #Atualiza o texto na tela

def organizar():
    pasta = label_pasta.cget("text") #pega o caminho da pasta

    #Verifica se o usuário selecionou algo
    if pasta == "Nenhuma pasta selecionada": 
        label_status.config(text="Selecione uma pasta primeiro!")
        return

    #Mostra "Organizando.."
    label_status.config(text="Organizando...")
    janela.update()


    resultado = executar_organizacao(pasta) #chama main.py
    label_status.config(text=resultado) #mostra resultado

#Cria janela
janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("500x250")

#Cria título
titulo = tk.Label(janela, text="Organizador de Arquivos", font=("Arial", 16))
titulo.pack(pady=10)

# Cria botão selecionar pasta
btn_pasta = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
btn_pasta.pack(pady=5)

# Cria caminho da pasta
label_pasta = tk.Label(janela, text="Nenhuma pasta selecionada")
label_pasta.pack(pady=5)

# Cria botão organizar
btn_organizar = tk.Button(janela, text="Organizar Arquivos", command=organizar)
btn_organizar.pack(pady=10)

# Cria status 
label_status = tk.Label(janela, text="")
label_status.pack(pady=10)

#Executar interface
janela.mainloop()