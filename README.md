# NLP Text Preprocessing (spaCy)

A configurable text preprocessing toolkit built using Python and spaCy.
It supports cleaning, tokenization, stopword removal, lemmatization, and word frequency analysis.

## Features
- Lowercasing
- Punctuation removal
- Number removal (optional)
- Stopword removal
- Lemmatization
- Min token length filter
- Top-K word frequency

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
