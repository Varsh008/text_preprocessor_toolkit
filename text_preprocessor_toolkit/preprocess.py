import re
from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional

import spacy


@dataclass
class PreprocessConfig:
    lowercase: bool = True
    remove_punct: bool = True
    remove_numbers: bool = False
    remove_stopwords: bool = True
    lemmatize: bool = True
    keep_pos: Optional[set] = None  
    min_token_len: int = 2          


class TextPreprocessor:
    """
    A simple text preprocessing toolkit using spaCy:
    - cleaning
    - tokenization
    - lemmatization
    - stopword removal
    - word frequency counts
    """

    def __init__(self, model: str = "en_core_web_sm", config: Optional[PreprocessConfig] = None):
        self.nlp = spacy.load(model, disable=["ner", "parser"])  # faster, we only need tokens/lemmas
        self.config = config or PreprocessConfig()

    def _basic_clean(self, text: str) -> str:
        if self.config.lowercase:
            text = text.lower()

        # normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()

        if self.config.remove_numbers:
            text = re.sub(r"\d+", "", text)
            text = re.sub(r"\s+", " ", text).strip()

        return text

    def preprocess(self, text: str) -> List[str]:
    
        text = self._basic_clean(text)
        doc = self.nlp(text)

        tokens: List[str] = []
        for token in doc:
            # Skip spaces
            if token.is_space:
                continue

            # Remove punctuation 
            if self.config.remove_punct and token.is_punct:
                continue

            # Remove stopwords
            if self.config.remove_stopwords and token.is_stop:
                continue

            # keep only certain POS tags
            if self.config.keep_pos is not None and token.pos_ not in self.config.keep_pos:
                continue

            # Choose lemma or original token
            out = token.lemma_ if self.config.lemmatize else token.text

            # Clean leftovers 
            out = out.strip()
            if not out:
                continue

            # filter very short tokens
            if len(out) < self.config.min_token_len:
                continue

            tokens.append(out)

        return tokens

    def word_frequencies(self, tokens: List[str], top_k: int = 20) -> List[Tuple[str, int]]:
        """
        Returns top_k most common tokens and their counts.
        """
        counter = Counter(tokens)
        return counter.most_common(top_k)

    def full_pipeline(self, text: str, top_k: int = 20) -> Dict:
        """
        Convenience method: preprocess + word frequency.
        """
        tokens = self.preprocess(text)
        freqs = self.word_frequencies(tokens, top_k=top_k)
        return {
            "num_tokens": len(tokens),
            "tokens": tokens,
            "top_k": freqs,
        }
