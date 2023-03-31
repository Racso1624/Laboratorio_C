class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.regular_expressions = {}
        self.read()

    def read(self):
        with open(self.filename, "r") as file:  
            for line in file:
                comment_start = None
                comment_final = None
                for i in range(len(line)):
                    if(line[i] == "(" and line[i + 1] == "*"):
                        comment_start = i
                    if(line[i] == "*" and line[i + 1] == ")"):
                        comment_final = i + 1
                # GUARDAR LINEAS EN UNA NUEVA ESTRUCTURA DE DATOS PARA EL ARCHIVO
                if(comment_start != None and comment_final != None):
                    pass