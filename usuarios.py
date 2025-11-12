from typing import Protocol

class SolcitanteProtocol(Protocol):
  def solicitar_libro(self, titulo: str) -> str:
    """Metodo que debe implementar cualquier solicitante"""
    ...

class Usuario:
  def __init__(self, nombre, curp):
    self.nombre = nombre
    self.edad = curp
    self.libros_prestados = []

  def solicitar_libro(self, titulo):
    return f"Se ha solicitado el libro: {titulo}"
  

class Estudiante(Usuario):
  def __init__(self, nombre, curp, carrera):
    super().__init__(nombre, curp)
    self.carrera = carrera
    self.limite_libros = 3

  def solicitar_libro(self, titulo):
    if (len(self.libros_prestados) >= self.limite_libros):
      return "Has alcanzado el límite de libros prestados."
    else:
      self.libros_prestados.append(titulo)
      return f"Se ha solicitado el libro: {titulo}"
  

class Profesor(Usuario):
  def __init__(self, nombre, curp, departamento):
    super().__init__(nombre, curp)
    self.departamento = departamento
    self.limite_libros = None
    self.libros_prestados = []

  def solicitar_libro(self, titulo):
    self.libros_prestados.append(titulo)
    return f"Se ha solicitado el libro: {titulo}"