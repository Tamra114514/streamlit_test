import streamlit as st


def main(rate):
    st.title('proper risk calculator result DEMO')
    st.title('入力情報をもとに計算された提示するべき金利は以下の通りです。')
    st.title('{:.2f}%です。'.format(rate))

if __name__ == '__main__':
    main()