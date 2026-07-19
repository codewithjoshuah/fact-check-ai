from sentence_transformers import SentenceTransformer, util


class Deduplicator:

    def __init__(self):
        print("Loading deduplication model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Deduplication model ready.\n")

    def remove_duplicates(self, articles, threshold=0.90):

        unique_articles = []

        for article in articles:

            paragraph = article.get("best_paragraph", "")

            if not paragraph:
                continue

            paragraph_embedding = self.model.encode(
                paragraph,
                convert_to_tensor=True
            )

            duplicate = False

            for existing in unique_articles:

                existing_embedding = self.model.encode(
                    existing["best_paragraph"],
                    convert_to_tensor=True
                )

                similarity = util.cos_sim(
                    paragraph_embedding,
                    existing_embedding
                ).item()

                if similarity >= threshold:

                    duplicate = True

                    if article["credibility"] > existing["credibility"]:
                        unique_articles.remove(existing)
                        unique_articles.append(article)

                    break

            if not duplicate:
                unique_articles.append(article)

        return unique_articles