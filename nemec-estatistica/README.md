# Estatística para Data Science e IA — Fernando Nemec

Notebooks de estudo baseados no livro *Estatística para Data Science e Inteligência Artificial*, do Prof. Fernando Nemec (FIAP). Implementações práticas em Python via Google Colab, acompanhando a leitura capítulo por capítulo.

Estudo autodidata: cada notebook cobre a teoria testada na prática mais a resolução dos Exercícios Propostos do capítulo.

---

## Sobre o dataset

Vários exercícios usam o dataset `jogadores_futebol.csv`, referenciado no livro (Tabela 2.8 / 3.11) mas não disponibilizado no repositório do autor. Por isso ele foi recriado seguindo a estrutura oficial descrita no livro.

Estrutura (7 colunas): `nome_jogador`, `time`, `ano`, `gols_marcados`, `faltas_cometidas`, `cartoes_amarelos`, `cartoes_vermelhos`. Contém 20 times do Brasileirão Série A, 15 jogadores por time, temporadas de 2021 a 2025 (1500 registros).

---

## Sumário

### Cap. 1 — Data Science e Inteligência Artificial
Capítulo introdutório e conceitual, sem código. Não possui notebook.

### Cap. 2 — Ferramentas na Prática — `cap02-ferramentas-pratica.ipynb`
- Primeiros passos no Google Colab
- Pandas e Matplotlib: o kit essencial
- Conhecendo o Matplotlib: gráfico de linhas, barras e dispersão
- Conceituação estatística: amostras, classificação estatística, forma dos dados
- Exercícios Propostos

### Cap. 3 — Medições e Distribuições Estatísticas — `cap03-medicoes-distribuicoes.ipynb`
- Estimativas de localização: média, média ponderada, mediana, moda, média aparada, percentil
- Definição de outliers
- Estimativas de variabilidade: desvio padrão, graus de liberdade, variância, amplitude
- Distribuições estatísticas: histograma, normal/gaussiana, densidade de probabilidade, binomial, Poisson, exponencial, assimetria, curtose
- Bootstrap e intervalo de confiança para estimativas
- Teorema Central do Limite
- Exercícios Propostos

### Cap. 4 — Probabilidade, Amostragem e Viés — `cap04-probabilidade-amostragem-vies.ipynb`
- Probabilidade: espaço amostral, eventos, eventos dependentes e independentes, arranjo e combinação, eventos compostos, probabilidade complementar, regra do produto, regra da soma, probabilidade condicional, Teorema de Bayes
- Amostragem: principais métodos, amostragem na prática, representatividade da amostra, viés de amostragem
- Exercícios Propostos

### Cap. 5 — Ferramentas Estatísticas Essenciais — `cap05-ferramentas-estatisticas.ipynb`
- O que são correlações? Variáveis de confusão e correlações espúrias
- Pearson, Spearman e Kendall Tau
- Correlação parcial: matriz de correlação
- Análise de outliers: classificação, quando tratar, detecção univariada e multivariada, tratamento
- Exercícios Propostos

### Cap. 6 — Testes de Hipótese — `cap06-testes-hipotese.ipynb`
- O que é um teste de hipótese; modelagem, tipos de erro, intervalo de confiança, p-valor, nível de significância, tipos de teste
- Teste T de Student (pareadas, independentes, uma amostra, pressupostos)
- Normalidade e homocedasticidade: Shapiro-Wilk, Levene
- Teste de Welch
- Testes não paramétricos: Mann-Whitney, Wilcoxon
- Testes para múltiplos grupos: Teste F, ANOVA (e variações), Kruskal-Wallis, Friedman, post-hoc
- Medidas de tamanho de efeito: D de Cohen, Delta de Glass, Delta de Cliff, correlação rank bisserial
- Qui-Quadrado de Pearson e V de Cramer; interpretação do p-valor
- Exercícios Propostos

### Cap. 7 — Análise Exploratória de Dados — `cap07-analise-exploratoria.ipynb`
- Limpeza e tratamento de dados: dados ausentes, padronização e normalização, correção de erros e inconsistências
- Feature engineering: criação de novas variáveis, transformações matemáticas, estratificação, variáveis categóricas, variáveis temporais
- Exercícios Propostos

---

## Ferramentas

Python · Pandas · NumPy · Matplotlib · SciPy · Google Colab

## Status

| Capítulo | Status |
|---|---|
| 1 — Data Science e IA | Sem notebook (conceitual) |
| 2 — Ferramentas na Prática | Concluído |
| 3 — Medições e Distribuições | Concluído |
| 4 — Probabilidade, Amostragem e Viés | A fazer |
| 5 — Ferramentas Estatísticas Essenciais | A fazer |
| 6 — Testes de Hipótese | A fazer |
| 7 — Análise Exploratória de Dados | A fazer |
