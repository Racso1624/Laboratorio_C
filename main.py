# Oscar Fernando López Barrios
# Carné 20679

# Se importan librerias
from filereader import *
from syntaxtree import *

# Se toma el filename
filename = "./tests/slr-4.yal"
# Se obtiene el filereader
file_reader = File(filename)
# Se obtiene la regex
regex = file_reader.regex
# Se crea el arbol
SyntaxTree(regex, "Yalex 4")