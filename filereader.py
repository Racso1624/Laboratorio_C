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
                    value_definition = []
                    print(value)
                    if(value[0] == '['):
                        value_definition.append('(')
                        if(value[1] == "'"):
                            separator_counter = value.count('-')
                            if(separator_counter != 0):
                                index_counter = 1
                                first_value = ""
                                second_value = ""
                                first_apostrophe = None
                                second_apostrophe = None
                                while(separator_counter != 0):
                                    if(value[index_counter] == "'" and not first_apostrophe):
                                        first_apostrophe = index_counter
                                    elif(value[index_counter] == "'" and first_apostrophe):
                                        second_apostrophe = index_counter

                                    if(first_apostrophe and second_apostrophe and first_value == ""):
                                        first_value = value[first_apostrophe + 1]
                                        first_apostrophe = None
                                        second_apostrophe = None
                                    elif(first_apostrophe and second_apostrophe and first_value != ""):
                                        second_value = value[first_apostrophe + 1]
                                        first_apostrophe = None
                                        second_apostrophe = None
                                        separator_counter -= 1
                                    
                                    if(first_value != "" and second_value != ""):
                                        first_ascii = ord(first_value)
                                        second_ascii = ord(second_value)
                                        first_value = ""
                                        second_value = ""
                                        if(len(value_definition) > 2):
                                            value_definition.append('|')
                                        for i in range(first_ascii, second_ascii):
                                            value_definition.append(i)
                                            value_definition.append('|')
                                        value_definition.append(second_ascii)

                                    index_counter += 1
                            else:
                                index_counter = 1
                                first_value = ""
                                first_apostrophe = None
                                second_apostrophe = None
                                while(value[index_counter] != ']'):
                                    if(value[index_counter] == "'" and not first_apostrophe):
                                        first_apostrophe = index_counter
                                    elif(value[index_counter] == "'" and first_apostrophe):
                                        second_apostrophe = index_counter
                        elif(value[1] == '"'):
                            pass

                        value_definition.append(')') 
                        print(value_definition)    