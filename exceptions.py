class BibliotecaError(Exception):
  """Clase base para excepciones de la biblioteca."""
  pass

class LimitePrestamosError(BibliotecaError):
  """Excepción para cuando se excede el límite de préstamos."""
  pass

class TituloInvalidoError(BibliotecaError):
  """Excepción para títulos de libros inválidos."""
  pass

class LibroNoDisponibleError(BibliotecaError):
  """Excepción para cuando un libro no está disponible."""
  pass

class UsuarioNoEncontradoError(BibliotecaError): 
  """Excepción para cuando un usuario no es encontrado."""
  pass