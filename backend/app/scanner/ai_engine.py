
def confidence_score(oi_change, volume):
    score = min(abs(oi_change) / 500, 1.0)
    vol_factor = min(volume / 100000, 1.0)
    return round((score * 0.7 + vol_factor * 0.3), 2)
