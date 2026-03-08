import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
"Null pointer exception in code",
"Syntax error in python program",
"Application crashed due to bug",
"Code works perfectly",
"Program executed successfully",
"No errors found in code",
"Index out of range error",
"Segmentation fault detected",
"Program compiled successfully",
"Execution completed without errors"
]

labels = [1,1,1,0,0,0,1,1,0,0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

pickle.dump(model, open("bug_model.pkl","wb"))
pickle.dump(vectorizer, open("bug_vectorizer.pkl","wb"))

print("Bug detection model saved!")