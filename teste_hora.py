from datetime import datetime
import time

def muda_seed():
    nova_seed = datetime.now().timestamp()#pega a hora atual para gerar o numero aleatório
    return nova_seed

