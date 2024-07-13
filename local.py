import streamlit as st
import pandas as pd
import numpy as np
import os
import subprocess

# Función para obtener la ruta del ejecutable
def get_executable_path():
    return os.path.dirname(os.path.abspath(__file__))

# Función para ejecutar comandos de git
def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        st.error(f"Error ejecutando el comando {command}: {result.stderr}")
    return result.stdout

# Generar datos de ejemplo
num_samples = st.number_input("Número de muestras:", min_value=1, value=10)
data = np.random.rand(num_samples, 3)  # Genera datos aleatorios
df = pd.DataFrame(data, columns=['Col1', 'Col2', 'Col3'])

st.write("Datos generados:")
st.write(df)

# Guardar datos en la ruta del ejecutable al presionar el botón
if st.button('Guardar datos'):
    executable_path = get_executable_path()
    file_path = os.path.join(executable_path, 'generated_data.csv')
    df.to_csv(file_path, index=False)
    st.success(f'Datos guardados en {file_path}')

    # Ejecutar el programa en C para calcular la suma
    os.system('./sum_program')  # Asegúrate de que el programa en C esté compilado y se llame sum_program

    # Leer el archivo con las sumas
    sum_file_path = os.path.join(executable_path, 'sums.txt')
    with open(sum_file_path, 'r') as sum_file:
        sums = sum_file.read()

    st.write("Sumas calculadas por el programa en C:")
    st.text(sums)

    # Configurar la identidad del usuario si no está configurada
    run_git_command(['git', 'config', '--global', 'user.email', 'akuntsueharu@gmail.com'])
    run_git_command(['git', 'config', '--global', 'user.name', 'Edithson1'])
    # Agregar los archivos cambiados a git
    run_git_command(['git', 'add', 'generated_data.csv', 'sums.txt'])
    # Hacer commit de los cambios
    commit_message = f"Actualizados los archivos generated_data.csv y sums.txt con {num_samples} muestras"
    run_git_command(['git', 'commit', '-m', commit_message])
    # Hacer push de los cambios
    run_git_command(['git', 'push', 'origin', 'main'])
    st.success("Cambios subidos a GitHub")

