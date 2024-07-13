import streamlit as st
import pandas as pd
import numpy as np

# Generar datos de ejemplo
num_samples = st.number_input("Número de muestras:", min_value=1, value=10)
data = np.random.rand(num_samples, 3)  # Genera datos aleatorios
df = pd.DataFrame(data, columns=['Col1', 'Col2', 'Col3'])

st.write("Datos generados:")
st.write(df)

# Guardar datos en un archivo CSV
file_path = 'generated_data.csv'
df.to_csv(file_path, index=False)

st.success(f'Datos guardados en {file_path}')
