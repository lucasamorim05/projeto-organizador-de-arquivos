#Torna o progama automático

from watchdog.observers import Observer                 #monitora a pasta
from watchdog.events import FileSystemEventHandler      #reage a eventos
import time                                             #controla pausas (evita travar CPU)
import os                                               
from main import executar_organizacao                   #função do main.py