# Crear un diccionario con información personal
mi_informacion = {
    "nombre": "Jean Carlos",
    "edad": 48,
    "ciudad": "Tandil",
    "profesion": "Analista QA",
    "hobbies": ["lectura", "running", "testing"],
    "lenguajes_programacion": ["Python", "JavaScript", "C#"],
    "experiencia": "3 años en testing manual",
    "meta_profesional": "Convertirme en QA Automation"
}

# Mostrar todos los elementos del diccionario en la terminal
print("Información personal:")
for clave, valor in mi_informacion.items():
    print(f"{clave}: {valor}")
