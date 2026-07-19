import re


class ClaimExtractor:
    def __init__(self):
        pass

    def extract(self, article):
        sentences = re.split(r"[.!?]+", article)

        claims = []

        for sentence in sentences:
            sentence = sentence.strip()

            if len(sentence) > 20:
                claims.append(sentence)

        return claims