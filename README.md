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

## Contato

Para mais questões/comentários ou correções acionar o contato abaixo, Hudson Barroso:
hudson.g4@gmail.com
"""
