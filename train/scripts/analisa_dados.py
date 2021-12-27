# Neste script será realizado uma análise inicial dos dados
#   1. Verificar o tamanho do dataset
#   2. Visualizar os 5 primeiros dados
#   3. Visualizar os 5 últimos dados
#   4. Verificar se sexistem dados faltantes do dataset


def analisa_dados(data):
    print('Tamanho do dataset:\n', data.shape)
    print('\nVisualização dos 5 primeiros dados:\n', data.head())
    print('\nVisualização dos 5 últimos dados:\n', data.tail())
    print('\nExistem valores faltantes?', data.isnull().any().any())