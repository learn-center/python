import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hello Title")
st.write("Sample text")

st.text_input("Enter Text Input")

df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
st.write(df)

file = st.file_uploader("Upload a file:")
if file is not None:
    df = pd.read_csv(file)
    df.set_index("Id", inplace=True)
    st.write(df)
    st.bar_chart(df)

button_clicked = st.button("Generate Charts")
if button_clicked:
    data = {
        "Fruits": ["Appple", "Oranges", "Cherries"],
        "Quantitites": [10, 20, 15],
    }

    fig, ax = plt.subplots()
    ax.bar(data["Fruits"], data["Quantitites"], color=["red", "Green", "Blue"])

    ax.set_title("Sample Charts")
    ax.set_xlabel("Fruits")
    ax.set_ylabel("Quantities")

    st.pyplot(fig)
