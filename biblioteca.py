from exceptions import UsuarioNoEncontradoError
from libros import LibroDigital, LibroFisico


class Biblioteca:
	def __init__(self, name) -> None:
		self.name = name
		self.libros = []
		self.usuarios = []

	def libros_disponibles(self):
		return [
      libro.titulo
      for libro in self.libros
      if libro.disponible
		]
	
	def buscar_usuario(self, curp):
		for usuario in self.usuarios:
			if usuario.curp == curp:
				return usuario
		raise UsuarioNoEncontradoError(f"El usuario con CURP {curp} no fue encontrado en la biblioteca.")
	
	def agregar_libro(self, tipo_libro, titulo, autor, isbn):
		if tipo_libro == "fisico":
			nuevo_libro = LibroFisico(titulo, autor, isbn)
		else:
			nuevo_libro = LibroDigital(titulo, autor, isbn)
		
		self.libros.append(nuevo_libro)
		return f"El libro {titulo} ha sido agregado a la biblioteca."