from urllib.parse import urlparse


class CredibilityScorer:

    def __init__(self):
        self.trusted = {
            "reuters.com": 100,
            "apnews.com": 99,
            "bbc.com": 98,
            "nasa.gov": 100,
            "who.int": 100,
            "cdc.gov": 100,
            "nature.com": 99,
            "science.org": 99,
        }

    def score(self, url):

        domain = urlparse(url).netloc.replace("www.", "")

        for trusted_domain, score in self.trusted.items():
            if domain == trusted_domain or domain.endswith("." + trusted_domain):
                return score

        return 20