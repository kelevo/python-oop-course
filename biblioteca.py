from exceptions import UsuarioNoEncontradoError


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