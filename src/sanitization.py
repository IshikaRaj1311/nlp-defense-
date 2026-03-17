import unicodedata
import re

# Covers all major Unicode emoji blocks
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F9FF"  # transport, misc symbols
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"  # enclosed characters
    "\U0001FA00-\U0001FA6F"  # chess, symbols
    "\U0001FA70-\U0001FAFF"  # additional symbols
    "]+",
    flags=re.UNICODE
)

def normalize_unicode(text: str) -> str:
    """NFKC maps Cyrillic/homoglyph lookalikes back to canonical Latin."""
    return unicodedata.normalize("NFKC", text)

def remove_emojis(text: str) -> str:
    """Strip all emoji characters from text."""
    return EMOJI_PATTERN.sub("", text)

def normalize_whitespace(text: str) -> str:
    """Collapse all whitespace variants to single spaces."""
    return " ".join(text.split())

def sanitize(text: str) -> str:
    """
    Full sanitization pipeline:
    Unicode normalization → emoji removal → whitespace normalization
    """
    text = normalize_unicode(text)
    text = remove_emojis(text)
    text = normalize_whitespace(text)
    return text.strip()