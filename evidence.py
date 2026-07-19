from sentence_transformers import SentenceTransformer, util
from sentence_transformers import SentenceTransformer, util
from nli import NLIPredictor

class EvidenceAnalyzer:

    def __init__(self):
        print("Loading semantic model...")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.nli = NLIPredictor()

        print("Evidence analyzer ready.\n")

    def find_best_evidence(self, claim, articles):

        claim_embedding = self.model.encode(
            claim,
            convert_to_tensor=True
        )

        best_matches = []

        for article in articles:

            content = article.get("content", "")

            if not content:
                continue

            paragraphs = content.split("\n")

            best_paragraph = ""
            best_score = 0

            for paragraph in paragraphs:

                if len(paragraph) < 50:
                    continue

                paragraph_embedding = self.model.encode(
                    paragraph,
                    convert_to_tensor=True
                )

                similarity = util.cos_sim(
                    claim_embedding,
                    paragraph_embedding
                ).item()

                if similarity > best_score:

                    best_score = similarity
                    best_paragraph = paragraph
            nli_result = self.nli.predict(
                claim,
                best_paragraph
            )

            article["similarity"] = round(best_score, 3)
            article["best_paragraph"] = best_paragraph

            article["nli"] = nli_result["label"]
            article["nli_score"] = nli_result["score"]

            best_matches.append(article)

        best_matches.sort(
            key=lambda x: x["similarity"],
            reverse=True
        )

        return best_matches