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

## Example 
 
## Input
Natural Language Processing is amazing! I am learning NLP in 2026.

## Output
Tokens: ['natural', 'language', 'processing', 'amazing', 'learn', 'nlp']

Top words:
natural: 1
language: 1
processing: 1
amazing: 1
learn: 1
nlp: 1

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm

