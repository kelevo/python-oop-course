from usuarios import Estudiante, Profesor, SolcitanteProtocol
from biblioteca import Biblioteca
from libros import LibroFisico
from exceptions import BibliotecaError, UsuarioNoEncontradoError

biblioteca = Biblioteca("Biblioteca Central")

"""Estudiantes y Profesores"""
estudiante_0 = Estudiante("Patrick", "1234567890", "Ingeniería")
estudiante_1 = Estudiante("Ana", "1234567888", "Medicina")
profesor = Profesor("Dr. Smith", "0000000001", "Ciencias")

"""Libros"""
libro_0 = LibroFisico("1984", "George Orwell", "1234567890")
libro_1 = LibroFisico("Brave New World", "Aldous Huxley", "0987654321")
libro_2 = LibroFisico("Cien años de soledad", "Gabriel Garcia Marquez", "0987654333", False)

"""Agregar usuarios a la biblioteca"""
biblioteca.usuarios = [estudiante_0, estudiante_1, profesor]
"""Agregar libros a la biblioteca"""
biblioteca.libros = [libro_0, libro_1, libro_2]


print("Bienvenido a la biblioteca")
print("Libros disponibles para préstamo:")
for titulo in biblioteca.libros_disponibles():
	print(f"- {titulo}")

print()

curp = input("Ingresa tu CURP para buscar tu usuario: ")

try:
	usuario = biblioteca.buscar_usuario(curp)
	print(f"Usuario encontrado: {usuario.nombre} - CURP: {usuario.curp}")
except UsuarioNoEncontradoError:
	print(f"El usuario no fue encontrado")
