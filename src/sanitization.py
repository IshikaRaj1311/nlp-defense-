import unicodedata
import re

HOMOGLYPH_MAP = {
    "а": "a",  # Cyrillic a
    "е": "e",  # Cyrillic e
    "о": "o",  # Cyrillic o
    "р": "p",
    "с": "c",
    "у": "y",
    "х": "x",
}

# Covers major emoji Unicode blocks
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002700-\U000027BF"
    "]+",
    flags=re.UNICODE
)

def normalize_unicode(text: str) -> str:
    """Normalize Unicode characters (NFKC) to canonical form."""
    text = unicodedata.normalize("NFKC", text)
    
    # Replace known homoglyphs
    text = "".join(HOMOGLYPH_MAP.get(ch, ch) for ch in text)
    return text

def remove_emojis(text: str) -> str:
    """Remove emoji characters from text."""
    return EMOJI_PATTERN.sub("", text)

def normalize_whitespace(text: str) -> str:
    """Collapse multiple whitespace into single spaces."""
    return " ".join(text.split())

def sanitize(text: str) -> str:
    """
    Full sanitization pipeline:
    1. Unicode normalization
    2. Emoji removal
    3. Lowercasing (model consistency)
    4. Whitespace normalization
    """
    text = normalize_unicode(text)
    text = remove_emojis(text)
    text = text.lower()
    text = normalize_whitespace(text)
    return text.strip()