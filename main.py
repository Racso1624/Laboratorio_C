# Oscar Fernando López Barrios
# Carné 20679

from filereader import *
from syntaxtree import *

filename = "./tests/slr-1.yal"
file_reader = File(filename)
regex = file_reader.regex
SyntaxTree(regex, "Yalex 1")