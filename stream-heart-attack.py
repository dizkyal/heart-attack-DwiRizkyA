import pickle
import streamlit as st

# membaca model
heart_model =  pickle.load(open('heart_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Serangan Jantung')

Age = st.text_input('Masukan Umur')

sex = st.text_input('Masukan Jenis Kelamin')

chest_pain_type = st.text_input('Masukan Jenis Nyeri Pada Dada')

resting_blood_pressure = st.text_input('Masukan Hasil Tekanan Darah')

cholestoral = st.text_input('Masukan Hasil Kolesterol')

fasting_blood_sugar = st.text_input('Masukan Hasil Gula Darah')

resting_electrocardiographic_results = st.text_input('Masukan Hasil Elektrokardiografi')

maximum_heart_rate_achieved = st.text_input('Masukan Hasil Detak Jantung Maksimal')

exercise_induced_angina = st.text_input('Masukan Hasil Angina Akibat Olahraga')

oldpeak = st.text_input('Masukan Hasil depresi yang diakibatkan oleh latihan relative')

slope_of_the_peak_exercise = st.text_input('Masukan Hasil Tekanan Depresi Maksimal')

number_of_major_vessels = st.text_input('Masukan Hasil Pembuluh Darah Utama')

Thalassemia = st.text_input('Masukan Hasil Kelainan Darah')

# code untuk kelompok jenis bunga
heart_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    heart_prediction = heart_model.predict([[Age, sex, chest_pain_type, resting_blood_pressure, cholestoral, fasting_blood_sugar, resting_electrocardiographic_results, maximum_heart_rate_achieved, exercise_induced_angina, oldpeak, slope_of_the_peak_exercise, number_of_major_vessels, Thalassemia]])
    
    if(heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terkena Serangan Jantung'
    else :
        heart_diagnosis = 'Pasien tidak Terkena Serangan Jantung'

    st.success(heart_diagnosis)