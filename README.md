# Avaliação N1 - Mineração de dados

## Alunos: Lucas Willian de Souza Serpa, Marlon de Souza

- 1. Mineração de Dados (MD) é uma técnica utilizada para identificar padrões úteis em grandes quantidades de
dados, também é considerada uma das atividades do processo de descoberta de conhecimento. Neste sentido,
apresente exemplos sucintos em que técnicas como classificação, regressão, clusterização, associação e
detecção de anomalias possam ser utilizadas em um processo de MD (2,5).
- 2. Um dos passos críticos no processo MD é o entendimento de negócio (domínio de problema) em que o modelo
de MD será implementado. Uma das maneiras de minimizar essa criticidade é utilizar Questões Analíticas
(QA) apoiadas pelo método SMART (Specific, Measurable, Attainable, Relevant, Time-related). Apresente um
exemplo de problema (diferente dos que foram apresentados em aula) com ao menos quatro QAs (2,5).
- 3. As atividades Entendimento e Preparação de dados do modelo de processo CRISP-DM são pautadas no
entendimento do negócio, assim utilize o domínio de negócio apresentado na questão anterior (2) para gerar
dados brutos (sugestão, é possível gerar dados brutos com LLMs ou bibliotecas como Faker em Python,...), em
seguida apresente exemplos relacionados às atividades de Entendimento e Preparação de Dados (3,0).

---

Questão 1: A Mineração de Dados (MD) é fundamental na análise de grandes volumes de informações, permitindo identificar padrões relevantes que auxiliam significativamente na tomada de decisões. Um exemplo prático da aplicação dessas técnicas é a utilização da base de dados Breast Cancer Wisconsin (Diagnostic), composta por atributos extraídos de imagens digitalizadas de células obtidas em massas mamárias. Utilizando essa base como exemplo, podemos aplicar diversas abordagens da mineração de dados para diferentes objetivos: 

- Classificação: Essa técnica é particularmente útil para prever se um tumor é maligno ou benigno, considerando atributos específicos como textura, compactação e raio das células. Algoritmos de IA amplamente utilizados para essas tarefas são os Multi Layer Perceptron e Knn's.

- Regressão: Embora a variável-alvo seja geralmente categórica, é possível aplicar técnicas de regressão para estimar a probabilidade de malignidade dos tumores, com base nas características disponíveis. Isso facilita a compreensão quantitativa do risco associado a determinados perfis celulares. Por exemplo, com base nas features A, B e C o risco da pessoa x desenvolver cancer de mama é y%. 

- Clusterização: Permite agrupar pacientes com padrões celulares semelhantes, sem depender dos diagnósticos previamente rotulados. Essa abordagem é valiosa para identificar subgrupos específicos de risco, utilizando técnicas como o K-means  (baseado em distância) ou o DBSCAN (baseado em densidade). 

- Regras de Associação: Técnicas de associação podem identificar padrões frequentes e relevantes entre as características celulares. Por exemplo, é possível descobrir regras indicando que, quando atributos como textura e simetria ultrapassam determinados limites, há uma maior probabilidade do tumor ser maligno, proporcionando insights clínicos úteis para diagnóstico precoce. 

- Detecção de Anomalias: Essa abordagem identifica exames cujas características celulares fogem significativamente dos padrões predominantes na base de dados. Casos assim podem indicar erros no diagnóstico inicial ou revelar tumores raros e atípicos, destacando-os para investigação mais detalhada. 

 ---

Questão 2: Para essa questão, resolvemos criar algo sobre a formula 1. As equipes de Fórmula 1 buscam constantemente otimizar suas estratégias de pit stop para minimizar o tempo perdido durante a corrida e maximizar o desempenho dos pneus. O objetivo é desenvolver um modelo de Machine Learning (MD) que ajude a prever o momento ideal para realizar o pit stop com base em diversos fatores. 

Questões Analíticas (QAs) com SMART 

Qual a influência do desgaste dos pneus no desempenho do carro durante a corrida? 

- Specific: Analisar como a degradação dos pneus afeta tempos de volta e aderência. 

- Measurable: Avaliar a variação dos tempos de volta conforme o número de voltas percorridas com um mesmo jogo de pneus. 

- Attainable: Utilizar dados de telemetria, sensores de temperatura e desgaste dos pneus. 

- Relevant: Melhorar a precisão na escolha do momento ideal para troca de pneus. 

- Time-related: Analisar o desgaste médio dos pneus em diferentes circuitos nos últimos 3 anos. 

Como as condições climáticas afetam a necessidade de um pit stop antecipado? 

- Specific: Examinar a relação entre temperatura da pista, umidade e degradação dos pneus. 

- Measurable: Comparar corridas em diferentes condições climáticas e a variação da performance dos pneus. 

- Attainable: Utilizar dados meteorológicos históricos e registros das equipes. 

- Relevant: Prever quando uma mudança climática pode exigir um pit stop inesperado. 

- Time-related: Considerar dados dos últimos 5 anos para identificar padrões. 

Qual o impacto do tráfego de outros carros na decisão de realizar um pit stop? 

- Specific: Identificar se parar antes ou depois dos concorrentes diretos gera vantagem na corrida. 

- Measurable: Comparar a diferença de posições antes e depois do pit stop em relação a rivais diretos. 

- Attainable: Usar dados de posicionamento por GPS e estratégias de corrida passadas. 

- Relevant: Melhorar a tomada de decisão da equipe durante a corrida. 

- Time-related: Analisar as últimas 50 corridas para identificar padrões. 

Como o tempo médio de um pit stop impacta a posição final do carro na corrida? 

- Specific: Determinar a relação entre a eficiência da parada e a posição final. 

- Measurable: Comparar tempos de pit stop com a variação de posições pós-parada. 

- Attainable: Utilizar tempos de pit stop oficiais das equipes. 

- Relevant: Otimizar o trabalho dos mecânicos para reduzir o tempo perdido. 

- Time-related: Considerar as últimas 3 temporadas para uma análise mais ampla. 


---
Questão 3: 

<img width="840" alt="Captura de Tela 2025-03-25 às 20 33 21" src="https://github.com/user-attachments/assets/f711eb5a-39c9-450a-bc63-e93c5907d739" />

Com base nos dados gerados para as atividades de Entendimento e Preparação de Dados no processo CRISP-DM para a análise de pit stops na Fórmula 1, podemos seguir as diretrizes das atividades dessa metodologia de forma prática. Vamos abordar cada uma das fases:

1. Entendimento do Negócio (Objetivo do Modelo)
O principal objetivo aqui é usar o conjunto de dados para prever o momento ideal para realizar um pit stop durante uma corrida de Fórmula 1, considerando fatores como tempo de volta, desgaste dos pneus, temperatura da pista, umidade, posição na corrida antes e depois do pit stop, e tempo de pit stop.

Esses fatores podem influenciar diretamente a performance dos carros e a decisão de quando realizar uma troca de pneus. A análise desses dados visa ajudar as equipes a tomar decisões mais informadas sobre quando realizar o pit stop, minimizando o impacto na posição do carro após a parada e maximizando o desempenho na corrida.

2. Entendimento dos Dados
O conjunto de dados gerado possui as seguintes variáveis:

volta: Número da volta na corrida.

tempo_volta: O tempo (em segundos) necessário para completar uma volta.

desgaste_pneu: O percentual de desgaste dos pneus até o momento da volta.

temperatura_pista: A temperatura da pista em graus Celsius.

umidade: O percentual de umidade no ambiente.

posicao_antes_pit: A posição do carro na corrida antes de realizar o pit stop.

tempo_pit_stop: O tempo (em segundos) gasto para realizar o pit stop.

posicao_apos_pit: A posição do carro na corrida após realizar o pit stop.

3. Preparação dos Dados
Para preparar os dados para análise, o primeiro passo seria limpar e transformar as variáveis. Considerando os dados gerados:

Desgaste dos pneus e tempo de volta são variáveis contínuas que podem ser utilizadas para identificar como a degradação dos pneus impacta o desempenho do carro.

Temperatura da pista e umidade podem ser importantes para entender como as condições climáticas influenciam o desempenho dos pneus.

Posição antes e depois do pit stop serão analisadas para avaliar se a posição de corrida é afetada pela eficiência do pit stop.

4. Análise Exploratória (Exemplo)
Agora vamos realizar uma análise exploratória simples com base nos dados. Aqui estão algumas possíveis observações:

a. Tempo de volta e desgaste dos pneus
Com base na tabela gerada, vemos que, conforme o desgaste dos pneus aumenta, o tempo de volta também tende a ser mais alto. Isso sugere que o desgaste dos pneus afeta diretamente a performance na pista. Por exemplo:

Volta 1: Desgaste dos pneus de 26,7% e tempo de volta de 92,85 segundos.

Volta 5: Desgaste dos pneus de 31,71% e tempo de volta de 87,81 segundos.

Essa correlação entre o desgaste dos pneus e o tempo de volta é importante para determinar o momento ideal para a troca de pneus.

b. Temperatura da pista e umidade
A temperatura da pista pode influenciar na aderência dos pneus e, consequentemente, no desgaste. Além disso, a umidade do ar também pode afetar a tração dos pneus. Esses fatores precisam ser analisados para ajustar a estratégia de pit stop. Por exemplo, a Volta 4 tem uma temperatura de pista de 23,09°C, que é bem mais baixa do que as outras voltas, sugerindo que a aderência dos pneus pode ser diferente devido à menor temperatura da pista.

c. Posição antes e depois do pit stop
Analisando as posições antes e depois do pit stop, podemos observar o impacto dos pit stops na posição do carro. Por exemplo:

Volta 2: A posição antes do pit stop é 9, mas após o pit stop, o carro cai para a 20ª posição. Esse grande impacto na posição pode indicar um tempo de pit stop mais longo ou um erro estratégico.

Volta 4: A posição antes do pit stop é 4, e depois da parada, o carro melhora para a 7ª posição, o que pode indicar uma parada eficiente ou uma vantagem estratégica.

5. Preparação dos Dados (Limpeza e Transformação)
Para modelagem, precisaremos realizar a limpeza e transformação dos dados:

Verificar valores ausentes ou inconsistentes e tratar conforme necessário.

Normalizar ou padronizar variáveis como tempo_volta e desgaste_pneu, pois elas podem ter escalas diferentes e precisam ser compatíveis para modelagem.

Criar novas variáveis que possam ser úteis, como a diferença de posições antes e depois do pit stop para avaliar a eficiência da estratégia de pit stop.

Conclusão
Com os dados prontos, podemos usar técnicas de machine learning para prever o melhor momento para realizar o pit stop. Isso poderia envolver algoritmos de regressão ou de classificação, dependendo de como o problema é formulado (ex.: prever a posição após o pit stop ou prever a necessidade de pit stop em cada volta).

Essas etapas de Entendimento e Preparação de Dados são fundamentais para construir um modelo robusto que auxilie nas decisões estratégicas de pit stop nas corridas de Fórmula 1.
 
