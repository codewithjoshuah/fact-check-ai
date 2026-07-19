from tavily import TavilyClient
from credibility import CredibilityScorer
from config import TAVILY_API_KEY


class Retriever:

    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)
        self.scorer = CredibilityScorer()

    def search(self, claim):

        response = self.client.search(
            query=claim,
            search_depth="advanced",
            max_results=5,
            include_answer=True,
            include_raw_content=True
        )

        results = response["results"]

        for article in results:
            article["credibility"] = self.scorer.score(article["url"])

        results.sort(
            key=lambda x: x["credibility"],
            reverse=True
        )

        return results