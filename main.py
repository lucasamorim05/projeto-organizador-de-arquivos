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
    try:
        arquivos = os.listdir(pasta) #acessa a pasta e pega seus arquivos
        print("\narquivos encontrados!\n")

        for arquivo in arquivos: #para cada arquivo encontrado
            caminho_completo = os.path.join(pasta, arquivo) #junta pasta e arquivo e cria o caminho completo

            if os.path.isfile(caminho_completo):
                categoria = descobrir_categoria(arquivo) 
                criar_pasta_categoria(pasta,categoria)
                print(f"{arquivo} → {categoria}") #se existir, descobre sua categoria e exibe ela
                

    
    except FileNotFoundError: #se a pasta não foi encontrada
        print("A pasta não foi encontrada.")

    except PermissionError: #se não conseguiu acessa-la
        print("Sem permissão para acessar essa pasta.")

def main():
    print("== Organizador de arquivos v0.4 ==")
    pasta = input("Digite o caminho da pasta que deseja organizar: ")
    
    try:
        analisar_arquivos(pasta)

if __name__ == "__main__":
    main()
