
def calc_pool(sex, education):
    if sex == 'male':
        if education != 'Highschool':
            return 'poolA'
        else:
            return 'poolC'
    elif sex == 'female':
        return 'poolB'
    else:
        return 'poolC'

def decide_pd(pool):
    if pool == 'poolA':
        return 0.05
    elif pool == 'poolB':
        return 0.06
    elif pool == 'poolC':
        return 0.07
    else:
        return 'error'

def calc_ra(exposure, pool):
    if pool == 'poolA':
        return exposure * 0.45
    elif pool == 'poolB':
        return exposure * 0.75
    elif pool == 'poolC':
        return exposure * 1.25
    else:
        return 'error'
"""
実際のRA算出式とは異なる。あくまでデモ
"""
    
def calc_proper_rate(exposure, pool, rora):
    ra = calc_ra(exposure, pool)
    return ((rora * ra)/(exposure)) * 100


def main():
    return 0

if __name__ == '__main__':
    main()