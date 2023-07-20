import streamlit as st
import numpy as np

st.markdown("""
            <style>
            footer {visibility: hidden;}
            </style> """, unsafe_allow_html=True)

st.title('Ujian Tasmi\'')

st.subheader('Hitung Nilai')
ayat = st.number_input('Jumlah Ayat', 1, step=1)

salah = st.number_input('Kesalahan', 0.0, float(ayat), step=.5)
st.error(f'Kesalahan : {salah}')

nilai = np.floor((ayat-salah)*100/ayat)

st.subheader('Hasil')
st.success(f'Nilai: {nilai}')

st.write('Dibuat dengan ❤ oleh Abdi S Wardoyo')
