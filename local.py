import streamlit as st
import subprocess

# Definir la interfaz de Streamlit
st.title('Suma de Números Enteros')

# Entrada del usuario en Streamlit
numero = st.number_input('Ingrese un número entero', min_value=1, step=1)

# Botón para ejecutar el programa C
if st.button('Calcular Suma'):
    # Ejecutar el código C con el número ingresado como argumento
    result = subprocess.run(['./actividad', str(int(numero))], capture_output=True, text=True, stderr=subprocess.PIPE)
    print(result.stderr)

    
    # Mostrar resultados
    if result.returncode == 0:
        st.write(f'La suma de los números enteros hasta {numero} es: {result.stdout.strip()}')
    else:
        st.write('Error al calcular la suma.')


