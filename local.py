import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Definir la interfaz de Streamlit
st.title('Modificación de Archivo CSV en GitHub')

# URL del archivo CSV en GitHub
url = 'https://github.com/Edithson1/sistemas/blob/main/generated_data.csv'

# Función para descargar y modificar el archivo CSV
def modificar_csv(numero):
    # Descargar el archivo CSV y leerlo
    response = requests.get(url)
    if response.status_code == 200:
        # Convertir la respuesta a un StringIO para que Pandas pueda leerlo
        df = pd.read_csv(url)
        
        # Modificar el DataFrame
        nueva_fila = {'Numero': numero}
        df = df.append(nueva_fila, ignore_index=True)
        
        # Guardar el DataFrame modificado en un nuevo archivo CSV localmente
        df.to_csv('datos_modificados.csv', index=False)
        
        # Mostrar mensaje de éxito
        st.success('Archivo CSV modificado y guardado localmente.')
    else:
        st.error(f'Error al descargar el archivo CSV. Código de estado: {response.status_code}')

# Entrada del usuario en Streamlit
numero = st.number_input('Ingrese un número entero', min_value=1, step=1)

# Botón para modificar el archivo CSV
if st.button('Modificar Archivo CSV'):
    modificar_csv(numero)
