import random
from faker import Faker
import pandas as pd

fake = Faker()

def gerar_dados_corrida(num_voltas=10):
    dados_corrida = []
    for volta in range(1, num_voltas + 1):
        dados_corrida.append({
            "volta": volta,
            "tempo_volta": round(random.uniform(80, 95), 2),  
            "desgaste_pneu": round(random.uniform(5, 50), 2), 
            "temperatura_pista": round(random.uniform(20, 45), 2), 
            "umidade": round(random.uniform(30, 90), 2), 
            "posicao_antes_pit": random.randint(1, 20), 
            "tempo_pit_stop": round(random.uniform(2, 4), 2), 
            "posicao_apos_pit": random.randint(1, 20) 
        })
    return dados_corrida

dados_ficticios = gerar_dados_corrida(50)

df_corrida = pd.DataFrame(dados_ficticios)

print(df_corrida.head())
