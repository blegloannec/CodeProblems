def survive(blood_type, donated_blood):
    mask = lambda blood: (int('B' in blood)<<2) | (int('A' in blood)<<1) | int('+' in blood)
    m0 = mask(blood_type)
    for blood in donated_blood:
        m = mask(blood)
        if m|m0==m0:
            return True
    return False