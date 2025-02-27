import streamlit as st
import requests
import json

# Configuración de la URL base de la API
API_URL = "http://localhost:8000"

st.title("Gestión de Usuarios")
st.write("Aplicación para gestionar usuarios con DNI y nombre")

# Crear pestañas para diferentes funcionalidades
tab1, tab2 = st.tabs(["Registrar Usuario", "Consultar Usuarios"])

with tab1:
    st.header("Registrar Nuevo Usuario")
    
    # Formulario para registrar un nuevo usuario
    with st.form("registro_usuario"):
        dni = st.text_input("DNI")
        nombre = st.text_input("Nombre")
        submitted = st.form_submit_button("Registrar Usuario")
        
        if submitted:
            if dni and nombre:
                try:
                    response = requests.post(
                        f"{API_URL}/usuarios/",
                        json={"dni": dni, "nombre": nombre}
                    )
                    
                    if response.status_code == 200:
                        st.success(f"Usuario {nombre} registrado correctamente")
                    else:
                        error_detail = response.json().get("detail", "Error desconocido")
                        st.error(f"Error al registrar usuario: {error_detail}")
                except Exception as e:
                    st.error(f"Error de conexión: {str(e)}")
            else:
                st.warning("Por favor, complete todos los campos")

with tab2:
    st.header("Consultar Usuarios")
    
    # Botón para refrescar la lista de usuarios
    if st.button("Refrescar Lista"):
        try:
            response = requests.get(f"{API_URL}/usuarios/")
            
            if response.status_code == 200:
                usuarios = response.json()
                if usuarios:
                    # Mostrar tabla de usuarios
                    st.write("Lista de Usuarios:")
                    usuarios_data = {"DNI": [], "Nombre": []}
                    
                    for usuario in usuarios:
                        usuarios_data["DNI"].append(usuario["dni"])
                        usuarios_data["Nombre"].append(usuario["nombre"])
                    
                    st.table(usuarios_data)
                else:
                    st.info("No hay usuarios registrados")
            else:
                st.error("Error al obtener la lista de usuarios")
        except Exception as e:
            st.error(f"Error de conexión: {str(e)}")
    
    # Buscar usuario por DNI
    st.subheader("Buscar Usuario por DNI")
    dni_busqueda = st.text_input("Ingrese el DNI a buscar")
    
    if st.button("Buscar"):
        if dni_busqueda:
            try:
                response = requests.get(f"{API_URL}/usuarios/{dni_busqueda}")
                
                if response.status_code == 200:
                    usuario = response.json()
                    st.write(f"**DNI:** {usuario['dni']}")
                    st.write(f"**Nombre:** {usuario['nombre']}")
                else:
                    st.warning("Usuario no encontrado")
            except Exception as e:
                st.error(f"Error de conexión: {str(e)}")
        else:
            st.warning("Por favor, ingrese un DNI para buscar")
