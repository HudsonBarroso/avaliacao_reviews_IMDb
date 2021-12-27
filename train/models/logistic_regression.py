from time import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def logistic_regression(X_train, X_test, y_train, y_test):
    start = time()
    model = LogisticRegression(verbose=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(y_pred)
    # Avaliação com a acurácia
    acc = accuracy_score(y_test, y_pred)
    print('Tempo: {:.2f}s\n'.format(time() - start))
    print("Acurácia do modelo LogisticRegression: {:.2f}".format(acc * 100))
    print(classification_report(y_test, model.predict(X_test), target_names=['Negative -1', 'Positive 1']))
    return model