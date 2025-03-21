import pandas as pd
import matplotlib.pyplot as plt
from src.utils import get_count_vectorizer_fake_news_dataset,get_tfidf_fake_newes_dataset

# Import the necessary modules
from sklearn import  metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score


count_train,count_test , count_vectorizer ,count_y_train, count_y_test = get_count_vectorizer_fake_news_dataset()


# Instantiate a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(count_train,count_y_train)
# Create the predicted tags: pred
pred = nb_classifier.predict(count_test)

# Calculate the accuracy score: score
score = accuracy_score(count_y_test,pred)
print(score)

# Calculate the confusion matrix: cm
cm = confusion_matrix(count_y_test,pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,  display_labels=['FAKE', 'REAL'])
disp.plot()
plt.show()
