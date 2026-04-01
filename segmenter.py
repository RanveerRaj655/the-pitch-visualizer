import nltk

# Download NLTK punkt tokenizer on first run
nltk.download('punkt', quiet=True)

def segment_text(text: str) -> list[str]:
    """
    Splits text into sentences using nltk.sent_tokenize.
    If there are more than 6 sentences, merges consecutive sentences in pairs
    so the final panel count is ideally 3-6.
    """
    sentences = nltk.sent_tokenize(text)
    
    while len(sentences) > 6:
        merged = []
        for i in range(0, len(sentences), 2):
            if i + 1 < len(sentences):
                merged.append(sentences[i] + " " + sentences[i+1])
            else:
                merged.append(sentences[i])
        sentences = merged

    return sentences
