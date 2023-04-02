class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.regular_expressions = {}
        self.read()

    def read(self):
        with open(self.filename, "r") as file:  
            for line in file:
                if('let' in line):
                    line = line.replace('let ', '')
                    line = line.replace(" ", "")
                    definition, value = line.split('=')
                    print(value)
                    if(value[0] == '['):
                        if(value[1] == "'"):
                            # HACER LA CUENTA DE LOS -
                            # SI EXISTEN - SE REALIZA UNA ITERACION EN LOS CHARSET
                            # SI NO, SOLO SE TOMA EN CUENTA LOS VALORES QUE SE ENCUENTRAN DENTRO
                            pass
                        elif(value[1] == '"'):
                            pass