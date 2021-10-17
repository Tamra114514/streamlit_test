import os
import sys

import numpy as np
import pandas as pd
import streamlit as st

from model import calc_risk as cr
from view import result

st.title('proper risk calculator DEMO')

st.write('本アプリケーションは、顧客情報の入力後にプール区分を判定し、目標収益を達成するために必要な金利を出力します。(DEMO版の目標収益率は6%です。)')

rora = 0.09 #目標収益率

company = st.text_input('顧客の所属する企業を入力してください')

work_year = st.number_input('勤続年数を入力してください',
                          value=1)

st.number_input('顧客の同居家族は何人ですか？',
                          value=1)

exposure = st.number_input('顧客のローン希望額を入力してください。単位は円です。',
                          value=1)

execution = st.button('計算開始')

if execution == True:
    pd = cr.calc_pd(exposure, work_year)
    rate = cr.calc_proper_rate(pd, exposure, rora)
    result.main(rate)
else:
    pass


"""
author:takuma tamura
"""