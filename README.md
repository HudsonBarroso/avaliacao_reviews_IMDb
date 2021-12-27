## Avaliação e Classificação de reviews IMDb v1.

## Overview

Esse projeto tem como objetivo a classificação de reviews de filmes,

Nele farei um pipeline com alguns dos processos mais importantes em Ciência de Dados,
Iniciaremos com o carregamento dos dados

## Dataset

Esta coleção de dados está disponível em http://ai.stanford.edu/~amaas/data/sentiment/

Existem 50,000 reviews de filmes que estão separados em:

    train = 25,000    
        pos = 12,500        
        neg = 12,500

    test = 25,000    
        pos = 12,500        
        neg = 12,500
        
Para criação deste dataset foi usada a seguinte regra:

    Review Negativa = Seu score é <= 4, em uma faixa de 10    
    Review Positiva = Seu score é >= 7, em uma faixa de 10
    
    * Os resultados mais neutros não foram incluídos nesta coleção

Acesse o diretório train

Dentro da pasta: data, está o arquivo que contém os reviews

Dentro da pasta: notebooks, estão os notebooks em jupyter utilizados para fazer a análise experimentos

Dentro da pasta: models, está o modelo utilizado e os aquivos .pkl

Dentro da pasta: scripts: estão os scripts em python utilizados para treinar o modelo

Dentro da pasta: input_new, devem ser inseridos os novos arquivos a serem carregados


O arquivo main.py contém todo o pipeline para o treinamento e ao final dele, pode ser carregado o novo arquivo para a classificação.

Breve descrição dos processos utilizados:

    1. Carregamento dos dados
    2. Criação do DataFrame pandas
    3. EDA
    4. Suffle, ao fazer um EDA simples, percebi que os dados estavam ordenados por classificação, então apliquei o metodo shuffle do sklearn
    5. Com os dados devidamente embaralhados, através do value_counts() pude averiguar que as classes estavam balanceadas
    6. Pre-Processamento
        6.1. Remoção de Tags HTML
        6.2. Remoção de pontuação
        6.3. Remoção de dígitos dentro de palavras
        6.4. Remoção de espaços extras
        6.5. Conversão do texto para lowercase
     7. TfidfVectorizer, antes de criar o modelo realizei alguns testes com vetorização e a que melhor se saiu foi a TfidfVectorizer
        7.1. stop_words, ao chamar esse parâmetro, ele carrega uma lista pronta de palavras que não devem entrar no modelo
        7.2. preprocessro, ao chamar esse parâmetro, ele executa a função de limpeza de texto que corresponde ao pre-processamento
     8. Modelagem, foram testados vários modelos, aqui uma descrição de nome e sua acurácia:
        8.1. RidgeClassifier -> 75.69
        8.2. LinearSVC -> 83.49
        8.3. PassiveAggressiveClassifier -> 84.02
        8.4. LogisticRegression + TfidfVectorizer -> 87.57 (Modelo Escolhido)
        
            

## Contato

Para mais questões/comentários ou correções acionar o contato abaixo, Hudson Barroso:
hudson.g4@gmail.com
"""
