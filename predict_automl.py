from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
import pandas as pd
import scikitplot as skplt

df_test = pd.read_csv('Test_20/test_set.csv')

X_test = df_test[df_test.columns[1:]]
y_test = df_test[df_test.columns[0]]

automl = AutoML(results_path="AutoML_compete_logloss")
predictions = automl.predict(X_test)

_ = skplt.metrics.plot_confusion_matrix(y_test, predictions, normalize=False)
print("Test accuracy:", accuracy_score(y_test, predictions.astype(int)))
