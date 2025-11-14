from biblioteca import Biblioteca
from data import data_libros, data_estudiantes
from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from libros import Libro
from usuarios import Profesor

biblioteca = Biblioteca("Biblioteca Central")

"""Estudiantes y Profesores"""
profesor = Profesor("Dr. Smith", "0000000001", "Ciencias")

"""Agregar usuarios a la biblioteca"""
biblioteca.usuarios = [profesor] + data_estudiantes
"""Agregar libros a la biblioteca"""
biblioteca.libros = data_libros


# print("Bienvenido a la biblioteca")
# print("Libros disponibles para préstamo:")
# for libro in biblioteca.libros_disponibles():
# 	print(libro.descripcion_completa)

# print()

# curp = input("Ingresa tu CURP para buscar tu usuario: ")

# try:
# 	usuario = biblioteca.buscar_usuario(curp)
# 	print(f"Usuario encontrado: {usuario.nombre} - CURP: {usuario.curp}")
# except UsuarioNoEncontradoError:
# 	print(f"El usuario no fue encontrado")

# titulo = input("Ingresa el título del libro que deseas solicitar: ")

# try:
# 	libro = biblioteca.buscar_libro(titulo)
# 	print(f"Libro encontrado: {libro.titulo} por {libro.autor}")
# except LibroNoDisponibleError:
# 	print(f"El libro con título {titulo} no está disponible.")

# resultado = (usuario.solicitar_libro(libro.titulo))
# print(f"\n{resultado}")

# resultado_prestamo = libro.prestar()
# print(f"\n{resultado_prestamo}")

# result = Biblioteca.validar_isbn("23")
# print(f"\n¿El ISBN es válido? {result}")

libro_no_disponible = Libro.crear_no_disponible("Libro No Disponible", "Autor Desconocido", "0000000000")

print(f"\nCreación de libro no disponible:\n{libro_no_disponible.descripcion_completa}")