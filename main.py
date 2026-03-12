import os
import shutil 


CATEGORIAS = { #cria dicionários conectando nossas categorias com as extensões
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Musicas": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar"]
}

def descobrir_categoria(arquivo):
    extensao =  os.path.splitext(arquivo)[1].lower() #separa nome e extensão

    for categoria, extensoes in CATEGORIAS.items(): #percorre CATEGORIAS e verifica se o meu arquivo tem uma delas
        if extensao in extensoes:
            return categoria

    return "Outros" #se não encontrou, retorne outros   

def criar_pasta_categoria(pasta, categoria):
    caminho_categoria = os.path.join(pasta, categoria) #junta pasta com a categoria
    #ex: C:/Users/ + "Imagens"
    
    if not os.path.exists(caminho_categoria):
        os.mkdir(caminho_categoria) #cria a pasta
        print(f"Pasta criada: {categoria}")

def analisar_arquivos(pasta):
    acoes = [] #guarda ações que o progama pode executar depois
    arquivos = os.listdir(pasta) #acessa a pasta e pega seus arquivos
    print("\narquivos encontrados!\n")

    for arquivo in arquivos: #para cada arquivo encontrado
        caminho_completo = os.path.join(pasta, arquivo) #junta pasta e arquivo e cria o caminho completo

        if os.path.isfile(caminho_completo):
            categoria = descobrir_categoria(arquivo) 
            print(f"{arquivo} → {categoria}") #se existir, descobre sua categoria e exibe ela
            acoes.append((arquivo,pasta)) #registrando na lista...

    return acoes

def rganizar_arquivos(pasta,acoes):

def main():
    print("== Organizador de arquivos v0.4 ==")
    pasta = input("Digite o caminho da pasta que deseja organizar: ")
    
    try:
        acoes = analisar_arquivos(pasta)
        confirma = input("\nDeseja organizar esses arquivos? (s/n): ").lower()

        if confirma == "s":
            organizar_arquivos(pasta,acoes)


if __name__ == "__main__":
    main()
