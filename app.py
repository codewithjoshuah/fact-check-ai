from ml_engine import MLEngine
from claim_extractor import ClaimExtractor

engine = MLEngine()
extractor = ClaimExtractor()

while True:

    article = input("\nPaste article:\n\n")

    print("\nExtracting claims...\n")

    claims = extractor.extract(article)

    for i, claim in enumerate(claims, start=1):

        print(f"Claim {i}:")
        print(claim)

        result = engine.predict(claim)

        verdict = "REAL" if result["prediction"] == 1 else "FAKE"

        print(f"Prediction : {verdict}")
        print(f"Confidence: {result['confidence']}%")
        print("-" * 50)

    again = input("\nCheck another article? (y/n): ").lower()

    if again != "y":
        break