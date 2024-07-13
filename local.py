import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Definir la interfaz de Streamlit
st.title('Modificación de Archivo CSV en GitHub')

# URL del archivo CSV en GitHub
url = 'https://raw.githubusercontent.com/Edithson1/sistemas/main/archivos.csv'

# Función para descargar y modificar el archivo CSV
def modificar_csv(numero):
    # Descargar el archivo CSV y leerlo
    response = requests.get(url)
    if response.status_code == 200:
        # Convertir la respuesta a un StringIO para que Pandas pueda leerlo
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content)
        
        # Añadir una nueva fila al DataFrame
        nueva_fila = pd.DataFrame({'Numero': [numero]})
        df = pd.concat([df, nueva_fila], ignore_index=True)
        
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
