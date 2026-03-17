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
            acoes.append((arquivo,categoria)) #registrando na lista...

    return acoes

def organizar_arquivos(pasta,acoes):
    for arquivo, categoria in acoes:
        criar_pasta_categoria(pasta,categoria)
        origem = os.path.join(pasta,arquivo) #caminho antes de mover
        destino = os.path.join(pasta,categoria,arquivo) #caminho incluindo a nova pasta

        shutil.move(origem,destino)
        print(f"{arquivo} movido para {categoria}")

def registrar_log(arquivo,categoria):
    with open("log_organizador.txt","a",encoding="utf-8") as log:
        log.write(f"{arquivo} -> {categoria}\n")


    
def main():
    print("== Organizador de arquivos v0.5 ==")
    pasta = input("Digite o caminho da pasta que deseja organizar: ")
    
    try:
        acoes = analisar_arquivos(pasta)
        confirma = input("\nDeseja organizar esses arquivos? (s/n): ").lower()

        if confirma == "s":
            organizar_arquivos(pasta,acoes)
            print("\nOrganização concluída!")
        else:
            print("\nOperação cancelada.")

    except FileNotFoundError: #se a pasta não foi encontrada
        print("A pasta não foi encontrada.")

    except PermissionError: #se não conseguiu acessa-la
        print("Sem permissão para acessar essa pasta.")

if __name__ == "__main__":
    main()
