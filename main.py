from usuarios import Estudiante, Profesor, SolcitanteProtocol
from biblioteca import Biblioteca
from libros import LibroFisico


biblioteca = Biblioteca("Biblioteca Central")

"""Estudiantes y Profesores"""
estudiante_0 = Estudiante("Patrick", "PAOG850101HDFTRN09", "Ingeniería")
estudiante_1 = Estudiante("Ana", "ANAG920202MDFTRN08", "Medicina")
profesor = Profesor("Dr. Smith", "SMID700202HDFTRN05", "Ciencias")

usuarios: list[SolcitanteProtocol] = [estudiante_0, estudiante_1, profesor]

mi_libro = LibroFisico("1984", "George Orwell", "1234567890", True)
otro_libro = LibroFisico("Brave New World", "Aldous Huxley", "0987654321", True)
libro_no_disponible = LibroFisico("Cien años de soledad", "Gabriel Garcia Marquez", "0987654333", False)

biblioteca.libros.extend([mi_libro, otro_libro, libro_no_disponible])
print(biblioteca.libros_disponibles())