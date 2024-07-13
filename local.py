import streamlit as st
import subprocess

# Definir la interfaz de Streamlit
st.title('Integración Streamlit con C')

# Entrada del usuario en Streamlit
input_value = st.number_input('Ingrese un número', value=0.0)

# Botón para ejecutar el programa C
if st.button('Ejecutar Código'):
    # Ejecutar el código C con el valor de entrada
    result = subprocess.run(['./actividad', str(input_value)], capture_output=True, text=True)
    
    # Mostrar resultados
    if result.returncode == 0:
        st.write('Resultado:')
        st.write(result.stdout)
    else:
        st.write('Error al ejecutar el programa C.')


