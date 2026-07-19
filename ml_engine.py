import joblib
from preprocessing import preprocess_text


class MLEngine:
    def __init__(self):
        print("Loading machine learning model...")

        self.model = joblib.load("model/fake_news_model.pkl")
        self.vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

        print("Machine learning model loaded.\n")

    def predict(self, text):
        cleaned = preprocess_text(text)

        vector = self.vectorizer.transform([cleaned])

        prediction = self.model.predict(vector)[0]
        probabilities = self.model.predict_proba(vector)[0]

        class_probs = dict(zip(self.model.classes_, probabilities))

        confidence = class_probs[prediction] * 100

        label = "REAL" if prediction == 1 else "FAKE"

        return {
            "prediction": label,
            "confidence": round(confidence, 2),
            "probabilities": {
                "fake": round(class_probs.get(0, 0) * 100, 2),
                "real": round(class_probs.get(1, 0) * 100, 2)
            }
        }