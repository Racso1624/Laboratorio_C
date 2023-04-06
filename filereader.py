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
                            separator_counter = value.count('-')
                            if(separator_counter != 0):
                                index_counter = 1
                                first_value = ""
                                second_value = ""
                                first_apostrophe = None
                                second_apostrophe = None
                                while(separator_counter != 0):
                                    if(value[index_counter] == "'" and first_apostrophe == None):
                                        first_apostrophe = index_counter
                                    else:
                                        second_apostrophe = index_counter
                                
                        elif(value[1] == '"'):
                            pass