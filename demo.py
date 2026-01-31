from text_preprocessor_toolkit.preprocess import TextPreprocessor, PreprocessConfig

# text = """
# Natural Language Processing is amazing! I am learning NLP in 2026,
# and I loved cleaning text: removing punctuation, stopwords, and lemmatizing tokens.
# """

#text can be taken from user
text = input()  

config = PreprocessConfig(
    lowercase=True,
    remove_punct=True,
    remove_numbers=True,
    remove_stopwords=True,
    lemmatize=True,
    min_token_len=2
)

tp = TextPreprocessor(model="en_core_web_sm", config=config)
result = tp.full_pipeline(text, top_k=10)

print("Tokens:", result["tokens"])
print("\nTop words:")
for w, c in result["top_k"]:
    print(f"{w}: {c}")
