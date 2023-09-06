class Modulo_fixo_1:
    lim_inf =0
    lim_sup = 100
    tensao = 0
    corrente = 0
class Modulo_fixo_2:
    lim_inf =0
    lim_sup = 100
    tensao = 0
    corrente = 0
class Modulo_fixo_3:
    lim_inf =0
    lim_sup = 100
    tensao = 0
    corrente = 0
class Modulo_fixo_4:
    lim_inf =0
    lim_sup = 100
    tensao = 0
    corrente = 0
class Modulo_movel_1:
    lim_inf =0
    lim_sup = 100
    tensao = 0
    corrente = 0
    incline = [0,0,0] #x,y,z em graus
class Modulo_movel_1:
    lim_inf =0
    lim_sup = 100
    tensao = 0
    corrente = 0
    incline = [0,0,0] #x,y,z em graus
class Trocador_100:
    lim_inf =0
    lim_sup = 100
    vazao = 0
    entrada = 0
    dentro = 0
    saida = 0
class Trocador_200:
    lim_inf =0
    lim_sup = 100
    vazao = 0
    entrada = 0
    dentro = 0
    saida = 0
class ambiente:
    lim_inf = 0
    lim_sup = 100
    humidade = 0
    temperatura = 0
    radiação_solar = 0
    incline = [0,0,0] #x,y,z em graus


def muda_limites(classe, lim_inf, lim_sup):
    classe.lim_inf = lim_inf
    classe.lim_sup = lim_sup

