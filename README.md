# MBTI-Prediction model for Personality profiling

The Myer-Briggs Type Indicator is a comprehensive indicator of personality types and is used commonly in various settings, from Occupational choices to targetted marketing and personality classification. Given that the test takes approximately 20-30 minutes, this is overhead time that can be reduced and classification made more efficient. Hence, we developed a Prediction model for MBTI personality types based on **text input** by the user. We train our model on user comments extracted from Reddit.

## Directory

1. [Exploratory Analysis and Data Cleaning](data_cleaning.ipynb)
2. [Generate word embeddings](Reddit%20Embeddings.ipynb)
3. [Classifier Comparisons](Classifier%20Comparisons.ipynb)
4. [Specific Model](Reddit%20LM.ipynb)

Datasets used for training and testing are not included in this repository due to Github's file size limit.

## Models used

- Albert Tokenizer
- General Classifier Comparisons
  - K Nearest Neighbors
  - Linear SVM
  - Neural Net (MLP)
  - Random Forest
  - Radial Basis Function SVM (RBF SVM)
  - Naive Bayes (Quadratic Discriminant Analysis)
  - AdaBoost
- Specific Models (with a larger dataset)
  - Support Vector Machine (SVM)
  - Multi-Layer Perceptual (MLP)

## Findings and Analysis
From the results (shown below) we identify the two best models to use in prediction of each class as follows:<br><br>
- I vs E - RBF SVM, MLP
- N vs S - RBF SVM, MLP
- F vs T - RBF SVM, Naive Bayes
- P vs J - RBF SVM, Naive Bayes

## Results and Conclusion
RBF SVM produces consistent results in predicting all classes, performing best with the highest accuracy for all. We highly recommend using this model for MBTI classification. 

### Analysis of Extraversion (E) vs Introversion (I)

| Model               | Accuracy  | F1 Score  | Precision | Recall    |
| ------------------- | --------- | --------- | --------- | --------- |
| K Nearest Neighbors | 0.517     | 0.484     | 0.482     | 0.487     |
| Linear SVM          | 0.537     | 0.467     | 0.504     | 0.436     |
| Decision Tree       | 0.515     | 0.443     | 0.477     | 0.414     |
| Neural Net (MLP)    | 0.530     | **0.500** | 0.496     | **0.504** |
| Random Forest       | 0.542     | 0.483     | 0.509     | 0.460     |
| RBF SVM             | **0.558** | 0.100     | **0.968** | 0.053     |
| Naive Bayes         | 0.538     | 0.495     | 0.505     | 0.487     |
| AdaBoost            | 0.529     | 0.453     | 0.493     | 0.419     |

### Analysis of Intuition (N) vs Sensing (S)

| Model               | Accuracy  | F1 Score  | Precision | Recall  |
| ------------------- | --------- | --------- | --------- | ------- |
| K Nearest Neighbors | 0.511     | 0.538     | 0.530     | 0.547   |
| Linear SVM          | 0.541     | 0.591     | **0.552** | 0.636   |
| Decision Tree       | 0.513     | 0.552     | 0.530     | 0.576   |
| Neural Net (MLP)    | 0.547     | 0.567     | 0.566     | 0.569   |
| Random Forest       | 0.517     | 0.656     | 0.522     | 0.881   |
| RBF SVM             | **0.551** | **0.699** | 0.537     | **1.0** |
| Naive Bayes         | 0.520     | 0.547     | 0.539     | 0.555   |
| AdaBoost            | 0.534     | 0.588     | 0.545     | 0.638   |

### Analysis of Feeling (F) vs Thinking (T)

| Model               | Accuracy  | F1 Score  | Precision | Recall    |
| ------------------- | --------- | --------- | --------- | --------- |
| K Nearest Neighbors | 0.524     | 0.521     | 0.511     | 0.531     |
| Linear SVM          | 0.552     | 0.558     | 0.537     | 0.580     |
| Decision Tree       | 0.524     | 0.537     | 0.510     | 0.568     |
| Neural Net (MLP)    | 0.546     | 0.545     | 0.532     | 0.558     |
| Random Forest       | 0.540     | 0.544     | 0.525     | 0.564     |
| RBF SVM             | 0.505     | **0.662** | 0.496     | **0.995** |
| Naive Bayes         | **0.555** | 0.517     | **0.548** | 0.489     |
| AdaBoost            | 0.530     | 0.536     | 0.516     | 0.557     |

### Analysis of Perceiving (P) vs Judging (J)

| Model               | Accuracy  | F1 Score  | Precision | Recall    |
| ------------------- | --------- | --------- | --------- | --------- |
| K Nearest Neighbors | 0.556     | 0.357     | 0.392     | 0.327     |
| Linear SVM          | 0.621     | 0.150     | 0.482     | 0.089     |
| Decision Tree       | 0.617     | 0.063     | 0.395     | 0.034     |
| Neural Net (MLP)    | 0.565     | 0.408     | 0.418     | 0.398     |
| Random Forest       | 0.623     | 0.002     | 0.500     | 0.001     |
| RBF SVM             | **0.631** | 0.044     | **0.955** | 0.023     |
| Naive Bayes         | 0.493     | **0.444** | 0.378     | **0.537** |
| AdaBoost            | 0.596     | 0.204     | 0.395     | 0.137     |

## Future Considerations
1. Given limited computing power, all analysis done was on a dataset with 4 million rows, which was then filtered down to 12k rows after all data cleaning and preprocessing. Given more time and resources, it would be beneficial to train our recommended models on a larger dataset of 17 million rows, which would be filtered down to 130k rows after all preprocessing. This would provide a more accurate model trained on a larger dataset.
2. Hyper parameter tuning would allow a better model fit on the training set and we were unable to perform this due to limited time.
3. Train model on a variety of datasets, not limited to just reddit comments but also exploring more primary data sources such as first hand accounts of events and self-introductions rather than secondary data such as replies on comments.

## Contributors

- @cadyli - Data Visualization
- @dhruvalk - Data Cleaning and preprocessing
- @jontay999 - Model fine-tuning

## References

1. [Bottom-Up and Top-Down: Predicting Personality with Psycholinguistic and Language Model Features](https://www.semanticscholar.org/paper/Bottom-Up-and-Top-Down%3A-Predicting-Personality-with-Mehta-Fatehi/a872c10eaba767f82ca0a2f474c5c8bcd05f0d44#citing-papers)
2. [Myer-Briggs Type Assesment](https://www.capt.org/take-mbti-assessment/mbti.htm#:~:text=The%20real%20Myers%2DBriggs%20Type,will%20be%20emailed%20to%20you.)
3. [Balancing learning rate and batch size](https://arxiv.org/pdf/1711.00489.pdf)
4. [Effect of batch size on training dynamics](https://medium.com/mini-distill/effect-of-batch-size-on-training-dynamics-21c14f7a716e)
5. [Classification Framework for imbalanced data](https://towardsdatascience.com/classification-framework-for-imbalanced-data-9a7961354033)
6. [Pre-trained word embeddings](https://towardsdatascience.com/from-pre-trained-word-embeddings-to-pre-trained-language-models-focus-on-bert-343815627598)

_This repository is submitted to Nanyang Technological University as part of a graded assignment for the course CZ1115 (Introduction to Data Science & Artificial Intelligence)_<br><br>
_Copyright &copy; 2022_
