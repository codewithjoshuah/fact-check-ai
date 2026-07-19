# 📰 AI Fact Checker

An AI-powered fact-checking system that combines **Machine Learning**, **Natural Language Processing (NLP)**, **Semantic Search**, **Natural Language Inference (NLI)**, and **Web Retrieval** to analyze news claims and determine whether they are supported by evidence from trusted sources.

Unlike traditional fake news detectors that rely only on writing style, this project retrieves real-world evidence and uses multiple AI techniques to make an informed decision.

---

## 🚀 Features

- 🧠 Machine Learning-based fake/real prediction
- 🔍 Automatic claim extraction
- 🌐 Live web search using Tavily Search API
- ⭐ Source credibility scoring
- 📖 Semantic evidence retrieval using Sentence Transformers
- ⚖️ Natural Language Inference (Support / Contradict / Neutral)
- 🗑️ Duplicate evidence removal
- 📊 Evidence ranking
- ✅ Final evidence-based verdict with confidence score

---

## 🏗️ System Architecture

```
                User Input
                    │
                    ▼
           Text Preprocessing
                    │
                    ▼
            Machine Learning Model
                    │
                    ▼
             Claim Extraction
                    │
                    ▼
          Tavily Evidence Retrieval
                    │
                    ▼
         Source Credibility Analysis
                    │
                    ▼
        Semantic Evidence Matching
                    │
                    ▼
     Natural Language Inference (NLI)
                    │
                    ▼
        Evidence Deduplication
                    │
                    ▼
            Evidence Ranking
                    │
                    ▼
           Rule-Based Reasoning
                    │
                    ▼
          Final Fact Check Result
```

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Logistic Regression
- TF-IDF Vectorizer

### Natural Language Processing

- NLTK
- Sentence Transformers
- Hugging Face Transformers

### Information Retrieval

- Tavily Search API

### Models Used

- all-MiniLM-L6-v2
- MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli

### Libraries

- Joblib
- NumPy
- Pandas
- Torch
- Transformers
- Sentence-Transformers

---

## 📂 Project Structure

```
fact-check-ai/
│
├── app.py
├── test.py
├── preprocessing.py
├── train_model.py
├── ml_engine.py
├── claim_extractor.py
├── retriever.py
├── credibility.py
├── evidence.py
├── nli.py
├── deduplicator.py
├── ranker.py
├── reasoner.py
├── config.py
├── requirements.txt
│
├── model/
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── data/
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/fact-check-ai.git
cd fact-check-ai
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
TAVILY_API_KEY=YOUR_API_KEY
```

---

## ▶️ Running the Project

Run

```bash
python test.py
```

Example

```
Enter a claim:

NASA discovered intelligent life on Mars.

Analyzing...

==========================================

VERDICT: FALSE

Confidence: 96.4%

Summary:
The claim is contradicted by trusted evidence.

==========================================
```

---

## 📌 How It Works

1. The input text is preprocessed.
2. The Machine Learning model predicts whether the writing resembles fake or real news.
3. Claims are extracted from the text.
4. Tavily retrieves relevant online evidence.
5. Sources are assigned credibility scores.
6. Semantic Search finds the most relevant evidence.
7. An NLI model determines whether each piece of evidence supports or contradicts the claim.
8. Duplicate evidence is removed.
9. Remaining evidence is ranked.
10. The reasoning engine combines all results to produce the final verdict.

---

## 📈 Future Improvements

- Streamlit Web Interface
- URL-based news verification
- PDF and document analysis
- Multi-language support
- Local LLM integration (Ollama)
- Explainable AI dashboard

---

## 👨‍💻 Author

**Joshuah Gnanraj**

GitHub: https://github.com/codewithjoshuah

LinkedIn: *(Add your LinkedIn profile here)*

---

## 📜 License

This project is licensed under the MIT License.
