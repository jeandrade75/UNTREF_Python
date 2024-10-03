""" Tendrán que armar una lista de 5 nombres, y mostrarlos a
todos en terminal. Luego remover el nombre en la posición 3
y poner un nuevo nombre al final de la lista. Mostrar en
terminal cómo quedaría después. """

# Crear una lista de 5 nombres
nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

# Mostrar la lista original en la terminal
print("Lista original de nombres:", nombres)

# Remover el nombre en la posición 3 (índice 2)
nombres.pop(2)

# Agregar un nuevo nombre al final de la lista
nombres.append("Fernando A")

# Mostrar la lista actualizada en la terminal
print("Lista de nombres después de los cambios:", nombres)
