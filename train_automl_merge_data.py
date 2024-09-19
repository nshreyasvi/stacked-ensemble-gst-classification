import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score

#Define training and validation sets

df_train = pd.read_csv('Train_60/train_set.csv')
df_test = pd.read_csv('Test_20/test_set.csv')

#Merge training and validation sets
df = pd.concat([df_train, df_test])

X_train = df[df.columns[1:]]
y_train = df[df.columns[0]]

print(len(X_train))

#Train and test machine learning models
automl = AutoML(mode="Compete",
        algorithms=[
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
