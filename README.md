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

- Classificação: Essa técnica é particularmente útil para prever se um tumor é maligno ou benigno, considerando atributos específicos como textura, compactação e raio das células. Algoritmos populares nessa tarefa incluem Árvores de Decisão e Máquinas de Vetores de Suporte (SVM). 

- Regressão: Embora a variável-alvo seja geralmente categórica, é possível aplicar técnicas de regressão para estimar a probabilidade de malignidade dos tumores, com base nas características contínuas disponíveis. Isso facilita a compreensão quantitativa do risco associado a determinados perfis celulares. 

- Clusterização: Permite agrupar pacientes com padrões celulares semelhantes, sem depender dos diagnósticos previamente rotulados. Essa abordagem é valiosa para identificar subgrupos específicos de risco, utilizando técnicas como o K-means ou o DBSCAN, que agrupam naturalmente indivíduos com características similares. 

- Regras de Associação: Técnicas de associação podem identificar padrões frequentes e relevantes entre as características celulares. Por exemplo, é possível descobrir regras indicando que, quando atributos como textura e simetria ultrapassam determinados limites, há maior probabilidade de malignidade, proporcionando insights clínicos úteis para diagnóstico precoce. 

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

 
