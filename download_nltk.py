import nltk

resources = [
    "stopwords",
    "punkt",
    "wordnet",
    "omw-1.4"
]

for resource in resources:
    print(f"Downloading {resource}...")
    nltk.download(resource)

print("\n✅ All NLTK resources downloaded successfully!")