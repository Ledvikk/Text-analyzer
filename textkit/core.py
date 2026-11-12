def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())

def count_words(text: str) -> int:
    return len(text.split())