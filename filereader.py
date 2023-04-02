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
                    line_separated = line.split('=')
                    print(line_separated)