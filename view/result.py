import streamlit as st


def main(rate):
    st.title('proper risk calculator result DEMO')
    st.write('入力情報をもとに計算された提示するべき金利は以下の通りです。')
    st.write('{:.2f}%です。'.format(rate))

if __name__ == '__main__':
    main()