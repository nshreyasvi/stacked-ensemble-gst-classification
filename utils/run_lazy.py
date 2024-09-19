from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

df_train = pd.read_csv('Train_60/train_set.csv')
df_test = pd.read_csv('Test_20/test_set.csv')

X_train = df_train[df_train.columns[1:]]
X_test = df_test[df_test.columns[1:]]

y_train = df_train[df_train.columns[0]]
y_test = df_test[df_test.columns[0]]

print(X_train.head())
print(y_train.head())

clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)