import streamlit as st
import pandas as pd
import numpy as np
import os

# Generar datos de ejemplo
num_samples = st.number_input("Número de muestras:", min_value=1, value=10)
data = np.random.rand(num_samples, 3)  # Genera datos aleatorios
df = pd.DataFrame(data, columns=['Col1', 'Col2', 'Col3'])

st.write("Datos generados:")
st.write(df)

# Función para obtener la ruta del ejecutable
def get_executable_path():
    return os.path.dirname(os.path.abspath(__file__))

# Guardar datos en la ruta del ejecutable al presionar el botón
if st.button('Guardar datos'):
    executable_path = get_executable_path()
    file_path = os.path.join(executable_path, 'generated_data.csv')
    df.to_csv(file_path, index=False)
    st.success(f'Datos guardados en {file_path}')

    # Ejecutar el programa en C para calcular la suma
    os.system(f'./sum_program')  # Asegúrate de que el programa en C esté compilado y se llame sum_program

    # Leer el archivo con las sumas
    sum_file_path = os.path.join(executable_path, 'sums.txt')
    with open(sum_file_path, 'r') as sum_file:
        sums = sum_file.read()

    st.write("Sumas calculadas por el programa en C:")
    st.text(sums)
