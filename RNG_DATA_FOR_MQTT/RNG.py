#Dados Elétricos
#MF1%%tensao%%corrente%%MF2%%tensao%%corrente%%MF3%%tensao%%corrente%%MF4%%tensao%%corrente%%
#MM1%%tensao%%corrente%%MM2%%tensao%%corrente%%
#Dados de temperatura & vazão
#TC%%vazão(L/min)%%entrada(ºC)%%dentro(ºC)%%saída(ºC)%%change%%TD%%vazão(L/min)%%entrada(ºC)%%dentro(ºC)%%saída(ºC)
#Dados ambientes (a serem medidos)
#UM%%numero%%TEMP%%numero%%Radiação%%numero%%Inclinação%%X%%Y%%Z
import random
import Classes
from datetime import datetime
import time

#insira os limites para as variáveis
#Os limites servem para todas as variáveis da classe, portanto os valores são compartilhados por tensão e corrente.
Classes.muda_limites(Classes.Modulo_fixo_1, 5,73)
Classes.muda_limites(Classes.Modulo_fixo_2, 0,100)
Classes.muda_limites(Classes.Modulo_fixo_3, 0,100)
Classes.muda_limites(Classes.Modulo_fixo_4, 0,100)
Classes.muda_limites(Classes.Modulo_movel_1, 0,100)
Classes.muda_limites(Classes.Modulo_movel_2, 0,100)

arquivo = open("valores.txt", "w+")

#random.seed(Classes.muda_seed())
Classes.Modulo_fixo_1.tensao = random.randrange(Classes.Modulo_fixo_1.lim_sup )
arquivo.write("tensao = " + str(Classes.Modulo_fixo_1.tensao) + "\n")
Classes.Modulo_fixo_1.corrente = random.randrange(Classes.Modulo_fixo_1.lim_sup )
arquivo.write("corrente = " + str(Classes.Modulo_fixo_1.corrente))