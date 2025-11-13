from libros import LibroDigital, LibroFisico
from usuarios import Estudiante

libro1 = LibroFisico("1984", "George Orwell", "1234567890")
libro2 = LibroFisico("Cien Años de Soledad", "Gabriel Garcia Marquez", "0987654321")
libro3 = LibroFisico("Don Quijote de la Mancha", "Miguel de Cervantes", "1122334455")
libro4 = LibroFisico("El Aleph", "Jorge Luis Borges", "6677889900")
libro5 = LibroFisico("Ficciones", "Jorge Luis Borges", "5544332211")
libro6 = LibroDigital("Rayuela", "Julio Cortázar", "4433221100")
libro7 = LibroDigital("La Sombra del Viento", "Carlos Ruiz Zafón", "3322110099")
libro8 = LibroDigital("La Ciudad y los Perros", "Mario Vargas Llosa", "2211009988")
libro9 = LibroDigital("Pedro Páramo", "Juan Rulfo", "1100998877")
libro10 = LibroDigital("La Metamorfosis", "Franz Kafka", "0099887766")

estudiante1 = Estudiante("Alice", "CURP1234", "Ingeniería")
estudiante2 = Estudiante("Bob", "CURP5678", "Medicina")
estudiante3 = Estudiante("Charlie", "CURP9101", "Derecho")
estudiante4 = Estudiante("Diana", "CURP1121", "Arquitectura")
estudiante5 = Estudiante("Eve", "CURP3141", "Psicología")
estudiante6 = Estudiante("Frank", "CURP5161", "Economía")
estudiante7 = Estudiante("Grace", "CURP7181", "Filosofía")
estudiante8 = Estudiante("Hank", "CURP9202", "Sociología")
estudiante9 = Estudiante("Ivy", "CURP1222", "Antropología")
estudiante10 = Estudiante("Jack", "CURP3242", "Historia")

data_libros = [
    libro1, libro2, libro3, libro4, libro5,
    libro6, libro7, libro8, libro9, libro10
]

data_estudiantes = [
    estudiante1, estudiante2, estudiante3, estudiante4, estudiante5,
    estudiante6, estudiante7, estudiante8, estudiante9, estudiante10
]