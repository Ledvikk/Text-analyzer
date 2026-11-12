from textkit.core import normalize_whitespace, count_words

print(normalize_whitespace("  Ahoj\n  světe  "))
print(count_words("  Ahoj\n  světe  "))
print(count_words(""))                          