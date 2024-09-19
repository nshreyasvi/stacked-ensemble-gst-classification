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

| Best model   | name                                                                                             | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
| **the best** | [Ensemble_Stacked](Ensemble_Stacked/README.md)                                                   | Ensemble       | logloss       |      0.0487711 |      4082.93 |
|              | [1_Baseline](1_Baseline/README.md)                                                               | Baseline       | logloss       |      0.312361  |        39    |
|              | [2_DecisionTree](2_DecisionTree/README.md)                                                       | Decision Tree  | logloss       |      0.0609345 |        97.66 |
|              | [3_DecisionTree](3_DecisionTree/README.md)                                                       | Decision Tree  | logloss       |      0.0590441 |        98.35 |
|              | [4_DecisionTree](4_DecisionTree/README.md)                                                       | Decision Tree  | logloss       |      0.0590441 |        98.38 |
|              | [5_Default_LightGBM](5_Default_LightGBM/README.md)                                               | LightGBM       | logloss       |      0.0491674 |       206.19 |
|              | [6_Default_Xgboost](6_Default_Xgboost/README.md)                                                 | Xgboost        | logloss       |      0.049337  |       208.63 |
|              | [7_Default_CatBoost](7_Default_CatBoost/README.md)                                               | CatBoost       | logloss       |      0.0494532 |       281.15 |
|              | [8_Default_NeuralNetwork](8_Default_NeuralNetwork/README.md)                                     | Neural Network | logloss       |      0.0601199 |       927.16 |
|              | [9_Default_RandomForest](9_Default_RandomForest/README.md)                                       | Random Forest  | logloss       |      0.0583586 |       249.84 |
|              | [10_Default_ExtraTrees](10_Default_ExtraTrees/README.md)                                         | Extra Trees    | logloss       |      0.126521  |       259.37 |
|              | [20_LightGBM](20_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0493681 |       193.59 |
|              | [11_Xgboost](11_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0492229 |       181.08 |
|              | [29_CatBoost](29_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0492586 |       459.24 |
|              | [38_RandomForest](38_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0594859 |       226.07 |
|              | [47_ExtraTrees](47_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.152036  |       321.63 |
|              | [56_NeuralNetwork](56_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0603064 |      1040.05 |
|              | [21_LightGBM](21_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0497553 |       130.7  |
|              | [12_Xgboost](12_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0492996 |       165.15 |
|              | [30_CatBoost](30_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0493382 |       257.95 |
|              | [39_RandomForest](39_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0545888 |       383.41 |
|              | [48_ExtraTrees](48_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.107614  |       250.14 |
|              | [57_NeuralNetwork](57_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0553636 |      2480.42 |
|              | [22_LightGBM](22_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0491429 |       203.05 |
|              | [13_Xgboost](13_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0494136 |       186.43 |
|              | [31_CatBoost](31_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.049365  |       263.11 |
|              | [40_RandomForest](40_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0603571 |       335.37 |
|              | [49_ExtraTrees](49_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.132285  |       213.9  |
|              | [58_NeuralNetwork](58_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0660043 |      2010.21 |
|              | [23_LightGBM](23_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0491101 |       146.96 |
|              | [14_Xgboost](14_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0497537 |       188.94 |
|              | [32_CatBoost](32_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0495029 |       194.44 |
|              | [41_RandomForest](41_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0557619 |       279.54 |
|              | [50_ExtraTrees](50_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.114447  |       247.1  |
|              | [59_NeuralNetwork](59_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0604965 |      1160.27 |
|              | [24_LightGBM](24_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.04965   |       129.55 |
|              | [15_Xgboost](15_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0495772 |       234.87 |
|              | [33_CatBoost](33_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0494204 |       347.05 |
|              | [42_RandomForest](42_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0603542 |       224.16 |
|              | [51_ExtraTrees](51_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.148196  |       226.72 |
|              | [60_NeuralNetwork](60_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0552701 |      1885.6  |
|              | [25_LightGBM](25_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0491614 |       185.12 |
|              | [16_Xgboost](16_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0497153 |       282.27 |
|              | [34_CatBoost](34_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0497611 |       403.03 |
|              | [43_RandomForest](43_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0547039 |       399.61 |
|              | [52_ExtraTrees](52_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.0789727 |       239.15 |
|              | [61_NeuralNetwork](61_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0553963 |      1501.23 |
|              | [26_LightGBM](26_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0491129 |       147.61 |
|              | [17_Xgboost](17_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.049253  |       231.91 |
|              | [35_CatBoost](35_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0492967 |       599.42 |
|              | [44_RandomForest](44_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0569874 |       281.83 |
|              | [53_ExtraTrees](53_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.0961841 |       229.18 |
|              | [62_NeuralNetwork](62_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0558558 |      1086.91 |
|              | [27_LightGBM](27_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0494392 |       136.65 |
|              | [18_Xgboost](18_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0494464 |       193.83 |
|              | [36_CatBoost](36_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0493499 |       324.47 |
|              | [45_RandomForest](45_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0587882 |       220    |
|              | [54_ExtraTrees](54_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.147102  |       317.78 |
|              | [63_NeuralNetwork](63_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0690673 |      1762.01 |
|              | [28_LightGBM](28_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0493859 |       185.49 |
|              | [19_Xgboost](19_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0491711 |       268.16 |
|              | [37_CatBoost](37_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.049334  |       797.6  |
|              | [46_RandomForest](46_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0572454 |       239.8  |
|              | [55_ExtraTrees](55_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.141972  |       220.96 |
|              | [64_NeuralNetwork](64_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.064335  |      1030.76 |
|              | [23_LightGBM_GoldenFeatures](23_LightGBM_GoldenFeatures/README.md)                               | LightGBM       | logloss       |      0.0491834 |       331    |
|              | [26_LightGBM_GoldenFeatures](26_LightGBM_GoldenFeatures/README.md)                               | LightGBM       | logloss       |      0.0491301 |       185.85 |
|              | [22_LightGBM_GoldenFeatures](22_LightGBM_GoldenFeatures/README.md)                               | LightGBM       | logloss       |      0.0491742 |       162.26 |
|              | [23_LightGBM_KMeansFeatures](23_LightGBM_KMeansFeatures/README.md)                               | LightGBM       | logloss       |      0.0493071 |       244.26 |
|              | [26_LightGBM_KMeansFeatures](26_LightGBM_KMeansFeatures/README.md)                               | LightGBM       | logloss       |      0.0492521 |       186.86 |
|              | [22_LightGBM_KMeansFeatures](22_LightGBM_KMeansFeatures/README.md)                               | LightGBM       | logloss       |      0.0492239 |       240.23 |
|              | [23_LightGBM_RandomFeature](23_LightGBM_RandomFeature/README.md)                                 | LightGBM       | logloss       |      0.0492587 |       241.98 |
|              | [23_LightGBM_SelectedFeatures](23_LightGBM_SelectedFeatures/README.md)                           | LightGBM       | logloss       |      0.0491752 |       154.93 |
|              | [19_Xgboost_SelectedFeatures](19_Xgboost_SelectedFeatures/README.md)                             | Xgboost        | logloss       |      0.0491888 |       255.05 |
|              | [29_CatBoost_SelectedFeatures](29_CatBoost_SelectedFeatures/README.md)                           | CatBoost       | logloss       |      0.0492449 |       473.46 |
|              | [39_RandomForest_SelectedFeatures](39_RandomForest_SelectedFeatures/README.md)                   | Random Forest  | logloss       |      0.054514  |       308.54 |
|              | [60_NeuralNetwork_SelectedFeatures](60_NeuralNetwork_SelectedFeatures/README.md)                 | Neural Network | logloss       |      0.0552919 |      1583.38 |
|              | [52_ExtraTrees_SelectedFeatures](52_ExtraTrees_SelectedFeatures/README.md)                       | Extra Trees    | logloss       |      0.0594756 |       228.08 |
|              | [65_LightGBM](65_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0492367 |       141.85 |
|              | [66_LightGBM](66_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.04921   |       149.65 |
|              | [67_LightGBM_GoldenFeatures](67_LightGBM_GoldenFeatures/README.md)                               | LightGBM       | logloss       |      0.0492746 |       148.12 |
|              | [68_Xgboost](68_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0492456 |       340.04 |
|              | [69_Xgboost](69_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0491114 |       250.2  |
|              | [70_Xgboost_SelectedFeatures](70_Xgboost_SelectedFeatures/README.md)                             | Xgboost        | logloss       |      0.049288  |       299.07 |
|              | [71_Xgboost_SelectedFeatures](71_Xgboost_SelectedFeatures/README.md)                             | Xgboost        | logloss       |      0.0491591 |       241.91 |
|              | [72_Xgboost](72_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.04926   |       233.77 |
|              | [73_Xgboost](73_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0492431 |       187.73 |
|              | [74_CatBoost_SelectedFeatures](74_CatBoost_SelectedFeatures/README.md)                           | CatBoost       | logloss       |      0.0492631 |       509.94 |
|              | [75_CatBoost_SelectedFeatures](75_CatBoost_SelectedFeatures/README.md)                           | CatBoost       | logloss       |      0.0492082 |       427.95 |
|              | [76_CatBoost](76_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.049313  |       499.31 |
|              | [77_CatBoost](77_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0492504 |       451.78 |
|              | [78_CatBoost](78_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.0493563 |       655.17 |
|              | [79_CatBoost](79_CatBoost/README.md)                                                             | CatBoost       | logloss       |      0.049248  |       583.7  |
|              | [80_RandomForest_SelectedFeatures](80_RandomForest_SelectedFeatures/README.md)                   | Random Forest  | logloss       |      0.0546304 |       348.87 |
|              | [81_RandomForest_SelectedFeatures](81_RandomForest_SelectedFeatures/README.md)                   | Random Forest  | logloss       |      0.0545376 |       326.5  |
|              | [82_RandomForest](82_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0546737 |       379.87 |
|              | [83_RandomForest](83_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0545493 |       371.04 |
|              | [84_RandomForest](84_RandomForest/README.md)                                                     | Random Forest  | logloss       |      0.0545742 |       384.98 |
|              | [85_NeuralNetwork](85_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0555424 |      1989.34 |
|              | [86_NeuralNetwork](86_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0553746 |      3364.09 |
|              | [87_NeuralNetwork_SelectedFeatures](87_NeuralNetwork_SelectedFeatures/README.md)                 | Neural Network | logloss       |      0.0557844 |      1313.94 |
|              | [88_NeuralNetwork_SelectedFeatures](88_NeuralNetwork_SelectedFeatures/README.md)                 | Neural Network | logloss       |      0.055366  |      2618.9  |
|              | [89_NeuralNetwork](89_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0553591 |      2288.01 |
|              | [90_NeuralNetwork](90_NeuralNetwork/README.md)                                                   | Neural Network | logloss       |      0.0553378 |      2549.14 |
|              | [91_ExtraTrees_SelectedFeatures](91_ExtraTrees_SelectedFeatures/README.md)                       | Extra Trees    | logloss       |      0.0614885 |       227.05 |
|              | [92_DecisionTree](92_DecisionTree/README.md)                                                     | Decision Tree  | logloss       |      0.0651356 |       111.61 |
|              | [93_ExtraTrees](93_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.0890991 |       263.25 |
|              | [94_ExtraTrees](94_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.11526   |       235.65 |
|              | [95_ExtraTrees](95_ExtraTrees/README.md)                                                         | Extra Trees    | logloss       |      0.103739  |       246.68 |
|              | [96_LightGBM](96_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0491101 |       159.22 |
|              | [97_Xgboost](97_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0491421 |       217.48 |
|              | [98_Xgboost](98_Xgboost/README.md)                                                               | Xgboost        | logloss       |      0.0491562 |       219.99 |
|              | [99_LightGBM](99_LightGBM/README.md)                                                             | LightGBM       | logloss       |      0.0491129 |       155.98 |
|              | [100_LightGBM](100_LightGBM/README.md)                                                           | LightGBM       | logloss       |      0.0491129 |       156.66 |
|              | [101_LightGBM_GoldenFeatures](101_LightGBM_GoldenFeatures/README.md)                             | LightGBM       | logloss       |      0.0491301 |       161.97 |
|              | [102_LightGBM_GoldenFeatures](102_LightGBM_GoldenFeatures/README.md)                             | LightGBM       | logloss       |      0.0491301 |       162.35 |
|              | [103_Xgboost_SelectedFeatures](103_Xgboost_SelectedFeatures/README.md)                           | Xgboost        | logloss       |      0.0491326 |       206.65 |
|              | [104_Xgboost_SelectedFeatures](104_Xgboost_SelectedFeatures/README.md)                           | Xgboost        | logloss       |      0.0492602 |       213.63 |
|              | [105_Xgboost](105_Xgboost/README.md)                                                             | Xgboost        | logloss       |      0.0491606 |       232.14 |
|              | [106_Xgboost](106_Xgboost/README.md)                                                             | Xgboost        | logloss       |      0.0492284 |       244.41 |
|              | [107_CatBoost_SelectedFeatures](107_CatBoost_SelectedFeatures/README.md)                         | CatBoost       | logloss       |      0.0492177 |       699.9  |
|              | [108_CatBoost_SelectedFeatures](108_CatBoost_SelectedFeatures/README.md)                         | CatBoost       | logloss       |      0.0492891 |       301.91 |
|              | [109_CatBoost_SelectedFeatures](109_CatBoost_SelectedFeatures/README.md)                         | CatBoost       | logloss       |      0.0492632 |       718.99 |
|              | [110_CatBoost_SelectedFeatures](110_CatBoost_SelectedFeatures/README.md)                         | CatBoost       | logloss       |      0.0493181 |       300.56 |
|              | [111_CatBoost](111_CatBoost/README.md)                                                           | CatBoost       | logloss       |      0.0492547 |       404.85 |
|              | [112_RandomForest_SelectedFeatures](112_RandomForest_SelectedFeatures/README.md)                 | Random Forest  | logloss       |      0.0545758 |       252.45 |
|              | [113_RandomForest_SelectedFeatures](113_RandomForest_SelectedFeatures/README.md)                 | Random Forest  | logloss       |      0.0544598 |       252.99 |
|              | [114_RandomForest](114_RandomForest/README.md)                                                   | Random Forest  | logloss       |      0.0545016 |       329.79 |
|              | [115_ExtraTrees_SelectedFeatures](115_ExtraTrees_SelectedFeatures/README.md)                     | Extra Trees    | logloss       |      0.0596076 |       234.72 |
|              | [116_ExtraTrees_SelectedFeatures](116_ExtraTrees_SelectedFeatures/README.md)                     | Extra Trees    | logloss       |      0.0612883 |       232.11 |
|              | [117_ExtraTrees](117_ExtraTrees/README.md)                                                       | Extra Trees    | logloss       |      0.0706535 |       251.07 |
|              | [96_LightGBM_BoostOnErrors](96_LightGBM_BoostOnErrors/README.md)                                 | LightGBM       | logloss       |      0.0491283 |       161.19 |
|              | [Ensemble](Ensemble/README.md)                                                                   | Ensemble       | logloss       |      0.0488402 |      1973.08 |
|              | [96_LightGBM_Stacked](96_LightGBM_Stacked/README.md)                                             | LightGBM       | logloss       |      0.0491743 |       181.65 |
|              | [69_Xgboost_Stacked](69_Xgboost_Stacked/README.md)                                               | Xgboost        | logloss       |      0.049114  |       217.14 |
|              | [75_CatBoost_SelectedFeatures_Stacked](75_CatBoost_SelectedFeatures_Stacked/README.md)           | CatBoost       | logloss       |      0.0489716 |       249.5  |
|              | [113_RandomForest_SelectedFeatures_Stacked](113_RandomForest_SelectedFeatures_Stacked/README.md) | Random Forest  | logloss       |      0.0488156 |       841.61 |
|              | [60_NeuralNetwork_Stacked](60_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.0500318 |      1719.68 |
|              | [52_ExtraTrees_SelectedFeatures_Stacked](52_ExtraTrees_SelectedFeatures_Stacked/README.md)       | Extra Trees    | logloss       |      0.0488204 |       686.23 |
|              | [23_LightGBM_Stacked](23_LightGBM_Stacked/README.md)                                             | LightGBM       | logloss       |      0.0491743 |       195.3  |
|              | [103_Xgboost_SelectedFeatures_Stacked](103_Xgboost_SelectedFeatures_Stacked/README.md)           | Xgboost        | logloss       |      0.0491199 |       222.75 |
|              | [107_CatBoost_SelectedFeatures_Stacked](107_CatBoost_SelectedFeatures_Stacked/README.md)         | CatBoost       | logloss       |      0.0489441 |       342.07 |
|              | [114_RandomForest_Stacked](114_RandomForest_Stacked/README.md)                                   | Random Forest  | logloss       |      0.0488296 |       774.53 |
|              | [60_NeuralNetwork_SelectedFeatures_Stacked](60_NeuralNetwork_SelectedFeatures_Stacked/README.md) | Neural Network | logloss       |      0.0499325 |      1832.94 |
|              | [115_ExtraTrees_SelectedFeatures_Stacked](115_ExtraTrees_SelectedFeatures_Stacked/README.md)     | Extra Trees    | logloss       |      0.0488098 |       678.25 |
|              | [100_LightGBM_Stacked](100_LightGBM_Stacked/README.md)                                           | LightGBM       | logloss       |      0.0491362 |       180.21 |
|              | [97_Xgboost_Stacked](97_Xgboost_Stacked/README.md)                                               | Xgboost        | logloss       |      0.0491515 |       212.56 |
|              | [29_CatBoost_SelectedFeatures_Stacked](29_CatBoost_SelectedFeatures_Stacked/README.md)           | CatBoost       | logloss       |      0.0489571 |       244.51 |
|              | [39_RandomForest_SelectedFeatures_Stacked](39_RandomForest_SelectedFeatures_Stacked/README.md)   | Random Forest  | logloss       |      0.0488591 |       732.91 |
|              | [90_NeuralNetwork_Stacked](90_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.0499736 |      2535.27 |
|              | [116_ExtraTrees_SelectedFeatures_Stacked](116_ExtraTrees_SelectedFeatures_Stacked/README.md)     | Extra Trees    | logloss       |      0.0488176 |       746.73 |
|              | [99_LightGBM_Stacked](99_LightGBM_Stacked/README.md)                                             | LightGBM       | logloss       |      0.0491362 |       178.62 |
|              | [98_Xgboost_Stacked](98_Xgboost_Stacked/README.md)                                               | Xgboost        | logloss       |      0.0491187 |       217.99 |
|              | [79_CatBoost_Stacked](79_CatBoost_Stacked/README.md)                                             | CatBoost       | logloss       |      0.0489624 |       286.35 |
|              | [81_RandomForest_SelectedFeatures_Stacked](81_RandomForest_SelectedFeatures_Stacked/README.md)   | Random Forest  | logloss       |      0.0488645 |       900.17 |
|              | [89_NeuralNetwork_Stacked](89_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.050004  |      1923.46 |
|              | [91_ExtraTrees_SelectedFeatures_Stacked](91_ExtraTrees_SelectedFeatures_Stacked/README.md)       | Extra Trees    | logloss       |      0.0488152 |       681.49 |
|              | [26_LightGBM_Stacked](26_LightGBM_Stacked/README.md)                                             | LightGBM       | logloss       |      0.0491362 |       179.01 |
|              | [71_Xgboost_SelectedFeatures_Stacked](71_Xgboost_SelectedFeatures_Stacked/README.md)             | Xgboost        | logloss       |      0.0491214 |       220.6  |
|              | [77_CatBoost_Stacked](77_CatBoost_Stacked/README.md)                                             | CatBoost       | logloss       |      0.0489713 |       262.22 |
|              | [83_RandomForest_Stacked](83_RandomForest_Stacked/README.md)                                     | Random Forest  | logloss       |      0.048857  |      1066.84 |
|              | [57_NeuralNetwork_Stacked](57_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.0499082 |      1898.02 |
|              | [117_ExtraTrees_Stacked](117_ExtraTrees_Stacked/README.md)                                       | Extra Trees    | logloss       |      0.0488144 |       546.26 |
|              | [102_LightGBM_GoldenFeatures_Stacked](102_LightGBM_GoldenFeatures_Stacked/README.md)             | LightGBM       | logloss       |      0.0491697 |       186.56 |
|              | [105_Xgboost_Stacked](105_Xgboost_Stacked/README.md)                                             | Xgboost        | logloss       |      0.049077  |       207.64 |
|              | [111_CatBoost_Stacked](111_CatBoost_Stacked/README.md)                                           | CatBoost       | logloss       |      0.0489798 |       235.39 |
|              | [84_RandomForest_Stacked](84_RandomForest_Stacked/README.md)                                     | Random Forest  | logloss       |      0.0488622 |       774.28 |
|              | [88_NeuralNetwork_SelectedFeatures_Stacked](88_NeuralNetwork_SelectedFeatures_Stacked/README.md) | Neural Network | logloss       |      0.0500559 |      2541.47 |
|              | [52_ExtraTrees_Stacked](52_ExtraTrees_Stacked/README.md)                                         | Extra Trees    | logloss       |      0.048809  |       561.92 |
|              | [26_LightGBM_GoldenFeatures_Stacked](26_LightGBM_GoldenFeatures_Stacked/README.md)               | LightGBM       | logloss       |      0.0491697 |       194.01 |
|              | [19_Xgboost_Stacked](19_Xgboost_Stacked/README.md)                                               | Xgboost        | logloss       |      0.0490235 |       208.74 |
|              | [29_CatBoost_Stacked](29_CatBoost_Stacked/README.md)                                             | CatBoost       | logloss       |      0.0490018 |       241.49 |
|              | [112_RandomForest_SelectedFeatures_Stacked](112_RandomForest_SelectedFeatures_Stacked/README.md) | Random Forest  | logloss       |      0.0488292 |       645.86 |
|              | [86_NeuralNetwork_Stacked](86_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.049863  |      2645.39 |
|              | [93_ExtraTrees_Stacked](93_ExtraTrees_Stacked/README.md)                                         | Extra Trees    | logloss       |      0.0488102 |       620.5  |
|              | [101_LightGBM_GoldenFeatures_Stacked](101_LightGBM_GoldenFeatures_Stacked/README.md)             | LightGBM       | logloss       |      0.0491697 |       199.51 |
|              | [19_Xgboost_SelectedFeatures_Stacked](19_Xgboost_SelectedFeatures_Stacked/README.md)             | Xgboost        | logloss       |      0.0490382 |       229.54 |
|              | [74_CatBoost_SelectedFeatures_Stacked](74_CatBoost_SelectedFeatures_Stacked/README.md)           | CatBoost       | logloss       |      0.0489488 |       227.48 |
|              | [39_RandomForest_Stacked](39_RandomForest_Stacked/README.md)                                     | Random Forest  | logloss       |      0.0488556 |       829.15 |
|              | [61_NeuralNetwork_Stacked](61_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.0502849 |      2284.87 |
|              | [53_ExtraTrees_Stacked](53_ExtraTrees_Stacked/README.md)                                         | Extra Trees    | logloss       |      0.0488633 |       534.96 |
|              | [22_LightGBM_Stacked](22_LightGBM_Stacked/README.md)                                             | LightGBM       | logloss       |      0.0490944 |       191.96 |
|              | [11_Xgboost_Stacked](11_Xgboost_Stacked/README.md)                                               | Xgboost        | logloss       |      0.0491853 |       194.75 |
|              | [109_CatBoost_SelectedFeatures_Stacked](109_CatBoost_SelectedFeatures_Stacked/README.md)         | CatBoost       | logloss       |      0.0489601 |       331.55 |
|              | [80_RandomForest_SelectedFeatures_Stacked](80_RandomForest_SelectedFeatures_Stacked/README.md)   | Random Forest  | logloss       |      0.0488611 |       880.87 |
|              | [85_NeuralNetwork_Stacked](85_NeuralNetwork_Stacked/README.md)                                   | Neural Network | logloss       |      0.0496906 |      2303.95 |
|              | [95_ExtraTrees_Stacked](95_ExtraTrees_Stacked/README.md)                                         | Extra Trees    | logloss       |      0.0488694 |       562.88 |
|              | [106_Xgboost_Stacked](106_Xgboost_Stacked/README.md)                                             | Xgboost        | logloss       |      0.0490517 |       226.17 |
|              | [108_CatBoost_SelectedFeatures_Stacked](108_CatBoost_SelectedFeatures_Stacked/README.md)         | CatBoost       | logloss       |      0.0490226 |       217.38 |
|              | [82_RandomForest_Stacked](82_RandomForest_Stacked/README.md)                                     | Random Forest  | logloss       |      0.0488677 |      1005.03 |
|              | [87_NeuralNetwork_SelectedFeatures_Stacked](87_NeuralNetwork_SelectedFeatures_Stacked/README.md) | Neural Network | logloss       |      0.0499196 |      2196.45 |
|              | [48_ExtraTrees_Stacked](48_ExtraTrees_Stacked/README.md)                                         | Extra Trees    | logloss       |      0.0488159 |       572.85 |


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