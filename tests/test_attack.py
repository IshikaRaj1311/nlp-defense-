from src.attack_generator import unicode_attack

def test_unicode_attack():
    text = "attack"
    attacked = unicode_attack(text)
    assert isinstance(attacked, str)
