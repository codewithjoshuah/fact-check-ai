from ml_engine import MLEngine
from retriever import Retriever
from evidence import EvidenceAnalyzer
from deduplicator import Deduplicator
from ranker import EvidenceRanker
from reasoner import Reasoner

claim = input("Enter a claim: ")

ml = MLEngine()
retriever = Retriever()
analyzer = EvidenceAnalyzer()
deduplicator = Deduplicator()
ranker = EvidenceRanker()
reasoner = Reasoner()

# 1. ML Prediction
ml_result = ml.predict(claim)

# 2. Retrieve Articles
articles = retriever.search(claim)

# 3. Extract Evidence
evidence = analyzer.find_best_evidence(claim, articles)

# 4. Remove Duplicates
unique_articles = deduplicator.remove_duplicates(evidence)

# 5. Rank Evidence
ranked_articles = ranker.rank(unique_articles)

# 6. Get Final Verdict  <-- THIS IS MISSING
result = reasoner.analyze(
    ml_result["prediction"],
    ranked_articles[:3]   # Use top 3 ranked articles
)

# 7. Print Result
print("\n" + "=" * 55)
print("           AI FACT CHECK RESULT")
print("=" * 55)

print(f"\nClaim:\n{claim}")
print(f"\nVerdict: {result['verdict']}")
print(f"Confidence: {result['confidence']}%")
print(f"\nSummary:\n{result['summary']}")