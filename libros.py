from abc import ABC, abstractmethod
from typing import Protocol
from exceptions import LibroNoDisponibleError

class LibroProtocol(Protocol):
	def prestar(self) -> str:
		"""Metodo para prestar un libro"""
		...

	def devolver(self) -> str: 
		"""Metodo para devolver un libro"""
		...

	def calcular_duracion(self) -> str:
		"""Metodo para calcular la duración del préstamo"""
		...

class LibroBase(ABC):
	@abstractmethod
	def calcular_duracion(self):
		pass

class Libro(LibroBase):
  
	def __init__(self, titulo, autor, isbn, disponible = True):
		self.titulo = titulo
		self.autor = autor
		self.isbn = isbn
		self.disponible = disponible
		self.__veces_prestado = 0
		
	@classmethod
	def crear_no_disponible(cls, titulo, autor, isbn):
		return cls(titulo, autor, isbn, disponible = False)

	def __str__(self):
		return f"{self.titulo} por {self.autor}, Available: {self.disponible}"
		
	def prestar(self):
		if not self.disponible:
			raise LibroNoDisponibleError(f"El libro {self.titulo} no está disponible para préstamo.")

		if self.disponible:
			self.disponible = False
			self.__veces_prestado += 1
			return f"{self.titulo} Se ha prestado. -- Número total de veces que se ha prestado.: {self.__veces_prestado}"

	def devolver(self):
		self.disponible = True
		return f"{self.titulo} Ha sido devuelto."
	
	def calcular_duracion(self):
		return "La duración del préstamo para libros físicos es de 7 días."

	@property
	def es_popular(self):
		return self.__veces_prestado > 5

	@property
	def veces_prestado(self):
		return self.__veces_prestado

	@veces_prestado.setter
	def veces_prestado(self, times):
		if self.__veces_prestado >= 0:
			self.__veces_prestado = times
		raise ValueError("El número de veces prestado no puede ser negativo.")
	
	@property
	def descripcion_completa(self):
		return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}, Veces prestado: {self.__veces_prestado}"

class LibroFisico(Libro):
	def calcular_duracion(self):
		return "La duración del préstamo para libros físicos es de 7 días."
	
class LibroDigital(Libro):
	def calcular_duracion(self):
		return "La duración del préstamo para libros digitales es de 14 días."