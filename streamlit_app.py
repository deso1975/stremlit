# импотираме библиотека Streamlit с име st
import streamlit as st

#от библиотеката PIL wkwrwame samo IMAGE
#izpolzwvame bibliotekata za wizualizaciq na izobrajeniq
from PIL import Image

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)




left_column, right_column=st.columns(2)

with left_column:
    st.title("Първа проба")

    # inicializaciq na snimkata
    ivo = Image.open("IMG_20201026_093407_8.jpg")
    ivo_1= Image.open("IMG_20210503_181615_8.jpg")

    # otvarqne na snimkata
    st.image(ivo, width=200)


with right_column:
    st.write("Не знам какво правя")
    st.subheader("Не знам какво правя")


    st.image(ivo_1,width=100)

    int_A= st.number_input("Integer A:", )
    int_B = st.number_input("Integer B:", )
    int_C = st.number_input("Integer C:", )

    total_sum= int_A+int_B+int_C

    st.subheader(f"Сумата на А, Б и С е равна на: {total_sum}, [mm]")
