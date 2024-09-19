import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score

#Load the training set and validation set

df_train = pd.read_csv('Train_60/train_set.csv')
df_test = pd.read_csv('Test_20/test_set.csv')

X_train = df_train[df_train.columns[1:]]
X_test = df_test[df_test.columns[1:]]

y_train = df_train[df_train.columns[0]]
y_test = df_test[df_test.columns[0]]

print(X_train.head())
print(y_train.head())

#Train the models and optimize based on the time limits

automl = AutoML(mode="Explain",algorithms=[
        "Baseline",
        "Xgboost",
        "Linear",
        "Decision Tree",
        "Random Forest",
        "Neural Network",
        "CatBoost",
        "Extra Trees",
        "LightGBM",
        "Nearest Neighbors"],
        #eval_metric="accuracy",
        total_time_limit=345600,
        train_ensemble=True)

automl.fit(X_train, y_train)

predictions = automl.predict(X_test)

print("Test accuracy:", accuracy_score(y_test, predictions.astype(int)))