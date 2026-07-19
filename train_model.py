from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import joblib
from preprocessing import preprocess_text

print("Loading datasets...")

true_df = pd.read_csv("dataset/True.csv")
fake_df = pd.read_csv("dataset/Fake.csv")

true_df["label"] = 1
fake_df["label"] = 0

data = pd.concat([true_df, fake_df], ignore_index=True)

data = data.sample(frac=1, random_state=42).reset_index(drop=True)

data["content"] = data["title"] + " " + data["text"]

print("Cleaning text...")

data["content"] = data["content"].apply(preprocess_text)

print("\nDataset Shape:", data.shape)

print("\nLabel Distribution:")
print(data["label"].value_counts())

print("\nFirst Cleaned Article:\n")
print(data["content"].iloc[0][:1000])

print("\nConverting text to TF-IDF vectors...")

vectorizer = TfidfVectorizer(
    max_features=5000
)

X = vectorizer.fit_transform(data["content"])
y = data["label"]

print("Shape of TF-IDF Matrix:", X.shape)

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])

print("\nTraining Logistic Regression Model...")

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("Training Complete!")

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))
print("\nSaving model...")

joblib.dump(model, "model/fake_news_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

print("✅ Model saved successfully!")