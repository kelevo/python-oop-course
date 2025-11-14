from abc import ABC, abstractmethod
from typing import Protocol
from exceptions import BibliotecaError, TituloInvalidoError

class SolcitanteProtocol(Protocol):
  def solicitar_libro(self, titulo: str) -> str:
    """Metodo que debe implementar cualquier solicitante"""
    ...

class UsuarioBase(ABC):
  @abstractmethod
  def solicitar_libro(self):
    pass

class Usuario(UsuarioBase):
  def __init__(self, nombre, curp):
    self.nombre = nombre
    self.curp = curp
    self.libros_prestados = []

  def solicitar_libro(self, titulo):
    return f"Se ha solicitado el libro: {titulo}"
  
  @property
  def nombre_completo(self):
    return f"{self.nombre} - CURP: {self.curp}"
  
class Estudiante(Usuario):
  def __init__(self, nombre, curp, carrera):
    super().__init__(nombre, curp)
    self.carrera = carrera
    self.limite_libros = 3

  def solicitar_libro(self, titulo):
    if not titulo:
      raise TituloInvalidoError(f"El título {titulo} del libro no puede estar vacío.")

    if (len(self.libros_prestados) >= self.limite_libros):
      return "Has alcanzado el límite de libros prestados."
    else:
      self.libros_prestados.append(titulo)
      return f"Prestamo del libro: {titulo} autorizado."
  

class Profesor(Usuario):
  def __init__(self, nombre, curp, departamento):
    super().__init__(nombre, curp)
    self.departamento = departamento
    self.limite_libros = None
    self.libros_prestados = []

  def solicitar_libro(self, titulo):
    self.libros_prestados.append(titulo)
    return f"Se ha solicitado el libro: {titulo}"