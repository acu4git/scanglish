import streamlit as st

from pages import dashboard, word_input, word_search, generate_sentence
from auth import authenticate
from database import init_db


def main():
    st.set_page_config(page_title="Scanglish", page_icon="🔍")

    init_db()

    if "username" not in st.session_state:
        authenticate()
    else:
        st.sidebar.title(f"Welcome, {st.session_state['username']}!")
        st.sidebar.button("Logout", on_click=logout)

        pages = {
            "ダッシュボード": dashboard,
            "画像読み込み": word_input,
            "単語帳": word_search,
            "文章生成": generate_sentence,
        }

        page = st.sidebar.radio("ナビゲーション", list(pages.keys()))
        pages[page](st.session_state.username)


def logout():
    st.session_state.username = None


if __name__ == "__main__":
    main()
