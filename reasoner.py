class Reasoner:

    def analyze(self, prediction, evidence):

        support = 0
        contradiction = 0

        for article in evidence:

            weight = (
                article["credibility"] *
                article["similarity"] *
                article["nli_score"]
            )

            label = article["nli"].lower()

            if "entail" in label or "support" in label:
                support += weight

            elif "contradiction" in label:
                contradiction += weight

        if contradiction > support:
            verdict = "FAKE"
            confidence = contradiction / (support + contradiction)

        elif support > contradiction:
            verdict = "REAL"
            confidence = support / (support + contradiction)

        else:
            verdict = prediction.upper()
            confidence = 0.50

        if verdict == "REAL":
            summary = (
                "The claim is supported by multiple trusted "
                "sources and no strong contradictory evidence "
                "was found."
            )

        elif verdict == "FAKE":
            summary = (
                "The claim is not supported by trusted "
                "sources and the available evidence "
                "contradicts it."
            )

        else:
            summary = (
                "The available evidence is insufficient to "
                "determine whether the claim is true or false."
            )

        return {
            "verdict": verdict,
            "confidence": round(confidence * 100, 2),
            "summary": summary
        }