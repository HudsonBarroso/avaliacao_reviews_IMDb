from train.scripts.load_data import load_data
from train.scripts.analisa_dados import analisa_dados
from train.scripts.limpa_texto import limpa_texto
from train.models.logistic_regression import logistic_regression
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings("ignore")

# Carregamento dos dados
data_dir = './data/aclImdb/'
train_data, test_data = load_data(data_dir)

# Criação de DataFrame dos Pandas
train_data = pd.DataFrame(train_data, columns=['text', 'sentiment'])
test_data = pd.DataFrame(test_data,columns=['text', 'sentiment'])

# Uma primeira análise dos dados
analisa_dados(train_data)
analisa_dados(test_data)

# Aqui faremos o "embaralhamento" dos dados, pois estão ordenados por classificação
train_data = shuffle(train_data)
train_data.reset_index(inplace=True, drop=True)
test_data = shuffle(test_data)
test_data.reset_index(inplace=True, drop=True)

# Neste ponto faremos o TfidfVectorizer usamos ele para criar os vetores a partir dos reviews
# Neste processo também executaremos os seguintes parâmetros:
#   1. stop_words = usa uma lista de palavras que serão excluídas
#   2. preprocessor = ele executará a nossa função limpa_texto() que faz o pre-processamento dos dados

vectorizer = TfidfVectorizer(stop_words="english",
                             preprocessor=limpa_texto,
                             ngram_range=(1, 2))
training_features = vectorizer.fit_transform(train_data["text"])
test_features = vectorizer.transform(test_data["text"])

# Treinamento do modelo
model = logistic_regression(training_features, test_features, train_data["sentiment"], test_data['sentiment'])

# Salvando o modelo como pikkle
import joblib
joblib.dump(vectorizer, 'models/vectorizer.pkl', protocol=2)
joblib.dump(model, 'models/logistic_model.pkl', protocol=2)


def pred_new(text):
    text = vectorizer.transform([text])
    result = model.predict(text)
    final = '-1 Negative' if result[0] == -1 else '1 Positive'
    print('Resultado de previsão para o review selecionado: ', final)
    return final

# Realiza a predição de um novo review
with open('4_4.txt', 'r') as file:
    data = file.read()
print(data)

pred_new(data)




