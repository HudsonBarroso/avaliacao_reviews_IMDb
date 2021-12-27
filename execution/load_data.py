import os

# Neste script será realizado o carregamento dos dados
#   1. Será acessada a pasta principal e faremos a separação entre train e test
#   2. Será acessada a pasta train e test e faremos a separação entre negativos e positivos
#   3. Para os reviews positivos, atribuiremos a label 1 e para os negativos a label -1

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