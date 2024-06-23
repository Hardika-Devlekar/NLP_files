import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
breastcancer = datasets.load_breast_cancer()

print("\nFeatures of breastcancer dataset : ", breastcancer.feature_names)
print("\nLabels of breastcancer dataset : ", breastcancer.target_names)
print("\nShape of breastcancer dataset : ", breastcancer.data.shape)
print("\n----------------------------------------------------------------------------------")

R = breastcancer.data
T = breastcancer.target

# Splitting the dataset into training set and testing set
Rtrain, Rtest, Ttrain, Ttest = train_test_split(R, T, test_size = 0.2, random_state = 0)

# 1. Using the Gaussian Naive Bayes Classifier
gauss = GaussianNB()

# Training the Gaussian Naive Bayes model using training set
gauss.fit(Rtrain,Ttrain)

# Making predictions using the test set
pred = gauss.predict(Rtest)

# Generating classification report of the Gaussian Naive Bayes Model
gcr = classification_report(Ttest,pred)
print("\nClassification Report gaussian : \n", gcr)

# Generating confusion matrix of the Gaussian Naive Bayes Model
gcm = confusion_matrix(Ttest, pred)
print("\nConfusion matrix gaussian : \n", gcm)

# Evaluating the naive bayes classifier on the basis of accuracy metric
accuracy = accuracy_score(Ttest, pred)
print("\nAccuracy : ", accuracy * 100)
