# AI Fact Checker

I built this project to explore how machine learning and NLP can be used to verify online news and claims. Instead of relying only on text classification, it retrieves evidence from trusted sources, analyzes the relevance and credibility of that evidence, and generates a final verdict.

## Features

- Machine learning-based claim classification
- Online evidence retrieval using Tavily
- Source credibility scoring
- Semantic similarity search
- Natural Language Inference (NLI)
- Evidence ranking and deduplication
- Final verdict with confidence score

## Tech Stack

- Python
- Scikit-learn
- NLTK
- Sentence Transformers
- Hugging Face Transformers
- Tavily Search API

## Running the Project

```bash
pip install -r requirements.txt
python app.py
```

Create a `.env` file before running:

```text
TAVILY_API_KEY=your_api_key_here
```

## Future Improvements

- Streamlit web interface
- URL-based fact checking
- Multi-language support
