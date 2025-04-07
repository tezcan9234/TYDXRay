# visualization/intelligent_overlay.py

def classify_by_density(density):
    """
    Manyetik yoğunluğa göre nesne sınıflandırması ve renk döner.
    """
    if density > 0.8:
        return "Metal", "red"
    elif density > 0.6:
        return "Heykel", "green"
    elif density > 0.4:
        return "Taş Blok", "orange"
    elif density > 0.2:
        return "Boşluk", "blue"
    else:
        return "Zayıf Alan", "gray"
