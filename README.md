## Stacked-Ensemble GSTN Modeling and Classification
The given submission is submission by **Shreyasvi Natraj** for the GSTN Hackathon on Predictive Modeling and Classification.

### Usage
In order to use the scripts for training and prediction, please follow the following steps:
- Install dependencies using `pip install -r requirements.txt`
- Download the dataset (in `.csv` format) and add the `target` variable column into the column with `input` data i.e. combine the two `.csv` files so that the target is the first column and the inputs are the following columns.
- Run training using `python train_automl.py`
- Once the model has been trained, you will obtain an `AutoML_1` folder.
- Carry out prediction by changing the output folder path in the `predict_automl.py` script as well as the CSV file to be used for prediction.
- Run prediction script using `python predict_automl.py`
The resultant accuracy over test data can be observed in the command prompt.

### Results
As a part of the project submission, we tested out the following machine learning models to obtain the final stacked ensemble machine learning model.

| Best model   | name                                                                                             | model_type     | metric_type   |   metric_value |
|:-------------|:-------------------------------------------------------------------------------------------------|:---------------|:--------------|---------------:|
| **the best** | Ensemble_Stacked                                                  | Ensemble       | logloss       |      0.0487711 |
|              | 1_Baseline                                                               | Baseline       | logloss       |      0.312361  |
|              | 2_DecisionTree                                                      | Decision Tree  | logloss       |      0.0609345 |
|              | 3_DecisionTree                                                       | Decision Tree  | logloss       |      0.0590441 |
|              | 4_DecisionTree                                                      | Decision Tree  | logloss       |      0.0590441 |
|              | 5_Default_LightGBM                                              | LightGBM       | logloss       |      0.0491674 |
|              | 6_Default_Xgboost                                                | Xgboost        | logloss       |      0.049337  |
|              | 7_Default_CatBoost                                          | CatBoost       | logloss       |      0.0494532 |
|              | 8_Default_NeuralNetwork                                    | Neural Network | logloss       |      0.0601199 |
|              | 9_Default_RandomForest                                       | Random Forest  | logloss       |      0.0583586 |
|              | 10_Default_ExtraTrees                                        | Extra Trees    | logloss       |      0.126521  |
|              | 20_LightGBM                                                            | LightGBM       | logloss       |      0.0493681 |
|              | 11_Xgboost                                                             | Xgboost        | logloss       |      0.0492229 |
|              | 29_CatBoost                                                            | CatBoost       | logloss       |      0.0492586 |
|              | 38_RandomForest                                                   | Random Forest  | logloss       |      0.0594859 |
|              | 47_ExtraTrees                                                        | Extra Trees    | logloss       |      0.152036  |
|              | 56_NeuralNetwork                                                  | Neural Network | logloss       |      0.0603064 |
|              | 21_LightGBM                                                            | LightGBM       | logloss       |      0.0497553 |
|              | 12_Xgboost                                                               | Xgboost        | logloss       |      0.0492996 |
|              | 30_CatBoost                                                             | CatBoost       | logloss       |      0.0493382 |
|              | 39_RandomForest                                                    | Random Forest  | logloss       |      0.0545888 |
|              | 48_ExtraTrees                                                        | Extra Trees    | logloss       |      0.107614  |
|              | 57_NeuralNetwork                                                 | Neural Network | logloss       |      0.0553636 |
|              | 22_LightGBM                                                            | LightGBM       | logloss       |      0.0491429 |
|              | 13_Xgboost                                                              | Xgboost        | logloss       |      0.0494136 |
|              | 31_CatBoost                                                            | CatBoost       | logloss       |      0.049365  |
|              | 40_RandomForest                                                   | Random Forest  | logloss       |      0.0603571 |
|              | 49_ExtraTrees                                                        | Extra Trees    | logloss       |      0.132285  |
|              | 58_NeuralNetwork                                                  | Neural Network | logloss       |      0.0660043 |
|              | 23_LightGBM                                                           | LightGBM       | logloss       |      0.0491101 |
|              | 14_Xgboost                                                              | Xgboost        | logloss       |      0.0497537 |
|              | 32_CatBoost                                                           | CatBoost       | logloss       |      0.0495029 |
|              | 41_RandomForest                                                   | Random Forest  | logloss       |      0.0557619 |
|              | 50_ExtraTrees                                                         | Extra Trees    | logloss       |      0.114447  |
|              | 59_NeuralNetwork                                                  | Neural Network | logloss       |      0.0604965 |
|              | 24_LightGBM                                                            | LightGBM       | logloss       |      0.04965   |
|              | 15_Xgboost                                                               | Xgboost        | logloss       |      0.0495772 |
|              | 33_CatBoost                                                            | CatBoost       | logloss       |      0.0494204 |
|              | 42_RandomForest                                                     | Random Forest  | logloss       |      0.0603542 |
|              | 51_ExtraTrees                                                        | Extra Trees    | logloss       |      0.148196  |
|              | 60_NeuralNetwork                                                   | Neural Network | logloss       |      0.0552701 |
|              | 25_LightGBM                                                           | LightGBM       | logloss       |      0.0491614 |
|              | 16_Xgboost                                                             | Xgboost        | logloss       |      0.0497153 |
|              | 34_CatBoost                                                           | CatBoost       | logloss       |      0.0497611 |
|              | 43_RandomForest                                                    | Random Forest  | logloss       |      0.0547039 |
|              | 52_ExtraTrees                                                     | Extra Trees    | logloss       |      0.0789727 |
|              | 61_NeuralNetwork                                                 | Neural Network | logloss       |      0.0553963 |
|              | 26_LightGBM                                                            | LightGBM       | logloss       |      0.0491129 |
|              | 17_Xgboost                                                            | Xgboost        | logloss       |      0.049253  |
|              | 35_CatBoost                                                             | CatBoost       | logloss       |      0.0492967 |
|              | 44_RandomForest                                                     | Random Forest  | logloss       |      0.0569874 |
|              | 53_ExtraTrees                                                       | Extra Trees    | logloss       |      0.0961841 |
|              | 62_NeuralNetwork                                                  | Neural Network | logloss       |      0.0558558 |
|              | 27_LightGBM                                                             | LightGBM       | logloss       |      0.0494392 |
|              | 18_Xgboost                                                              | Xgboost        | logloss       |      0.0494464 |
|              | 36_CatBoost                                                          | CatBoost       | logloss       |      0.0493499 |
|              | 45_RandomForest                                                     | Random Forest  | logloss       |      0.0587882 |
|              | 54_ExtraTrees                                                       | Extra Trees    | logloss       |      0.147102  |
|              | 63_NeuralNetwork                                                   | Neural Network | logloss       |      0.0690673 |
|              | 28_LightGBM                                                             | LightGBM       | logloss       |      0.0493859 |
|              | 19_Xgboost                                                            | Xgboost        | logloss       |      0.0491711 |
|              | 37_CatBoost                                                           | CatBoost       | logloss       |      0.049334  |
|              | 46_RandomForest                                                   | Random Forest  | logloss       |      0.0572454 |
|              | 55_ExtraTrees                                                      | Extra Trees    | logloss       |      0.141972  |
|              | 64_NeuralNetwork                                                 | Neural Network | logloss       |      0.064335  |
|              | 23_LightGBM_GoldenFeatures                               | LightGBM       | logloss       |      0.0491834 |
|              | 26_LightGBM_GoldenFeatures                              | LightGBM       | logloss       |      0.0491301 |
|              | 22_LightGBM_GoldenFeatures                               | LightGBM       | logloss       |      0.0491742 |
|              | 23_LightGBM_KMeansFeatures                               | LightGBM       | logloss       |      0.0493071 |
|              | 26_LightGBM_KMeansFeatures                             | LightGBM       | logloss       |      0.0492521 |
|              | 22_LightGBM_KMeansFeatures                             | LightGBM       | logloss       |      0.0492239 |
|              | 23_LightGBM_RandomFeature                                | LightGBM       | logloss       |      0.0492587 |
|              | 23_LightGBM_SelectedFeatures                           | LightGBM       | logloss       |      0.0491752 |
|              | 19_Xgboost_SelectedFeatures                           | Xgboost        | logloss       |      0.0491888 |
|              | 29_CatBoost_SelectedFeatures                           | CatBoost       | logloss       |      0.0492449 |
|              | 39_RandomForest_SelectedFeatures                  | Random Forest  | logloss       |      0.054514  |
|              | 60_NeuralNetwork_SelectedFeatures                 | Neural Network | logloss       |      0.0552919 |
|              | 52_ExtraTrees_SelectedFeatures                       | Extra Trees    | logloss       |      0.0594756 |
|              | 65_LightGBM                                                           | LightGBM       | logloss       |      0.0492367 |
|              | 66_LightGBM                                                         | LightGBM       | logloss       |      0.04921   |
|              | 67_LightGBM_GoldenFeatures                               | LightGBM       | logloss       |      0.0492746 |
|              | 68_Xgboost                                                            | Xgboost        | logloss       |      0.0492456 |
|              | 69_Xgboost                                                              | Xgboost        | logloss       |      0.0491114 |
|              | 70_Xgboost_SelectedFeatures                             | Xgboost        | logloss       |      0.049288  |
|              | 71_Xgboost_SelectedFeatures                             | Xgboost        | logloss       |      0.0491591 |
|              | 72_Xgboost                                                               | Xgboost        | logloss       |      0.04926   |
|              | 73_Xgboost                                                               | Xgboost        | logloss       |      0.0492431 |
|              | 74_CatBoost_SelectedFeatures                           | CatBoost       | logloss       |      0.0492631 |
|              | 75_CatBoost_SelectedFeatures                           | CatBoost       | logloss       |      0.0492082 |
|              | 76_CatBoost                                                            | CatBoost       | logloss       |      0.049313  |
|              | 77_CatBoost                                                            | CatBoost       | logloss       |      0.0492504 |
|              | 78_CatBoost                                                           | CatBoost       | logloss       |      0.0493563 |
|              | 79_CatBoost                                                            | CatBoost       | logloss       |      0.049248  |
|              | 80_RandomForest_SelectedFeatures                   | Random Forest  | logloss       |      0.0546304 |
|              | 81_RandomForest_SelectedFeatures                   | Random Forest  | logloss       |      0.0545376 |
|              | 82_RandomForest                                                    | Random Forest  | logloss       |      0.0546737 |
|              | 83_RandomForest                                                     | Random Forest  | logloss       |      0.0545493 |
|              | 84_RandomForest                                                     | Random Forest  | logloss       |      0.0545742 |
|              | 85_NeuralNetwork                                                   | Neural Network | logloss       |      0.0555424 |
|              | 86_NeuralNetwork                                                   | Neural Network | logloss       |      0.0553746 |
|              | 87_NeuralNetwork_SelectedFeatures                 | Neural Network | logloss       |      0.0557844 |
|              | 88_NeuralNetwork_SelectedFeatures                 | Neural Network | logloss       |      0.055366  |
|              | 89_NeuralNetwork                                                  | Neural Network | logloss       |      0.0553591 |
|              | 90_NeuralNetwork                                                  | Neural Network | logloss       |      0.0553378 |
|              | 91_ExtraTrees_SelectedFeatures                       | Extra Trees    | logloss       |      0.0614885 |
|              | 92_DecisionTree                                                    | Decision Tree  | logloss       |      0.0651356 |
|              | 93_ExtraTrees                                                         | Extra Trees    | logloss       |      0.0890991 |
|              | 94_ExtraTrees                                                        | Extra Trees    | logloss       |      0.11526   |
|              | 95_ExtraTrees                                                         | Extra Trees    | logloss       |      0.103739  |
|              | 96_LightGBM                                                           | LightGBM       | logloss       |      0.0491101 |
|              | 97_Xgboost                                                              | Xgboost        | logloss       |      0.0491421 |
|              | 98_Xgboost                                                              | Xgboost        | logloss       |      0.0491562 |
|              | 99_LightGBM                                                            | LightGBM       | logloss       |      0.0491129 |
|              | 100_LightGBM                                                          | LightGBM       | logloss       |      0.0491129 |
|              | 101_LightGBM_GoldenFeatures                            | LightGBM       | logloss       |      0.0491301 |
|              | 102_LightGBM_GoldenFeatures                             | LightGBM       | logloss       |      0.0491301 |
|              | 103_Xgboost_SelectedFeatures                         | Xgboost        | logloss       |      0.0491326 |
|              | 104_Xgboost_SelectedFeatures                           | Xgboost        | logloss       |      0.0492602 |
|              | 105_Xgboost                                                             | Xgboost        | logloss       |      0.0491606 |
|              | 106_Xgboost                                                             | Xgboost        | logloss       |      0.0492284 |
|              | 107_CatBoost_SelectedFeatures                         | CatBoost       | logloss       |      0.0492177 |
|              | 108_CatBoost_SelectedFeatures                         | CatBoost       | logloss       |      0.0492891 |
|              | 109_CatBoost_SelectedFeatures                         | CatBoost       | logloss       |      0.0492632 |
|              | 110_CatBoost_SelectedFeatures                         | CatBoost       | logloss       |      0.0493181 |
|              | 111_CatBoost                                                           | CatBoost       | logloss       |      0.0492547 |
|              | 112_RandomForest_SelectedFeatures                 | Random Forest  | logloss       |      0.0545758 |
|              | 113_RandomForest_SelectedFeatures                 | Random Forest  | logloss       |      0.0544598 |
|              | 114_RandomForest                                                   | Random Forest  | logloss       |      0.0545016 |
|              | 115_ExtraTrees_SelectedFeatures                     | Extra Trees    | logloss       |      0.0596076 |
|              | 116_ExtraTrees_SelectedFeatures                     | Extra Trees    | logloss       |      0.0612883 |
|              | 117_ExtraTrees                                                       | Extra Trees    | logloss       |      0.0706535 |
|              | 96_LightGBM_BoostOnErrors                                 | LightGBM       | logloss       |      0.0491283 |
|              | Ensemble                                                                   | Ensemble       | logloss       |      0.0488402 |
|              | 96_LightGBM_Stacked                                            | LightGBM       | logloss       |      0.0491743 |
|              | 69_Xgboost_Stacked                                               | Xgboost        | logloss       |      0.049114  |
|              | 75_CatBoost_SelectedFeatures_Stacked           | CatBoost       | logloss       |      0.0489716 |
|              | 113_RandomForest_SelectedFeatures_Stacked | Random Forest  | logloss       |      0.0488156 |
|              | 60_NeuralNetwork_Stacked                                   | Neural Network | logloss       |      0.0500318 |
|              | 52_ExtraTrees_SelectedFeatures_Stacke       | Extra Trees    | logloss       |      0.0488204 |
|              | 23_LightGBM_Stacked                                          | LightGBM       | logloss       |      0.0491743 |
|              | 103_Xgboost_SelectedFeatures_Stacked           | Xgboost        | logloss       |      0.0491199 |
|              | 107_CatBoost_SelectedFeatures_Stacked        | CatBoost       | logloss       |      0.0489441 |
|              | 114_RandomForest_Stacked                                  | Random Forest  | logloss       |      0.0488296 | 
|              | 60_NeuralNetwork_SelectedFeatures_Stacked | Neural Network | logloss       |      0.0499325 |
|              | 115_ExtraTrees_SelectedFeatures_Stacked    | Extra Trees    | logloss       |      0.0488098 |
|              | 100_LightGBM_Stacked                                          | LightGBM       | logloss       |      0.0491362 |
|              | 97_Xgboost_Stacked                                              | Xgboost        | logloss       |      0.0491515 |
|              | 29_CatBoost_SelectedFeatures_Stacked           | CatBoost       | logloss       |      0.0489571 |
|              | 39_RandomForest_SelectedFeatures_Stacked   | Random Forest  | logloss       |      0.0488591 |
|              | 90_NeuralNetwork_Stacked                                 | Neural Network | logloss       |      0.0499736 |
|              | 116_ExtraTrees_SelectedFeatures_Stacked     | Extra Trees    | logloss       |      0.0488176 |
|              | 99_LightGBM_Stacked                                           | LightGBM       | logloss       |      0.0491362 |
|              | 98_Xgboost_Stacked                                              | Xgboost        | logloss       |      0.0491187 |
|              | 79_CatBoost_Stacked                                           | CatBoost       | logloss       |      0.0489624 |
|              | 81_RandomForest_SelectedFeatures_Stacked   | Random Forest  | logloss       |      0.0488645 |
|              | 89_NeuralNetwork_Stacked                                  | Neural Network | logloss       |      0.050004  |
|              | 91_ExtraTrees_SelectedFeatures_Stacked       | Extra Trees    | logloss       |      0.0488152 |
|              | 26_LightGBM_Stacked                                           | LightGBM       | logloss       |      0.0491362 |
|              | 71_Xgboost_SelectedFeatures_Stacked             | Xgboost        | logloss       |      0.0491214 |
|              | 77_CatBoost_Stacked                                            | CatBoost       | logloss       |      0.0489713 |
|              | 83_RandomForest_Stacked                                     | Random Forest  | logloss       |      0.048857  |
|              | 57_NeuralNetwork_Stacked                                   | Neural Network | logloss       |      0.0499082 |
|              | 117_ExtraTrees_Stacked                                    | Extra Trees    | logloss       |      0.0488144 |
|              | 102_LightGBM_GoldenFeatures_Stacked            | LightGBM       | logloss       |      0.0491697 |
|              | 105_Xgboost_Stacked                                           | Xgboost        | logloss       |      0.049077  |
|              | 111_CatBoost_Stacked                                           | CatBoost       | logloss       |      0.0489798 |
|              | 84_RandomForest_Stacked                                    | Random Forest  | logloss       |      0.0488622 |
|              | 88_NeuralNetwork_SelectedFeatures_Stacked | Neural Network | logloss       |      0.0500559 |
|              | 52_ExtraTrees_Stacked                                        | Extra Trees    | logloss       |      0.048809  |
|              | 26_LightGBM_GoldenFeatures_Stacked               | LightGBM       | logloss       |      0.0491697 |
|              | 19_Xgboost_Stacked                                             | Xgboost        | logloss       |      0.0490235 |
|              | 29_CatBoost_Stacked                                            | CatBoost       | logloss       |      0.0490018 |
|              | 112_RandomForest_SelectedFeatures_Stacked | Random Forest  | logloss       |      0.0488292 |
|              | 86_NeuralNetwork_Stacked                                   | Neural Network | logloss       |      0.049863  |
|              | 93_ExtraTrees_Stacked                                        | Extra Trees    | logloss       |      0.0488102 |
|              | 101_LightGBM_GoldenFeatures_Stacked             | LightGBM       | logloss       |      0.0491697 |
|              | 19_Xgboost_SelectedFeatures_Stacked             | Xgboost        | logloss       |      0.0490382 |
|              | 74_CatBoost_SelectedFeatures_Stacked           | CatBoost       | logloss       |      0.0489488 |
|              | 39_RandomForest_Stacked                                     | Random Forest  | logloss       |      0.0488556 |
|              | 61_NeuralNetwork_Stacked                                   | Neural Network | logloss       |      0.0502849 |
|              | 53_ExtraTrees_Stacked                                         | Extra Trees    | logloss       |      0.0488633 |
|              | 22_LightGBM_Stacked                                            | LightGBM       | logloss       |      0.0490944 |
|              | 11_Xgboost_Stacked                                             | Xgboost        | logloss       |      0.0491853 |
|              | 109_CatBoost_SelectedFeatures_Stacked         | CatBoost       | logloss       |      0.0489601 |
|              | 80_RandomForest_SelectedFeatures_Stacked   | Random Forest  | logloss       |      0.0488611 |
|              | 85_NeuralNetwork_Stacked                                   | Neural Network | logloss       |      0.0496906 |
|              | 95_ExtraTrees_Stacked                                         | Extra Trees    | logloss       |      0.0488694 |
|              | 106_Xgboost_Stacked                                            | Xgboost        | logloss       |      0.0490517 |
|              | 108_CatBoost_SelectedFeatures_Stacked         | CatBoost       | logloss       |      0.0490226 |
|              | 82_RandomForest_Stacked                                     | Random Forest  | logloss       |      0.0488677 |
|              | 87_NeuralNetwork_SelectedFeatures_Stacked | Neural Network | logloss       |      0.0499196 |
|              | 48_ExtraTrees_Stacked                                        | Extra Trees    | logloss       |      0.0488159 |


The best trained stacked-ensemble model's results are described below:

#### Ensemble structure
| Model                                     |   Weight |
|:------------------------------------------|---------:|
| 113_RandomForest_SelectedFeatures_Stacked |       54 |
| 114_RandomForest_Stacked                  |       12 |
| 115_ExtraTrees_SelectedFeatures_Stacked   |       14 |
| 117_ExtraTrees_Stacked                    |       29 |
| 22_LightGBM_KMeansFeatures                |       13 |
| 23_LightGBM_KMeansFeatures                |        1 |
| 25_LightGBM                               |       19 |
| 52_ExtraTrees_Stacked                     |       40 |
| Ensemble                                  |        1 |

#### Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0487711 | nan           |
| auc       | 0.994939  | nan           |
| f1        | 0.890978  |   0.399357    |
| accuracy  | 0.978369  |   0.560246    |
| precision | 0.993911  |   0.971979    |
| recall    | 1         |   7.03518e-08 |
| mcc       | 0.881903  |   0.399357    |


#### Confusion matrix (at threshold=0.560246)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           700354 |            10746 |
| Labeled as 1 |             6237 |            67796 |


### Miscellaneous
We initially carried out benchmarking using using [LazyPredict](https://github.com/shankarpandala/lazypredict) which was used for model selection. These models were then utillized along with feature engineering, stacking and ensembling to obtain the final model.
LazyPredict can be run over the dataset using `utils/run_lazy.py` over the dataset.

The initial results from LazyPredict are as follows:
```
Model                              Accuracy  Balanced Accuracy  ROC AUC  F1 Score  Time Taken
LinearDiscriminantAnalysis         0.96               0.98     0.98      0.97        1.88
SGDClassifier                      0.97               0.96     0.96      0.97        2.52
LGBMClassifier                     0.98               0.96     0.96      0.98        2.24
SVC                                0.97               0.96     0.96      0.98     5951.60
XGBClassifier                      0.98               0.96     0.96      0.98        4.30
AdaBoostClassifier                 0.98               0.96     0.96      0.98       39.38
NearestCentroid                    0.96               0.95     0.95      0.97        1.08
RandomForestClassifier             0.98               0.95     0.95      0.98       62.20
QuadraticDiscriminantAnalysis      0.96               0.95     0.95      0.96        1.59
KNeighborsClassifier               0.97               0.94     0.94      0.97      121.77
ExtraTreesClassifier               0.97               0.94     0.94      0.97       57.46
LogisticRegression                 0.97               0.93     0.93      0.97        1.58
BernoulliNB                        0.97               0.93     0.93      0.97        1.10
GaussianNB                         0.96               0.93     0.93      0.96        1.28
LinearSVC                          0.97               0.93     0.93      0.97      228.62
BaggingClassifier                  0.97               0.93     0.93      0.97        9.49
CalibratedClassifierCV             0.97               0.92     0.92      0.97       22.52
Perceptron                         0.96               0.92     0.92      0.96        2.11
DecisionTreeClassifier             0.97               0.91     0.91      0.97        1.94
ExtraTreeClassifier                0.96               0.90     0.90      0.96        1.47
RidgeClassifier                    0.97               0.89     0.89      0.97        1.37
RidgeClassifierCV                  0.97               0.89     0.89      0.97        2.37
PassiveAggressiveClassifier        0.92               0.71     0.71      0.91        1.72
DummyClassifier                    0.91               0.50     0.50      0.86        0.79
```