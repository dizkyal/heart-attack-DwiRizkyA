import pickle
import streamlit as st

# membaca model
heart_model =  pickle.load(open('heart_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Serangan Jantung')

Age = st.text_input('Masukan Umur')

sex = st.text_input('Masukan Jenis Kelamin')

cp = st.text_input('Masukan Jenis Nyeri Pada Dada')

trtbps = st.text_input('Masukan Hasil Tekanan Darah')

chol = st.text_input('Masukan Hasil Kolesterol')

fbs = st.text_input('Masukan Hasil Gula Darah')

restecg = st.text_input('Masukan Hasil Elektrokardiografi')

thalachh = st.text_input('Masukan Hasil Detak Jantung Maksimal')

exng = st.text_input('Masukan Hasil Angina Akibat Olahraga')

oldpeak = st.text_input('Masukan Hasil depresi yang diakibatkan oleh latihan relative')

slp = st.text_input('Masukan Hasil Tekanan Depresi Maksimal')

caa = st.text_input('Masukan Hasil Pembuluh Darah Utama')

thall = st.text_input('Masukan Hasil Kelainan Darah')

# code untuk kelompok jenis bunga
heart_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    heart_prediction = heart_model.predict([[Age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])
    if(heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terkena Serangan Jantung'
    else :
        heart_diagnosis = 'Pasien tidak Terkena Serangan Jantung'

    st.success(heart_diagnosis)
