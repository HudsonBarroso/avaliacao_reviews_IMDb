import io, os
import streamlit as st
from sklearn.utils import shuffle
import numpy as np
import pandas as pd
import pickle

# Criando um título para nosso projeto

st.title("Classificador de Comentário")
st.write('''
### Carregue um arquivo de texto para realizar a classificação!
''')
uploaded_file = st.file_uploader("Buscar arquivo")
if uploaded_file:
    # To convert to a string based IO:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

def user_input_features():
    data ={
        'text':uploaded_file,
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Carregamento dos dados

def load_data(data_dir):
    data = {}
    for split in ["train", "test"]:
        data[split] = []
        for sentiment in ["neg", "pos"]:
            if sentiment == 'pos':
                score = 1
            else:
                score = -1
            path = os.path.join(data_dir, split, sentiment)
            file_names = os.listdir(path)
            for f_name in file_names:
                with open(os.path.join(path, f_name), "r", encoding="utf-8") as f:
                    review = f.read()
                    data[split].append([review, score])
    return data["train"], data["test"]

data_dir = './train/data/aclImdb/'
train_data, test_data = load_data(data_dir)

# Criação de DataFrame dos Pandas
test_data = pd.DataFrame(test_data,columns=['text', 'sentiment'])

# Aqui faremos o "embaralhamento" dos dados, pois estão ordenados por classificação
test_data = shuffle(test_data)
test_data.reset_index(inplace=True, drop=True)

input_df =user_input_features()

# lendo o dataset de teste
review_test = pd.DataFrame(test_data)
#review_test = test_data
# concatenando os dados do usuário com os dados do dataset de teste
df = pd.concat([input_df, review_test], axis=0)

# selecionando a primeira linha (o valor inserido pelo usuário)
df = df[:1]

# realizando a leitura do modelo salvo
load_logisticRegression = pickle.load(open('logistic_model.pkl', 'rb'))

# aplicando o modelo para realizar a previsão

prediction = load_logisticRegression.predict(input_df)
prediction_probability = load_logisticRegression.predict_proba(input_df)

st.subheader('Previsão')
result = np.array(['Você provavelmente não será promovido.','Você será promovido!'])
st.write(result[prediction][0])

st.subheader('Probabilidade da Previsão')
st.write('Baseado nos dados selecionados,\nvocê tem {0:.2f}% de chances de ser promovido.'.format(
    prediction_probability[0][1] * 100))




