
def oi_change_percent(current, previous):
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100
