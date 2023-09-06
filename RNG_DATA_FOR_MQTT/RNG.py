#Dados Elétricos
#MF1%%tensao%%corrente%%MF2%%tensao%%corrente%%MF3%%tensao%%corrente%%MF4%%tensao%%corrente%%
#MM1%%tensao%%corrente%%MM2%%tensao%%corrente%%
#Dados de temperatura & vazão
#TC%%vazão(L/min)%%entrada(ºC)%%dentro(ºC)%%saída(ºC)%%change%%TD%%vazão(L/min)%%entrada(ºC)%%dentro(ºC)%%saída(ºC)
#Dados ambientes (a serem medidos)
#UM%%numero%%TEMP%%numero%%Radiação%%numero%%Inclinação%%X%%Y%%Z
import random
import Classes

#insira os limites para as variáveis
Classes.muda_limites(Classes.Modulo_fixo_1, 0,100)
Classes.muda_limites(Classes.Modulo_fixo_1, 0,100)
Classes.muda_limites(Classes.Modulo_fixo_1, 0,100)
Classes.muda_limites(Classes.Modulo_fixo_1, 0,100)
Classes.muda_limites(Classes.Modulo_movel_1, 0,100)
Classes.muda_limites(Classes.Modulo_movel_1, 0,100)




Classes.Modulo_fixo_1.tensao = 5
print(Classes.Modulo_fixo_1.tensao)