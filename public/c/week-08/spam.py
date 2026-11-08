# AI in 15 lines: a spam filter that LEARNS from examples (scikit-learn, installed in Colab)
# pip install scikit-learn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = ["win a free prize now", "free money click here", "claim your free iphone",
            "lab 7 is due on friday", "see you at the lecture", "the midterm covers weeks 1 to 7"]
labels = ["spam", "spam", "spam", "ham", "ham", "ham"]

vectorizer = CountVectorizer()                      # turns each message into word counts (a dict, really)
X = vectorizer.fit_transform(messages)              # one row per message, one column per word

model = MultinomialNB()                             # a classic learning algorithm
model.fit(X, labels)                                # the "learning": count which words appear in spam

for text in ["free prize for you", "the lab is due friday", "free lecture notes"]:
    guess = model.predict(vectorizer.transform([text]))[0]
    print(f"{text!r:30} → {guess}")
