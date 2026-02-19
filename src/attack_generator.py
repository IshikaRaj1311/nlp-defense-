import random
import pandas as pd

# Unicode homoglyph map (simplified)
HOMOGLYPHS = {
    'a': 'а',  # Cyrillic a
    'o': 'о',  # Cyrillic o
    'e': 'е',
    'c': 'с'
}

EMOJIS = ["🔥", "💀", "🎯", "⚠️", "💣"]

def unicode_attack(text):
    attacked = ""
    for ch in text:
        if ch in HOMOGLYPHS and random.random() < 0.5:
            attacked += HOMOGLYPHS[ch]
        else:
            attacked += ch
    return attacked

EMOJIS = ["🔥", "💀", "💣", "⚠️", "🎯"]

def strong_emoji_attack(text):
    attacked = ""
    for ch in text:
        attacked += ch

        # Insert emoji inside words randomly
        if ch.isalpha() and random.random() < 0.3:
            attacked += random.choice(EMOJIS)

    return attacked

def emoji_replacement_attack(text):
    attacked = ""
    for ch in text:
        if ch.lower() in ["a", "o", "e", "i"] and random.random() < 0.5:
            attacked += random.choice(EMOJIS)
        else:
            attacked += ch
    return attacked


def whitespace_attack(text):
    return " ".join(list(text))

def generate_attacks(clean_prompts):
    data = []
    for prompt in clean_prompts:
        data.append(("unicode", prompt, unicode_attack(prompt)))
        data.append(("emoji_insertion", prompt, strong_emoji_attack(prompt)))
        data.append(("emoji_replacement", prompt, emoji_replacement_attack(prompt)))
        data.append(("whitespace", prompt, whitespace_attack(prompt)))
    return pd.DataFrame(data, columns=["type", "clean", "adversarial"])
