class EvidenceRanker:

    def rank(self, articles):

        for article in articles:

            credibility = article["credibility"] / 100
            similarity = article["similarity"]
            nli = article["nli_score"]

            score = (
                credibility * 0.5 +
                similarity * 0.3 +
                nli * 0.2
            )

            article["overall_score"] = round(score, 3)

        articles.sort(
            key=lambda x: x["overall_score"],
            reverse=True
        )

        return articles