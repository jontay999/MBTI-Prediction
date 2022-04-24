# MBTI-Prediction model for Personality profiling

The Myer-Briggs Type Indicator is a comprehensive indicator of personality types and is used commonly in various settings, from Occupational choices to targetted marketing and personality classification. Given that the test takes approximately 20-30 minutes, this is overhead time that can be reduced and classification made more efficient. Hence, we developed a Prediction model for MBTI personality types based on **text input** by the user. We train our model on user comments extracted from Reddit.

## Directory

1. [Exploratory Analysis](explore.ipynb)
2. [Data Cleaning](data_cleaning.ipynb)
3. [Generate word embeddings](Reddit%20Embeddings.ipynb)
4. [Classifier Comparisons](Classifier%20Comparisons.ipynb)
5. [Specific Model](Reddit%20LM.ipynb)

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

We can talk about our accuracy here and do some analysis. throw in wordcloud of more frequent words for each MBTI

## Results and Conclusion

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

## Contributors

- @cadyli - Data Visualization
- @dhruvalk - Data Cleaning and preprocessing
- @jontay999 - Model fine-tuning

## References

1. [Bottom-Up and Top-Down: Predicting Personality with Psycholinguistic and Language Model Features](https://www.semanticscholar.org/paper/Bottom-Up-and-Top-Down%3A-Predicting-Personality-with-Mehta-Fatehi/a872c10eaba767f82ca0a2f474c5c8bcd05f0d44#citing-papers)
2. [Myer-Briggs Type Assesment](https://www.capt.org/take-mbti-assessment/mbti.htm#:~:text=The%20real%20Myers%2DBriggs%20Type,will%20be%20emailed%20to%20you.)
3. any other research links we have

_This repository is submitted to Nanyang Technological University as part of a graded assignment for the course CZ1115 (Introduction to Data Science & Artificial Intelligence)_<br><br>
_Copyright &copy; 2022_
