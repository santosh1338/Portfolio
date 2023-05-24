import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Santosh C")
    content = """
    aaaaaaaaaaaaaasahschfghf hhfvhxvjwgfbxwbqbbbkqkyfvcqbcyycvwvfcwwvbwuyqvtquubqucbvufwbycbuywfwvcfqwbuqcwqkcbqcbkwqcqw
    cvqkc
    """
    st.info(content)

st.write("Below you can find some of the other apps that I have built. Feel free to contact me!")

col3, cole, col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write("[Source Code](https://youtube.com)")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write("[Source Code](https://youtube.com)")