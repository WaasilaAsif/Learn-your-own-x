# Solar Panel Fault Detection Model

## 1. What does this model do?

This notebook uses machine learning to identify the condition of a solar panel from its electrical and environmental measurements.

It learns from the labelled training dataset and predicts the label for each row in the test dataset.

The main measurements used are:

- `dc_voltage`: The DC voltage produced by the panel.
- `dc_current`: The DC current produced by the panel.
- `irradiance`: The amount of sunlight reaching the panel.
- `panel_temp`: The temperature of the solar panel.

The training data also contains a `label` column. This tells the model which condition each training example belongs to.

## 2. Loading and preparing the data

The notebook loads `train.csv` and `test.csv`.

Some measurements may be missing. To handle this, missing values in the four measurement columns are replaced with the median value from the training data.

The labels are then converted into numbers so that the machine learning models can use them.

## 3. Estimating normal panel behaviour

A solar panel's voltage and current naturally change with sunlight and temperature.

Because of this, the model first learns what normal panel behaviour should look like.

It uses only training examples labelled `normal` with irradiance above 100 to build two regression models:

1. One estimates the expected DC current using irradiance and panel temperature.
2. The other estimates the expected DC voltage using panel temperature and the logarithm of irradiance.

These models use polynomial features and Ridge Regression. This allows them to learn simple nonlinear relationships while reducing overfitting.

The estimated values are then compared with the panel's actual voltage and current.

## 4. Creating useful features

The notebook creates additional measurements from the original data.

These include:

- The logarithm of irradiance.
- Current relative to irradiance.
- Power relative to irradiance.
- Voltage divided by current.
- The difference between actual and expected current.
- The difference between actual and expected voltage.
- Actual current and voltage compared with their expected values.
- Actual power compared with expected power.
- An estimate related to series resistance.

These features help the model identify unusual panel behaviour that may indicate a fault.

For example, if the actual current is much lower than the expected current under the same sunlight and temperature conditions, this may help distinguish a faulty panel from a normal one.

## 5. Machine learning models

The notebook uses two classification algorithms:

**Random Forest**

This model combines many decision trees. Each tree makes a prediction, and their combined predictions help determine the final result.

**Histogram Gradient Boosting**

This model builds decision trees sequentially. Each new tree attempts to improve the predictions made by the previous trees.

Both models produce probabilities for the possible classes.

The notebook gives more importance to less common classes during training. This helps address class imbalance, where some panel conditions appear much less frequently than others.

Finally, the probabilities from both models are averaged. This is called an ensemble.

## 6. Model validation

Before making predictions for the test dataset, the notebook checks how well the model performs on the training data.

It uses Group K Fold validation with up to five groups.

The groups are based on the `day` column. This means that data from the same day is kept together instead of being randomly divided between training and validation.

This gives a more realistic evaluation when measurements from the same day may be related.

The notebook reports:

- **Macro F1 score:** Measures performance across all classes, giving each class equal importance.
- **Precision:** How often predictions for a class are correct.
- **Recall:** How many actual examples of a class the model successfully identifies.
- **F1 score:** A balance between precision and recall.

## 7. Generating the Kaggle submission

After validation, the notebook trains the models using the full training dataset.

It then predicts the labels for the test dataset.

The final predictions are saved in a file called `submission.csv`.

The file contains two columns:

- `id`: The identifier of each test example.
- `label`: The predicted panel condition.

This file can then be submitted to the Kaggle competition.

## 8. Overall workflow

1. Load the training and test datasets.
2. Fill missing measurement values.
3. Learn expected normal voltage and current.
4. Create additional features from the measurements.
5. Train Random Forest and Histogram Gradient Boosting classifiers.
6. Validate the models using groups based on day.
7. Average the predictions from both classifiers.
8. Predict labels for the test dataset.
9. Save the predictions as `submission.csv`.

## Conclusion

The main idea behind this model is to compare a solar panel's actual electrical behaviour with the behaviour expected under its current sunlight and temperature conditions.

Instead of relying only on raw voltage and current measurements, the model also uses differences and ratios between actual and expected values.

These additional features, combined with two machine learning classifiers, help the model distinguish between the different conditions in the dataset.
