# Importing the libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from text_cleaner import TextCleaner
import numpy as np
import pandas as pd
import pickle


def main():
    # Importing the dataset
    dataset = pd.read_csv("../Dataset/dataset.csv")

    # Cleaning the texts
    corpus = []
    for i in range(0, 1500):
        corpus.append(TextCleaner.clear_text(dataset['text'][i]))

    # Creating the Bag of Words model
    cv = CountVectorizer(max_features=1500)
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    # Encode dependant variable
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    # Training the Naive Bayes model on the Training set
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

    # Making the Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(accuracy_score(y_test, y_pred))

    # Saving Model and CountVectorizer

    with open("./trained_model/model.pkl", "wb") as f:
        pickle.dump((classifier, cv), f)


if __name__ == '__main__':
    main()
