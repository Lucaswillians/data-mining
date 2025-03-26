import pandas as pd
import random
from faker import Faker

fake = Faker()

def gerar_dados_corrida(num_voltas):
    dados_corrida = []
    
    for volta in range(1, num_voltas + 1):
        dados_corrida.append({
            "volta": volta,
            "tempo_volta": float(fake.random.uniform(80, 95)),  
            "desgaste_pneu": float(fake.random.uniform(5, 50)), 
            "temperatura_pista": float(fake.random.uniform(20, 45)), 
            "umidade": float(fake.random.uniform(30, 90)), 
            "posicao_antes_pit": fake.random_int(min=1, max=20), 
            "tempo_pit_stop": float(fake.random.uniform(2, 4)), 
            "posicao_apos_pit": fake.random_int(min=1, max=20), 
            "piloto": fake.name(), 
            "equipe": fake.company(), 
            "pneu_utilizado": fake.random_element(elements=["Macio", "Médio", "Duro", "Chuva"]), 
            "clima": fake.random_element(elements=["Ensolarado", "Nublado", "Chuvoso", "Ventando"]) 
        })
    
    return dados_corrida

dados_ficticios = gerar_dados_corrida(50)

df_corrida = pd.DataFrame(dados_ficticios)

print(df_corrida.head())
