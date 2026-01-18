
def select_atm_strikes(spot, strikes, width=1):
    strikes = sorted(strikes)
    atm = min(strikes, key=lambda x: abs(x - spot))
    idx = strikes.index(atm)
    return strikes[max(0, idx-width): idx+width+1]
