import os
import sys

import numpy as np
import pandas as pd
import streamlit as st

from model import calc_risk as cr
from view import result

st.title('proper risk calculator DEMO')

st.write('本アプリケーションは、顧客情報の入力後にプール区分を判定し、目標収益を達成するために必要な金利を出力します。')

rora = 0.06 #目標収益率

sex = st.selectbox('顧客の性別は何ですか？',
                  ('male', 'female'))

education = st.selectbox('顧客の学歴は何ですか？',
                        ('Doctor', 'Master', 'Bachelor', 'Highschool'))

exposure = st.number_input('顧客のローン希望額を入力してください。単位は円です。',
                          value=1)

execution = st.button('計算開始')

pool = cr.calc_pool(sex, education)
pd = cr.decide_pd(pool)
rate = cr.calc_proper_rate(exposure, pool, rora)

if execution == True:
    result.main(rate)
else:
    pass