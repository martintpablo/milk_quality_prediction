import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("model/milk_q_model.pkl")

st.set_page_config(layout="wide")

st.title('**Milk quality prediction**')

st.image("https://www.southernliving.com/thmb/zCKBQZG85v0gxUpn5Nm_8elGJaA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1413944242-79c406e0bbe4435596bc671f95a949cb.jpg", width=400)

ph = st.number_input('pH', 0.0, 14.0, key="pH")

temperature = st.number_input('Temperature', 0.0, 40.0, key="temperature")

taste = st.selectbox(
    'Sabor',
    ('Buen sabor', 'Mal sabor'), key="taste")

odor = st.selectbox(
    'Olor',
    ('Buen olor', 'Mal olor'), key="odor")

fat = st.selectbox(
    'Grasas',
    ('Contiene grasas', 'Pocas o grasas nulas'), key="fat")
  
turdibity = st.selectbox(
    'Turbidez',
    ('Sí', 'No'), key="turdibity")

colour_slider = st.slider("Selecciona el color", 240, 255, key="colour_slider")
# colour_hex = "#{:02x}{:02x}{:02x}".format(colour_slider, colour_slider, colour_slider)
st.markdown(f"Color seleccionado: <span style='background-color:rgb({colour_slider}, {colour_slider}, {colour_slider}); padding-left: 50px; padding-right: 50px; width: 100px; height: 100px;border:1px solid black'> &nbsp; </span>", unsafe_allow_html=True)

if st.button("Enviar"):
  X = pd.DataFrame([[ph, temperature, taste, odor, fat, turdibity, colour_slider]], columns=["pH", "Temprature", "Taste", "Odor", "Fat ", "Turbidity", "Colour"])
  X = X.replace(["Buen sabor", "Mal sabor", "Buen olor", "Mal olor", "Contiene grasas", "Pocas o grasas nulas", "Sí", "No"], [1, 0, 0, 1, 1, 0, 1, 0])
  prediction = clf.predict(X)[0]
  st.text(f"The milk quality is {prediction}")