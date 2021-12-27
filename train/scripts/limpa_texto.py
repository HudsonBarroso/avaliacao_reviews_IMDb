import re

# Nesta função realizarei os mais importantes processos de pre-processamento:
#   1. Remoção de caracteres inviáveis
#   2. remoação de pontuação em palavras
#   3. Conversão para minúsculo


def limpa_texto(text):
    # remove tags do HTML
    text = re.sub(r'<.*?>', '', text)
    # remove os caracteres (\), (') e (")
    text = re.sub(r"\\", "", text)
    text = re.sub(r"\'", "", text)
    text = re.sub(r"\"", "", text)
    # converte o texto para lowercase
    text = text.strip().lower()
    # remove os caracteres de pontuação
    filters = '!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    translate_dict = dict((c, " ") for c in filters)
    translate_map = str.maketrans(translate_dict)
    text = text.translate(translate_map)
    # remove dígitos dentro de uma palavra, exemplo brasil123 = brasil
    text = re.sub('W*dw*', '', text)
    # remove espaços extras
    text = re.sub(' +', ' ', text)

    return text