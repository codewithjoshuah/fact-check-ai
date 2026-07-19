class ReportGenerator:

    def generate(self, claim, prediction, confidence, evidence):

        print("\n" + "=" * 70)
        print("AI FACT CHECK REPORT")
        print("=" * 70)

        print(f"\nClaim:\n{claim}")

        print("\nML Classifier")
        print("-" * 70)

        print(f"Prediction : {prediction}")
        print(f"Confidence : {confidence:.2f}%")

        print("\nEvidence")
        print("-" * 70)

        for article in evidence:

            print(f"Source      : {article['title']}")
            print(f"Credibility : {article['credibility']}")
            print(f"Similarity  : {article['similarity']}")
            print(f"URL         : {article['url']}")
            print()

        print("=" * 70)