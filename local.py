import streamlit as st
import pandas as pd

# Definir la interfaz de Streamlit
st.title('Modificación de Archivo CSV en GitHub')

# Entrada del usuario en Streamlit
numero = st.number_input('Ingrese un número entero', min_value=1, step=1)

# Botón para modificar el archivo CSV
if st.button('Modificar Archivo CSV'):
    # Leer el archivo CSV desde GitHub
    url = 'https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/datos.csv'
    df = pd.read_csv(url)
    
    # Modificar el DataFrame
    nueva_fila = {'Numero': numero}
    df = df.append(nueva_fila, ignore_index=True)
    
    # Guardar el DataFrame modificado de vuelta al archivo CSV en GitHub
    df.to_csv('datos.csv', index=False)
    st.success('Archivo CSV modificado correctamente en el repositorio GitHub.')
