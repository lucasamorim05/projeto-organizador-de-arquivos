#Torna o progama automático

from watchdog.observers import Observer                 #monitora a pasta
from watchdog.events import FileSystemEventHandler      #reage a eventos
import time                                             #controla pausas (evita travar CPU)
import os                                               
from main import executar_organizacao                   #função do main.py


class MonitorHandler(FileSystemEventHandler):           #classe que reage a eventos do sistema

    def __init__(self, pasta):                          #recebe a pasta que será monitorada
        self.pasta = pasta                              #guarda essa informação dentro da classe

    def on_created(self, event):
        if not event.is_directory:                      #verifica se é arquivo, e não pasta
            print(f"Novo arquivo detectado: {event.src_path}")
            executar_organizacao(self.pasta)

def iniciar_monitoramento(pasta):                        #inicia todo o sistema de monitoramento
    event_handler = MonitorHandler(pasta)                #Define o que fazer quando algo acontecer
    observer = Observer()                                #vigia a pasta
    
    observer.schedule(event_handler, path=pasta, recursive=False)
    observer.start()  #começa a observar a pasta em tempo real

    print(f"Monitorando pasta: {pasta}")

    try:
        while True:                                       #Mantém o programa rodando
            time.sleep(2)
    except KeyboardInterrupt:                             #Se apertar Ctrl + C, o programa para
        observer.stop()
    
    observer.join()