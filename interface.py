import tkinter as tk #biblioteca para criar janelas (interfaces gráficas)
from tkinter import filedialog #abre janela para escolher pasta
from main import executar_organizacao #função onde está a lógica do organizador
import threading   #roda mais de um código ao mesmo tempo
from monitor import iniciar_monitoramento

monitorando = False  #variável para saber se o monitor está rodando

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

def iniciar_auto():
    global monitorando
    pasta = label_pasta.cget("text")

    if pasta == "Nenhuma pasta selecionada":    #verifica se o usuário selecionou pasta
        label_status.config(text="Selecione uma pasta primeiro!")
        return

    if not monitorando:     #Verifica se já está monitorando
        monitorando = True
        label_status.config(text="Monitoramento ativo...")  #Atualiza a interface

        thread = threading.Thread(      #Cria uma thread
            target=iniciar_monitoramento,
            args=(pasta,),
            daemon=True
        )
        thread.start()



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

#Cria botão Organizar auto
btn_auto = tk.Button(janela, text="Ativar Organização Automática", command=iniciar_auto)
btn_auto.pack(pady=5)

# Cria status 
label_status = tk.Label(janela, text="")
label_status.pack(pady=10)

#Executar interface
janela.mainloop()