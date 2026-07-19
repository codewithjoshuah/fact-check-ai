from transformers import pipeline


class NLIPredictor:

    def __init__(self):

        print("Loading NLI model...")

        self.classifier = pipeline(
            "text-classification",
            model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"
        )

        print("NLI model loaded.\n")

    def predict(self, claim, evidence):

        text = f"{claim} [SEP] {evidence}"

        result = self.classifier(text)[0]

        return {
            "label": result["label"],
            "score": round(result["score"], 3)
        }