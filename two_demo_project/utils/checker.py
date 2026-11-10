from .cleaner import clean_text

def is_valid(text,min_len=10):
    cleaned = clean_text(text)
    return len(cleaned) >= min_len