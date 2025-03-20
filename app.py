import streamlit as st
import sqlite3

veza = sqlite3.connect("biblioteka.db")
veza.execute("CREATE TABLE IF NOT EXISTS knjige(naslov TEXT, autor TEXT)")

st.title("Biblioteka knjiga")

naslov = st.text_input("Naslov knjige:")
autor = st.text_input("Autor knjige:")

if st.button("Spremi knjigu"):
    veza.execute("INSERT INTO knjige VALUES (?,?)", (naslov, autor))
    veza.commit()
    st.success(f"Spremljena knjiga: {naslov} - {autor}")

if st.button("Prikaži sve knjige"):
    knjige = veza.execute("SELECT naslov, autor FROM knjige").fetchall()
    for k in knjige:
        st.write(f"{k[0]} - {k[1]}")


