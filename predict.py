import joblib
from preprocessing import preprocess_text

print("Loading AI model...")

model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

print("Model loaded successfully!\n")

while True:
    print("=" * 60)
    print("AI Powered Fake News Detector")
    print("=" * 60)

    news = input("\nEnter a headline or article:\n\n")

    cleaned = preprocess_text(news)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = max(probability) * 100

    print("\nPrediction")

    if prediction == 1:
        print("✅ REAL NEWS")
    else:
        print("❌ FAKE NEWS")

    print(f"Confidence: {confidence:.2f}%")

    again = input("\nPredict another article? (y/n): ").lower()

    if again != "y":
        break

print("\nGoodbye!")