import numpy as np
import pandas as pd
from scipy.stats import norm

def calc_pd(exposure, work_year):
    logexposure = np.log(exposure)
    if logexposure <= 12.086:
        if work_year == 0:
            return 0.0411
        elif work_year > 0 and work_year <= 4.756:
            return 0.0947
        elif work_year > 4.756:
            return 0.029
        else:
            pass
    elif logexposure > 12.086 and logexposure <= 12.324:
        if work_year == 0:
            return 0.0297
        elif work_year > 0 and work_year <= 4.756:
            return 0.1115
        elif work_year > 4.756 and work_year <= 6.614:
            return 0.0941
        elif work_year > 6.614:
            return 0.0622
        else:
            pass
    elif logexposure > 12.324 and logexposure <= 12.933:
        if work_year == 0:
            return 0.0489
        elif work_year > 0 and work_year <= 2.301:
            return 0.1037
        elif work_year > 2.301 and work_year <= 4.756:
            return 0.0882
        elif  work_year > 4.756 and work_year <= 9.036:
            return 0.0696
        elif work_year > 9.036:
            return 0.0451
        else:
            pass
    elif logexposure > 12.933 and logexposure <= 13.025:
        if work_year == 0:
            return 0.0693
        elif work_year > 0 and work_year <= 4.756:
            return 0.1320
        elif work_year > 4.756 and work_year <= 9.036:
            return 0.0882
        elif work_year > 9.036:
            return 0.0592
        else:
            pass
    elif logexposure > 13.025:
        if work_year == 0:
            return 0.0467
        elif work_year > 0 and work_year <= 4.756:
            return 0.0622
        elif work_year > 4.756 and work_year <= 13.658:
            return 0.0445
        elif work_year > 13.658:
            return 0.0327
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
    

def calc_proper_rate(pd, exposure, rora):
    ra = calc_ra(pd, exposure)
    return ((rora * ra)/(exposure)) * 100


def main():
    return 0

if __name__ == '__main__':
    main()