import numpy as np
import pandas as pd
from scipy.stats import norm

def calc_pd(exposure, work_year):
    logexposure = np.log(exposure)
    if logexposure <= 12.086:
        if work_year == 0:
            return 0.01
        elif work_year > 0 and work_year <= 4.756:
            return 0.02
        elif work_year > 4.756:
            return 0.03
        else:
            pass
    elif logexposure > 12.086 and logexposure <= 12.324:
        if work_year == 0:
            return 0.04
        elif work_year > 0 and work_year <= 4.756:
            return 0.05
        elif work_year > 4.756 and work_year <= 6.614:
            return 0.06
        elif work_year > 6.614:
            return 0.07
        else:
            pass
    elif logexposure > 12.324 and logexposure <= 12.933:
        if work_year == 0:
            return 0.08
        elif work_year > 0 and work_year <= 2.301:
            return 0.09
        elif work_year > 2.301 and work_year <= 4.756:
            return 0.1
        elif  work_year > 4.756 and work_year <= 9.036:
            return 0.11
        elif work_year > 9.036:
            return 0.12
        else:
            pass
    elif logexposure > 12.933 and logexposure <= 13.025:
        if work_year == 0:
            return 0.13
        elif work_year > 0 and work_year <= 4.756:
            return 0.14
        elif work_year > 4.756 and work_year <= 9.036:
            return 0.15
        elif work_year > 9.036:
            return 0.16
        else:
            pass
    elif logexposure > 13.025:
        if work_year == 0:
            return 0.17
        elif work_year > 0 and work_year <= 4.756:
            return 0.18
        elif work_year > 4.756 and work_year <= 13.658:
            return 0.19
        elif work_year > 13.658:
            return 0.20
        else:
            pass

def calc_ra(pd, exposure):
    lgd = 1.0
    el = pd * lgd
    gpd = norm.ppf(pd)
    R = 0.03 * ((1 - np.exp(-35 * pd))/(1 - np.exp(-35))) + 0.06 * (1 - ((1 - np.exp(-35 * pd))/(1- np.exp(-35))))
    K = lgd * norm.cdf((np.sqrt((1-R)**(-1)) * gpd)+(np.sqrt(R/(1-R)*norm.ppf(0.999)))) - el
    RA = K * 12.5 * exposure
    return RA
    
"""
実際のRA算出式とは異なる。あくまでデモ
"""
    
def calc_proper_rate(pd, exposure, rora):
    ra = calc_ra(pd, exposure)
    return ((rora * ra)/(exposure)) * 100


def main():
    return 0

if __name__ == '__main__':
    main()